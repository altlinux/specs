%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-pywlroots
Version: 0.15.24
Release: alt2

Summary: Python binding to the wlroots library using cffi
License: NCSA
Group: Development/Python3

Url: https://github.com/flacjacket/pywlroots
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-xkbcommon
BuildRequires: python3-module-pywayland
BuildRequires: libxkbcommon-devel
BuildRequires: libwlroots10
BuildRequires: libwlroots-devel
BuildRequires: libinput-devel
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-icccm-devel

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
A Python binding to the wlroots library using cffi. The library uses
pywayland to provide the Wayland bindings and python-xkbcommon to
provide wlroots keyboard functionality.

%prep
%setup
%patch0 -p1

%build
# NOTE(egori): revert '2ef42bb6a2a30f6595b29619cd712d1f38d86724' before building
# with wlroots 0.16.0 see: https://github.com/flacjacket/pywlroots/pull/109
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
