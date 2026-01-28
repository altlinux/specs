Name:           xkbgroup
Version:        0.2.0
Release:        alt1
VCS:            https://github.com/hcpl/xkbgroup

License:        MIT
Summary:        Change the keyboard layout through XKB extension
Source:         %name-%version.tar
Group:          System/X11
Buildarch:      noarch
Patch:          0001-Fix-for-32bit.patch
# Automatically added by buildreq on Sat Jan 17 2026
# optimized out: bash5 libgpg-error openssl-config python3 python3-base python3-dev python3-module-jaraco.context python3-module-jaraco.functools python3-module-jaraco.text python3-module-more-itertools python3-module-packaging python3-module-pkg_resources python3-module-py3dephell python3-module-wheel sh5
BuildRequires: libX11 python3-module-build python3-module-pyproject-installer python3-module-setuptools

%description
Use this library to change the keyboard layout through XKB extension
(subsystem) of the X server system. Both library and command line script
included.

%package -n python3-module-%name
Summary:        Supplement module for %name
Group:          Development/Python3

%description -n python3-module-%name
%summary

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/*

%files -n python3-module-%name
%python3_sitelibdir_noarch/%{name}*

%changelog
* Sat Jan 17 2026 Fr. Br. George <george@altlinux.org> 0.2.0-alt1
- Initial build for ALT
