%define work_name   %{name}-%{version}
%define build_timestamp %(date +"%Y%m%d")

Name:           libnfsidmap-regex
Version:        %{build_timestamp}
Release:        1
License:        BSD
Url:            https://github.com/isginf/libnfsidmap-regex
BuildRequires:  coreutils git libnfsidmap-devel
BuildRequires:  libtool automake autoconf
Summary:        libnfsidmap plugin using regex based mapping of ids
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
mkdir -p  %{buildroot}/lib64/libnfsidmap/
mkdir -p  %{buildroot}/usr/share/man/man5/
cp .libs/regex.so %{buildroot}/lib64/libnfsidmap/
cp libnfsidmap-regex.5.gz %{buildroot}/usr/share/man/man5/

%files
/lib64/libnfsidmap/regex.so
/usr/share/man/man5/libnfsidmap-regex.5.gz

%changelog
* Tue Mar 24 2020 stefan.walter@inf.ethz.ch
- removed group section feature
- fixed detection of libnfsidmap/nfsutils version
* Tue Feb 27 2018 stefan.walter@inf.ethz.ch
- Changed from iniparser to libini_config.
- Build RPM directly from git.
* Tue Jun 20 2017 stefan.walter@inf.ethz.ch
- First initial package for linux.

