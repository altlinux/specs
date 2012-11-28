Name: whdd
Version: 1.1
Release: alt1

Summary: Diagnostic and recovery tool for block devices
License: GNU GPL
Group: System/Kernel and hardware
Url: https://github.com/krieger-od/whdd

Packager: Pavel Isopenko <pauli@altlinux.org>
Summary(ru_RU.UTF-8): Инструмент для диагностики и восстановления блочных устройств
Source: %name-%version.tar
BuildRequires(pre): cmake
# Automatically added by buildreq on Tue Nov 27 2012
# optimized out: cmake-modules libncurses-devel libstdc++-devel libtinfo-devel
BuildRequires: cmake gcc-c++ libdialog-devel libncursesw-devel

%description
WHDD is a diagnostic and recovery tool for block devices (near to replace MHDD for Linux).
%description -l ru_RU.UTF-8
WHDD - инструмент для диагностики и восстановления блочных устройств (как бы замена MHDD для Linux).

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%attr(4711, root, root) %_sbindir/whdd-c*

%changelog
* Mon Nov 26 2012 Pavel Isopenko <pauli@altlinux.org> 1.1-alt1
- Initial build for Sisyphus
- Add ncursesw to target_link_libraries()

