Name:           libnfsidmap-regex
Version:        0.1
Release:        1
License:        BSD
Url:            https://github.com/isginf/libnfsidmap-regex
BuildRequires:  coreutils
Requires:       coreutils
Summary:        libnfsidmap plugin using regex based mapping
Source:         libnfsidmap-regex-0.1.tar.gz

%description
The regex plugin parses NFSv4 user and groups names using regex to extract the local user or group. NFSv4 names are created by adding constant strings before and after the local user and group names.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}
gzip -9 libnfsidmap-regex.5

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/lib64/libnfsidmap/
mkdir -p  %{buildroot}/usr/share/man/man5/
cp .libs/regex.so %{buildroot}/lib64/libnfsidmap/
cp libnfsidmap-regex.5.gz %{buildroot}/usr/share/man/man5/

%files
/lib64/libnfsidmap/regex.so
/usr/share/man/man5/libnfsidmap-regex.5.gz

%changelog
