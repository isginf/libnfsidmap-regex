# Process this file with autoconf to produce a configure script.
AC_PREREQ([2.63])
AC_INIT([libnfsidmap-regex],[0.1],[stefan.walter@inf.ethz.ch])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE
LT_INIT

# Checks for programs.
AC_PROG_CC

# Checks for typedefs, structures, and compiler characteristics.
AC_TYPE_UID_T
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_MALLOC
AC_CHECK_FUNCS([strchr strdup])

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS([stdlib.h string.h unistd.h errno.h])

AC_CHECK_HEADERS([nfsidmap_internal.h], [], [], [[#include <sys/types.h>
#include <stddef.h>
#include "nfsidmap.h"]])
AC_CHECK_HEADERS([nfsidmap_plugin.h], [], [], [[#include <sys/types.h>
#include <stddef.h>
#include "nfsidmap.h"]])

AC_CHECK_DECLS([conf_get_str], [], [], [[#include <sys/types.h>
#include <stddef.h>
#include "nfsidmap.h"
#ifdef HAVE_NFSIDMAP_INTERNAL_H
#include "nfsidmap_internal.h"
#endif
#ifdef HAVE_NFSIDMAP_PLUGIN_H
#include "nfsidmap_plugin.h"
#endif
]])
AC_CHECK_DECLS([nfsidmap_config_get], [], [], [[#include <sys/types.h>
#include <stddef.h>
#include "nfsidmap.h"
#ifdef HAVE_NFSIDMAP_INTERNAL_H
#include "nfsidmap_internal.h"
#endif
#ifdef HAVE_NFSIDMAP_PLUGIN_H
#include "nfsidmap_plugin.h"
#endif
]])

#Set the NFSv4 idmapd library install path
AC_ARG_ENABLE([nfsidmaplibdir], [AS_HELP_STRING([--enable-nfsidmaplibdir],
                                        [Where to install libnfsidmap libraries ($libdir/libnfsidmap)])],
              [nfsidmaplibdir=$enableval],
              [nfsidmaplibdir=$libdir/libnfsidmap])
AC_SUBST(nfsidmaplibdir)

AC_CONFIG_FILES([Makefile])
AC_OUTPUT

