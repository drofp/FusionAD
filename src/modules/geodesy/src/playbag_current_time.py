#!/usr/bin/env python

"""Play bag using current system time for selected topics.

Usage
=====
Make sure ROS Master is running, then run this node with:
```
rosrun package_name playbag_current_time.py
```

Parameters
==========
Change the following variables to fit use case in main()
- bag_path = Full path to bag (string)
- topics = Topics (dict -- maps topic to message type)
"""

from __future__ import print_function
from __future__ import division

import rospy
import rosbag

# Add message definitions as necessary

class BagPlayerRealTime(object):
    def __init__(self, bag_path="", topics={}):
        self.bag_path = bag_path
        self.topics = topics

        self.publishers = self.create_publishers(topics)
        self.callbacks = self.create_callbacks(topics)
    
    def create_publishers(self, topics):
        publishers = []

        for topic, message_type in topics.iteritems():
            publishers.append(rospy.Publisher(topic, message_type))
        
        return publishers

    def create_callback(self, topics):
        def callback(self, topics):
            """Republish with current timestamp"""

        return callback
    
    def create_callbacks(self, topics):
        callbacks = []

        for topic in topics:
            callbacks.append(self.create_callback(topics))

        return callbacks
    
    def run(self):
        """Instantiate and run arbitrary number of subscribers"""


        rospy.spin()

def main():
    bag_path = ""
    topics = {}

if __name__ == "__main__":
    main()

