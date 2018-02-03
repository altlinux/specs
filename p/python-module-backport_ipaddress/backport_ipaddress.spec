%define oname backport_ipaddress
Name: python-module-%oname
Version: 0.1
Release: alt1.git20140816.1
Summary: Backport of Python 3's ipaddress module
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/backport_ipaddress/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sk-/backport_ipaddress.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-pytest
BuildPreReq: python-module-unittest2 python-module-nose

%py_provides %oname

%description
backport_ipaddress is a backport of Python 3's ipaddress module for
Python 2.6 and Python 2.7. It is based on the backport of Soren Lovborg
(https://bitbucket.org/kwi/py2-ipaddress/).

%prep
%setup

%build
%python_build_debug

%install
%python_install

pushd %buildroot%python_sitelibdir
for i in ipaddress.*; do
	mv $i backport_$i
done
popd

%check
python setup.py test
rm -fR build original
py.test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt1.git20140816.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140816
- Initial build for Sisyphus

