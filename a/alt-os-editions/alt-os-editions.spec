Name: alt-os-editions
Version: 0.1.0
Release: alt1

Summary: RPM filetrigger to update edition in dconf 
License: GPLv2+
Group: System/Base

Source: %name-%version.tar
BuildArch: noarch

Requires: dconf-profile >= 0.2

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_rpmlibdir/
install -pDm755 x-alt-os-editions.filetrigger %buildroot%_rpmlibdir

%files
%_rpmlibdir/x-alt-os-editions.filetrigger

%changelog
* Tue Jan 28 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
