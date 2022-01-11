%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-pywlroots
Version: 0.14.12
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

%check
%__python3 -m pytest tests

%files
%doc LICENSE README.rst
%python3_sitelibdir/wlroots
%python3_sitelibdir/*.egg-info

%changelog
* Tue Jan 11 2022 Egor Ignatov <egori@altlinux.org> 0.14.12-alt1
- 0.14.12

* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 0.14.11-alt1
- First build for ALT
