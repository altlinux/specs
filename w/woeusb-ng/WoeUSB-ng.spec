%define nameB WoeUSB
%define nameD woeusb_ng
%define nameL com.github.woeusb.woeusb-ng

Name: woeusb-ng
Version: 0.2.12
Release: alt2

Summary: A Linux program to create a Windows USB stick installer

License: GPL-3.0-or-later
Group: Archiving/Cd burning
URL: https://github.com/WoeUSB/WoeUSB-ng
VCS: https://github.com/WoeUSB/WoeUSB-ng

BuildArch: noarch

Source: %name-%version.tar

Patch: setup-0.2.12-alt-fixes.patch

Requires: python3-module-termcolor

Conflicts: woeusb

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel git

%description
WoeUSB-ng is a simple tool that enable you to create your own usb
stick windows installer from an iso image or a real DVD. This is
a rewrite of original WoeUSB.


%package -n python3-module-%nameB
Group:   Development/Python3
Summary: Python module for %name
%description -n python3-module-%nameB
%summary.

%prep
%setup
git apply development.patch
%patch -p0
subst 's|usr/local/bin|usr/bin|' miscellaneous/%nameL.policy
subst 's|/usr/share/icons/WoeUSB-ng/|%python3_sitelibdir/%nameB/data/|' miscellaneous/WoeUSB-ng.desktop

%build
%pyproject_build

%install
%pyproject_install
rm %buildroot%python3_sitelibdir/%nameB/woeusb
rm %buildroot%python3_sitelibdir/%nameB/woeusbgui
install -Dm 0644 miscellaneous/%nameL.policy \
    %buildroot%_datadir/polkit-1/actions/%nameL.policy
install -Dm 0644 miscellaneous/WoeUSB-ng.desktop \
    %buildroot%_datadir/applications/WoeUSB-ng.desktop

%files
%doc *.md
%_bindir/woeus*
%_datadir/applications/*.desktop
%_datadir/polkit-1/actions/%nameL.policy

%files -n python3-module-%nameB
%python3_sitelibdir/%nameB/
%python3_sitelibdir/%{pyproject_distinfo %nameD}

%changelog
* Mon Aug 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.12-alt2
- added requires and conflicts

* Sat Aug 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.12-alt1
- Initial build for ALT Linux.
