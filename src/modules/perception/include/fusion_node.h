#ifndef FUSION_NODE_H
#define FUSION_NODE_H

#include "ros/ros.h"
#include "std_msgs/Bool.h"

namespace fusionad
{
namespace perception
{
namespace fusion
{
class FusionNode
{
  public:
    void initRosComm();
  private:
    ros::NodeHandle fusion_cam_lidar_nh;
    ros::Publisher fusion_cam_lidar_pub;
    ros::Subscriber point_cloud_sub;
    ros::Subscriber yolo_sub;

    int pnt_cnt_thresh;
    bool pnt_cnt_reached, person_detected;

    void fusionCallback();
    bool enoughPointsInBox();
    bool personDetected();
};
} // namespace fusion
} // namespace perception
} // namespace fusionad

#endif
