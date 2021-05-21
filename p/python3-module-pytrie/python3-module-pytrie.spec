%define  modulename pytrie

Name:    python3-module-%modulename
Version: 0.4.0
Release: alt1

Summary: Pure Python implementation of the trie data structure
License: BSD
Group:   Development/Python3
URL:     https://github.com/gsakkis/pytrie/

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

Source:  %modulename-%version.tar

BuildArch: noarch

%description
Concise Binary Object Representation (CBOR) is a superset of JSON's
schema that's faster and more compact.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Wed May 19 2021 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- new version 0.4.0
- python 3 only

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus
