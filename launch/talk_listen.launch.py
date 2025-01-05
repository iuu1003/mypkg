import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    olympic = launch_ros.actions.Node(
        package='mypkg',
        executable='olympic',
        )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([olympic, listener])
