%define _unpackaged_files_terminate_build 1
%define modulename xcffib

%def_without generator

Name: python3-module-%modulename
Version: 1.5.0
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

%if_with generator
BuildRequires(pre): rpm-build-haskell

BuildRequires: ghc8.6.4
BuildRequires: ghc8.6.4-split
BuildRequires: ghc8.6.4-filemanip
BuildRequires: ghc8.6.4-xml
BuildRequires: ghc8.6.4-attoparsec
BuildRequires: ghc8.6.4-cabal-install
BuildRequires: ghc8.6.4-optparse-applicative

# Not in sisyphus yet
#BuildRequires: ghc8.6.4-either
#BuildRequires: ghc8.6.4-language-python
#BuildRequires: ghc8.6.4-xcb-types
%endif

Requires: libxcb

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

%description
%summary

%prep
%setup
%patch0 -p1

%build

%if_with generator
cd generator
ghc ./xcffibgen.hs
cd -
generator/xcffibgen --input /usr/share/xcb --output ./xcffib
touch ./xcffib/py.typed
%endif

cp ./module/*py ./xcffib/
XCBVER="$(pkg-config --modversion xcb-proto)"
sed -i "s/__xcb_proto_version__ = .*/__xcb_proto_version__ = \"$XCBVER\"/" xcffib/__init__.py
sed -i "s/__version__ = .*/__version__ = \"%version\"/" xcffib/__init__.py

%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Wed Sep 27 2023 Egor Ignatov <egori@altlinux.org> 1.5.0-alt1
- 1.5.0

* Wed Nov 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.1-alt2
- Add requires to libxcb

* Tue Dec 14 2021 Egor Ignatov <egori@altlinux.org> 0.11.1-alt1
- 0.11.1

* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus
