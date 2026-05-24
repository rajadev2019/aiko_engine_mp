#!/bin/bash
# mpfshell without --reset (use when board is busy or CH340 needs soft connect)
MPF_SCRIPT=$1
mpfshell -o ${AMPY_PORT:4} -s "$MPF_SCRIPT"
