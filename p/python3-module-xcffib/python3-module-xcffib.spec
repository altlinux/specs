%define _unpackaged_files_terminate_build 1
%define modulename xcffib

%def_with check

Name: python3-module-%modulename
Version: 1.12.0
Release: alt1

Summary: A drop-in replacement for xpyb based on cffi
License: Apache-2.0
Group: Development/Python3
URL: https://github.com/tych0/xcffib

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-cffi
BuildRequires: xorg-xcbproto-devel

BuildRequires(pre): rpm-build-haskell-vendored
BuildRequires: ghc-devel cabal-install

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: xorg-xvfb xeyes
%endif

Requires: libxcb

BuildArch: noarch

Source: %name-%version.tar

# Vendor
Patch0: %name-%version-alt.patch

%description
%summary

%prep
%setup
%patch0 -p1

%build
%cabal_vendor_build
%cabal_vendor_run xcffibgen -- --input /usr/share/xcb --output ./xcffib
touch ./xcffib/py.typed

cp ./module/*py ./xcffib/
XCBVER="$(pkg-config --modversion xcb-proto)"
sed -i "s/__xcb_proto_version__ = .*/__xcb_proto_version__ = \"$XCBVER\"/" xcffib/__init__.py
sed -i "s/__version__ = .*/__version__ = \"%version\"/" xcffib/__init__.py

%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Wed Apr 22 2026 Leonid Znamenok <respublica@altlinux.org> 1.12.0-alt1
- New version 1.12.0.

* Tue Mar 31 2026 Leonid Znamenok <respublica@altlinux.org> 1.11.2-alt1.1
- Fixed FTBFS with ghc-1:9.6.7-alt2.

* Wed Oct 15 2025 Leonid Znamenok <respublica@altlinux.org> 1.11.2-alt1
- 1.11.2

* Sun Jun 08 2025 Leonid Znamenok <respublica@altlinux.org> 1.9.0-alt1
- 1.9.0
- Build generator using rpm-build-haskell-vendored
- Enable test suite

* Wed Sep 27 2023 Egor Ignatov <egori@altlinux.org> 1.5.0-alt1
- 1.5.0

* Wed Nov 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.1-alt2
- Add requires to libxcb

* Tue Dec 14 2021 Egor Ignatov <egori@altlinux.org> 0.11.1-alt1
- 0.11.1

* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus
