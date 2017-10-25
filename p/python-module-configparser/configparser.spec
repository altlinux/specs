%define _unpackaged_files_terminate_build 1

%define mname configparser

Name: python-module-%mname
Version: 3.5.0
Release: alt1%ubt
Summary: This library brings the updated configparser from Python 3.5 to Python 2.6-3.5

Group: Development/Python
License: MIT
Url: https://pypi.python.org/pypi/configparser

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

Requires: python-module-setuptools
%py_provides %mname

%description
The ancient ConfigParser module available in the standard library 2.x has seen a
major update in Python 3.2. This is a backport of those changes so that they can
be used directly in Python 2.6 - 3.5.

%package -n python3-module-%mname
Summary: This library brings the updated configparser from Python 3.5 to Python 2.6-3.5
Group: Development/Python3
Requires: python3-module-setuptools
%py3_provides %mname

%description -n python3-module-%mname
The ancient ConfigParser module available in the standard library 2.x has seen a
major update in Python 3.2. This is a backport of those changes so that they can
be used directly in Python 2.6 - 3.5.

%prep
%setup
rm -rfv *.egg-info
rm -rfv ../python3
cp -a . ../python3

%build
%python_build_debug
pushd ../python3
%python3_build_debug
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%check
python setup.py test
pushd ../python3
python3 setup.py test
popd

%files
%python_sitelibdir/*

%files -n python3-module-%mname
%python3_sitelibdir/*

%changelog
* Wed Oct 25 2017 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1%ubt
- Initial build

