Name: alt-os-release
Version: 0.1.1
Release: alt1

Summary: RPM filetrigger to generate /etc/os-release file
License: GPLv2+
Group: System/Base

Source: %name-%version.tar
BuildArch: noarch

%description
This package contains a RPM filetrigger to generate /etc/os-release file.

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/
touch %buildroot%_sysconfdir/os-release
install -pDm755 alt-os-release.filetrigger %buildroot%_rpmlibdir/alt-os-release.filetrigger

%files
%ghost %_sysconfdir/os-release
%_rpmlibdir/alt-os-release.filetrigger

%changelog
* Fri Oct 01 2021 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Fixed cleanup_handler() (thx andy@).

* Wed Sep 29 2021 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build.
