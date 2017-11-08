ACLOCAL_AMFLAGS = -I m4

lib_LTLIBRARIES = regex.la

regex_la_SOURCES = regex.c
regex_la_LDFLAGS = -module -avoid-version
regex_la_CFLAGS = $(AM_CFLAGS)
regex_la_LIBADD = -lnfsidmap -lini_config

man5_MANS       = libnfsidmap-regex.5

EXTRA_DIST = $(man5_MANS) nfsidmap_internal.h

pkgconfigdir=$(libdir)/pkgconfig

