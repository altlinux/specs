%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-pywlroots
Version: 0.15.24
Release: alt1

Summary: Python binding to the wlroots library using cffi
License: NCSA
Group: Development/Python3

Url: https://github.com/flacjacket/pywlroots
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: libxkbcommon-devel
BuildRequires: libwlroots-devel
BuildRequires: libinput-devel
BuildRequires: libxcb-devel
BuildRequires: python3-module-xkbcommon
BuildRequires: python3-module-pywayland

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
%__python3 ./wlroots/ffi_build.py
%python3_build

%install
%python3_install

# hack to drop .abi3 from binaries
find %buildroot -name '*.abi3*' -exec rename '.abi3' '' {} \;

%check
%__python3 -m pytest tests

%files
%doc LICENSE README.rst
%python3_sitelibdir/wlroots
%python3_sitelibdir/*.egg-info

%changelog
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
