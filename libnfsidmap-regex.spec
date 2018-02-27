%define work_name   %{name}-%{version}
%define build_timestamp %(date +"%Y%m%d")

Name:           libnfsidmap-regex
Version:        %{build_timestamp}
Release:        1
License:        BSD
Url:            https://github.com/isginf/libnfsidmap-regex
%if 0%{?rhel} == 6
BuildRequires:  nfs-utils-lib-devel
%else
BuildRequires:  libnfsidmap-devel
%endif
BuildRequires:  coreutils git
BuildRequires:  libtool automake autoconf
BuildRequires:  libini_config-devel
Requires:       libini_config
Summary:        libnfsidmap plugin using regex based mapping
%description
The regex plugin parses NFSv4 user and groups names using regex to extract the local user or group. NFSv4 names are created by adding constant strings before and after the local user and group names.

%prep
rm -rf %{work_name}
git clone %{url}.git %{work_name}

%build
cd %{work_name}
sh autogen.sh
%configure
make %{?_smp_mflags}
gzip -9 libnfsidmap-regex.5

%install
cd %{work_name}
rm -rf %{buildroot}
mkdir -p  %{buildroot}/usr/lib64/libnfsidmap/
mkdir -p  %{buildroot}/usr/share/man/man5/
cp .libs/regex.so %{buildroot}/usr/lib64/libnfsidmap/
cp libnfsidmap-regex.5.gz %{buildroot}/usr/share/man/man5/

%files
/usr/lib64/libnfsidmap/regex.so
/usr/share/man/man5/libnfsidmap-regex.5.gz

%changelog
* Tue Feb 27 2018 stefan.walter@inf.ethz.ch
- Changed from iniparser to libini_config.
- Build RPM directly from git.
* Tue Jun 20 2017 stefan.walter@inf.ethz.ch
- First initial package for linux.

