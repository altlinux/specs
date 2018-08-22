%define  modulename pytrie

Name:    python-module-%modulename
Version: 0.3.1
Release: alt1

Summary: Pure Python implementation of the trie data structure
License: BSD
Group:   Development/Python3
URL:     https://github.com/gsakkis/pytrie/

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

Source:  %modulename-%version.tar

BuildArch: noarch

%description
Concise Binary Object Representation (CBOR) is a superset of JSON's
schema that's faster and more compact.

%package -n python3-module-%modulename
Summary: CBOR rfc7049 for Python 
Group: Development/Python3

%description -n python3-module-%modulename
Concise Binary Object Representation (CBOR) is a superset of JSON's
schema that's faster and more compact.

Python 3 version.

%prep
%setup -n %modulename-%version

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%python_sitelibdir/*

%files -n python3-module-%modulename
%python3_sitelibdir/*

%changelog
* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus
