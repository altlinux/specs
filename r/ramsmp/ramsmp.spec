Name: ramsmp
Version: 3.5.0
Release: alt1
Summary: RAMspeed/SMP, a cache and memory benchmarking tool
License: Distributable
Group: System/Kernel and hardware
URL: https://github.com/beefyamoeba5/ramspeed
Source: %name-%version.tar
%define _unpackaged_files_terminate_build 1

ExclusiveArch: %ix86 x86_64

%description
RAMspeed/SMP, a cache and memory benchmarking tool (for multiprocessor machines
running UNIX-like operating systems)

%prep
%setup

%build
mkdir -p temp
/bin/sh ./build.sh Linux \
%ifarch %ix86
	i386
%endif
%ifarch x86_64
	amd64
%endif

%install
install -Dd %buildroot%_bindir
install -m 0755 ramsmp %buildroot%_bindir/

%files
%_bindir/*
%doc LICENCE

%changelog
* Thu Dec 06 2018 Konstantin Rybakov <kastet@altlinux.org> 3.5.0-alt1
- Initial build for ALT.

