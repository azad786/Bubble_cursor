import math
import random


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class ObjectManager:
    def __init__(self, canvas, window_width, window_height, object_num, object_radius):
        self.canvas = canvas
        self.window_width = window_width
        self.window_height = window_height
        self.object_num = object_num  # object number
        self.object_radius = object_radius
        self.objects = []  # store all objects
        self.object_tag_in_canvas = []  # store the tag of the objects in canvas
        self.last_selected_object_index = 0

    def update_object_mouse_click(self, object_index):
        # object_tag is used to find the object in canvas, so that we can update the object
        if object_index >= 0: # a target has been selected
            object_tag = self.object_tag_in_canvas[object_index]
            self.canvas.itemconfig(object_tag, fill="yellow", outline="gray", width=4)  # red indicates the selected target

    def update_object(self, object_index):
        if object_index >= 0:  # a target has been selected
            if self.last_selected_object_index != object_index:
                last_object_tag = self.object_tag_in_canvas[self.last_selected_object_index]
                # update object according to their tag
                self.canvas.itemconfig(last_object_tag, fill="green", width=0)
                self.last_selected_object_index = object_index

                # object_tag is used to find the object in canvas, so that we can update the object
                object_tag = self.object_tag_in_canvas[object_index]
                self.canvas.itemconfig(object_tag, fill="red", outline="gray", width=4)  # red indicates the selected target
        else:  # no target has been selected, we change the previously selected target to green
            last_object_tag = self.object_tag_in_canvas[self.last_selected_object_index]
            # update object according to their tag
            self.canvas.itemconfig(last_object_tag, fill="green", width=0)
            self.last_selected_object_index = object_index

    def paint_objects(self):
        for t in self.objects:
            tag = self.canvas.create_oval(t.x - t.radius, t.y - t.radius, t.x + t.radius, t.y + t.radius, fill="green",
                                          outline="green", width=0)
            # add object's tag to the list, so they can be accessed according to their tag
            # note that objects are indexed in the same order in both objects and object_tag_in_canvas lists
            self.object_tag_in_canvas.append(tag)

    def generate_random_targets(self):
        i = 0
        while i < self.object_num:
            new_object = Circle(random.randint(self.object_radius, self.window_width - self.object_radius),
                                random.randint(self.object_radius, self.window_height - self.object_radius),
                                self.object_radius)
            overlap = False
            for j in self.objects:
                if self.check_two_targets_overlap(new_object, j):
                    overlap = True
                    break

            if not overlap:  # if the new object does not overlap with others, add it to the objects list.
                self.objects.append(new_object)
                i += 1

        self.paint_objects()
        self.generate_start_target_object()
        return self.objects

    def check_two_targets_overlap(self, t1, t2):
        if math.hypot(t1.x - t2.x, t1.y - t2.y) > (t1.radius + t2.radius):
            return False
        else:
            return True

    def generate_start_target_object(self):
        start_object = Circle(50, 700, self.object_radius)

        target_object = Circle(random.randint(self.object_radius, self.window_width - self.object_radius),
                              random.randint(self.object_radius, self.window_height - self.object_radius),
                              self.object_radius)

        tag = self.canvas.create_oval(start_object.x - start_object.radius, start_object.y - start_object.radius, start_object.x + start_object.radius, start_object.y + start_object.radius, fill="blue",
                                      outline="blue", width=0)
        # add object's tag to the list, so they can be accessed according to their tag
        # note that objects are indexed in the same order in both objects and object_tag_in_canvas lists
        self.object_tag_in_canvas.append(tag)

        tag = self.canvas.create_oval(target_object.x - target_object.radius, target_object.y - target_object.radius,
                                      target_object.x + target_object.radius, target_object.y + target_object.radius,
                                      fill="red",
                                      outline="red", width=0)
        # add object's tag to the list, so they can be accessed according to their tag
        # note that objects are indexed in the same order in both objects and object_tag_in_canvas lists
        self.object_tag_in_canvas.append(tag)

    '''
    def _euclidean_distance(self, point_1, point_2):
        return math.hypot(point_1.x - point_2.x,
                          point_1.y - point_2.y)
    '''
