# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define  modulename ubjson
%define  srcname py-ubjson

Name:    python-module-%modulename
Version: 0.12.0
Release: alt1.1

Summary: Universal Binary JSON draft-12 serializer for Python
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/Iotic-Labs/py-ubjson

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

Source:  %srcname-%version.tar

%description
This is a Python Universal Binary JSON encoder/decoder based on the
draft-12 specification.

%package -n python3-module-%modulename
Summary: Universal Binary JSON draft-12 serializer for Python
Group: Development/Python3

%description -n python3-module-%modulename
This is a Python Universal Binary JSON encoder/decoder based on the
draft-12 specification.

%prep
%setup -n %srcname-%version

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/_ubjson.so
%python_sitelibdir/*.egg-info

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/_ubjson*.so
%python3_sitelibdir/*.egg-info

%changelog
* Sat Oct 20 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt1.1
- Fix unpackages files

* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus
