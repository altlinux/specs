Name: masscan
Version: 1.0.5
Release: alt1

Summary: The fastest Internet port scanner
Group: Monitoring
License: AGPL-3
Url: https://github.com/robertdavidgraham/masscan

Source: %name.tar

Patch0: debian_buildsystem.patch
Patch1: debian_fix-spelling-errors.patch
Patch2: debian_use-gcc-instead-of-clang.patch
Patch3: alt_fix-version.patch

BuildRequires: gcc
BuildRequires: libpcap-devel

%description
This is the fastest Internet port scanner. It can scan the entire Internet in
under 6 minutes, transmitting 10 million packets per second. It produces results
similar to nmap, the most famous port scanner. Internally, it operates more like
scanrand, unicornscan, and ZMap, using asynchronous transmission. The major
difference is that it's faster than these other scanners. In addition, it's more
flexible, allowing arbitrary address ranges and port ranges.

%prep
%setup -n %name
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/masscan
%doc LICENSE VULNINFO.md README.md

%check
make regress

%changelog
* Fri Oct 05 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.0.5-alt1
- initial build of masscan 1.0.5
