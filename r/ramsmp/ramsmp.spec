Name: ramsmp
Version: 3.5.0
Release: alt2

Summary: RAMspeed/SMP, a cache and memory benchmarking tool
License: Distributable
Group: System/Kernel and hardware

Url: https://github.com/beefyamoeba5/ramspeed
Source: %name-%version.tar
Patch: ramsmp-3.5.0-alt-e2k.patch

ExclusiveArch: %ix86 x86_64 %e2k
Provides: ramspeed

%define _unpackaged_files_terminate_build 1

%description
RAMspeed/SMP, a cache and memory benchmarking tool (for multiprocessor machines
running UNIX-like operating systems)

%prep
%setup
%patch -p2

%build
mkdir -p temp
yes | sh build.sh Linux

%install
install -pDm755 ramsmp %buildroot%_bindir/%name

%files
%_bindir/%name
%doc LICENCE

%changelog
* Wed Jan 23 2019 Michael Shigorin <mike@altlinux.org> 3.5.0-alt2
- Added e2k build (generic codebase).
- Spec cleanup.

* Thu Dec 06 2018 Konstantin Rybakov <kastet@altlinux.org> 3.5.0-alt1
- Initial build for ALT.

