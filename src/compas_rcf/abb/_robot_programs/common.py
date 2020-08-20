from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import sys

import questionary

from compas_rcf.abb import DOCKER_COMPOSE_PATHS
from compas_rcf.abb import ROBOT_IPS
from compas_rcf.docker import compose_up

log = logging.getLogger(__name__)


def compose_up_driver(target_controller):

    ip = {"ROBOT_IP": ROBOT_IPS[target_controller]}
    compose_up(DOCKER_COMPOSE_PATHS["driver"], check_output=True, env_vars=ip)
    log.debug("Driver services are running.")


def confirm_start():
    if not questionary.confirm("Ready to start program?").ask():
        log.critical("Program exited because user didn't confirm start.")
        print("Exiting.")
        sys.exit()
