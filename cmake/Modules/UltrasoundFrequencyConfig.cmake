INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_ULTRASOUNDFREQUENCY UltrasoundFrequency)

FIND_PATH(
    ULTRASOUNDFREQUENCY_INCLUDE_DIRS
    NAMES UltrasoundFrequency/api.h
    HINTS $ENV{ULTRASOUNDFREQUENCY_DIR}/include
        ${PC_ULTRASOUNDFREQUENCY_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    ULTRASOUNDFREQUENCY_LIBRARIES
    NAMES gnuradio-UltrasoundFrequency
    HINTS $ENV{ULTRASOUNDFREQUENCY_DIR}/lib
        ${PC_ULTRASOUNDFREQUENCY_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(ULTRASOUNDFREQUENCY DEFAULT_MSG ULTRASOUNDFREQUENCY_LIBRARIES ULTRASOUNDFREQUENCY_INCLUDE_DIRS)
MARK_AS_ADVANCED(ULTRASOUNDFREQUENCY_LIBRARIES ULTRASOUNDFREQUENCY_INCLUDE_DIRS)

