%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-pywlroots
Version: 0.17.0
Release: alt2

Summary: Python binding to the wlroots library using cffi
License: NCSA
Group: Development/Python3

Url: https://github.com/flacjacket/pywlroots
Source: %name-%version.tar
Source1: wlr-%version.tar

Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-xkbcommon
BuildRequires: python3-module-pywayland
BuildRequires: libxkbcommon-devel
BuildRequires: libinput-devel
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-icccm-devel

# wlroots is poorly maintained, so just vendor headers from libwlroots-devel
# See: https://bugzilla.altlinux.org/54843
# See: https://lists.altlinux.org/pipermail/devel/2025-June/219307.html
BuildRequires: libwayland-server-devel
BuildRequires: libpixman-devel
BuildRequires: libwlroots12
%global libwlroots_file libwlroots.so.12

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
A Python binding to the wlroots library using cffi. The library uses
pywayland to provide the Wayland bindings and python-xkbcommon to
provide wlroots keyboard functionality.

%prep
%setup -a1
%patch0 -p1

sed -i -e "/libraries=/ s/wlroots/:%libwlroots_file/" ./wlroots/ffi_build.py

%build
export CFLAGS="-I$PWD/wlroots/include"
%__python3 ./wlroots/ffi_build.py
%pyproject_build

%install
%pyproject_install

# hack to drop .abi3 from binaries
find %buildroot -name '*.abi3*' -exec rename '.abi3' '' {} \;

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.rst
%python3_sitelibdir/wlroots
%python3_sitelibdir/%{pyproject_distinfo pywlroots}

%changelog
* Mon Jun 23 2025 Egor Ignatov <egori@altlinux.org> 0.17.0-alt2
- fix FTBFS: build with old libwlroots 0.17.4

* Thu May 30 2024 Egor Ignatov <egori@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Fri Apr 19 2024 Egor Ignatov <egori@altlinux.org> 0.16.7-alt1
- new version 0.16.7

* Wed Sep 27 2023 Egor Ignatov <egori@altlinux.org> 0.16.5-alt1
- new version 0.16.5

* Sun Jan 15 2023 Egor Ignatov <egori@altlinux.org> 0.15.24-alt2
- fix FTBFS: build with old libwlroots 0.15.1

* Sun Oct 30 2022 Egor Ignatov <egori@altlinux.org> 0.15.24-alt1
- new version 0.15.24

* Thu Sep 22 2022 Egor Ignatov <egori@altlinux.org> 0.15.22-alt1
- new version 0.15.22

* Mon Sep 19 2022 Egor Ignatov <egori@altlinux.org> 0.15.21-alt1
- new version 0.15.21

* Wed Aug 31 2022 Egor Ignatov <egori@altlinux.org> 0.15.20-alt1
- new version 0.15.20

* Tue Jul 26 2022 Egor Ignatov <egori@altlinux.org> 0.15.19-alt1
- new version 0.15.19

* Mon Jun 27 2022 Egor Ignatov <egori@altlinux.org> 0.15.18-alt1
- new version 0.15.18

* Tue Jun 07 2022 Egor Ignatov <egori@altlinux.org> 0.15.17-alt1
- new version 0.15.17

* Mon May 30 2022 Egor Ignatov <egori@altlinux.org> 0.15.15-alt1
- new version 0.15.15

* Wed May 18 2022 Egor Ignatov <egori@altlinux.org> 0.15.14-alt1
- new version 0.15.14

* Tue Apr 19 2022 Egor Ignatov <egori@altlinux.org> 0.15.13-alt1
- add hack to drop .abi3 from binaries
- new version 0.15.13

* Fri Apr 15 2022 Egor Ignatov <egori@altlinux.org> 0.15.12-alt1
- new version 0.15.12

* Thu Feb 24 2022 Egor Ignatov <egori@altlinux.org> 0.15.10-alt1
- new version 0.15.10

* Mon Feb 14 2022 Egor Ignatov <egori@altlinux.org> 0.15.8-alt1
- new version 0.15.8

* Wed Feb 09 2022 Egor Ignatov <egori@altlinux.org> 0.15.7-alt1
- new version 0.15.7

* Fri Jan 28 2022 Egor Ignatov <egori@altlinux.org> 0.15.3-alt1
- new version 0.15.3

* Mon Jan 17 2022 Alexey Gladkov <legion@altlinux.ru> 0.15.1-alt1
- NMU: New version (0.15.1).

* Sat Jan 15 2022 Alexey Gladkov <legion@altlinux.ru> 0.15.0-alt1
- NMU: New version (0.15.0).

* Tue Jan 11 2022 Egor Ignatov <egori@altlinux.org> 0.14.12-alt1
- 0.14.12

* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 0.14.11-alt1
- First build for ALT
