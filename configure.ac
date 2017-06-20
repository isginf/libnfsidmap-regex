# Process this file with autoconf to produce a configure script.
AC_PREREQ([2.66])
AC_CONFIG_MACRO_DIR([m4])
AC_INIT([libnfsidmap-regex],[0.1],[stefan.walter@inf.ethz.ch])
AM_INIT_AUTOMAKE
LT_INIT

# Checks for programs.
AC_PROG_CC

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS([nfsidmap.h stdlib.h string.h unistd.h errno.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_TYPE_UID_T
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_MALLOC
AC_CHECK_FUNCS([strchr strdup])

#Set the NFSv4 idmapd library install path
AC_ARG_ENABLE([nfsidmaplibdir], [AS_HELP_STRING([--enable-nfsidmaplibdir],
                                        [Where to install libnfsidmap libraries ($libdir/libnfsidmap)])],
              [nfsidmaplibdir=$enableval],
              [nfsidmaplibdir=$libdir/libnfsidmap])
AC_SUBST(nfsidmaplibdir)

AC_CONFIG_FILES([Makefile])
AC_OUTPUT

