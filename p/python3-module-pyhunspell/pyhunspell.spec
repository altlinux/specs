%define modulename pyhunspell

Name: python3-module-%modulename
Version: 0.5.4
Release: alt1
Summary: Python 3 bindings for hunspell

License: LGPLv3+
Group: Development/Python3
Url: https://github.com/blatinier/pyhunspell
#Source-url: https://github.com/blatinier/pyhunspell/archive/pyhunspell-%version.tar.gz
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %modulename-%version.tar
BuildRequires: gcc-c++
BuildRequires: libhunspell-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

# make it build with hunspell-1.5:
#Patch: pyhunspell-0.5.0-hunspell15.patch

%description
These are python 3 bindings for hunspell, that allow
to use the hunspell library in python.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS.md CHANGELOG.md PKG-INFO README.md
%python3_sitelibdir/*

%changelog
* Fri May 21 2021 Anton Midyukov <antohami@altlinux.org> 0.5.4-alt1
- initial build
