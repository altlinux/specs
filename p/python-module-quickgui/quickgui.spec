%define _unpackaged_files_terminate_build 1
%define oname quickgui
Name: python-module-%oname
Version: 1.5.6
Release: alt1.1
Summary: Rapidly create gui without any knowledge of wxpython
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/quickgui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/8d/b2/48aaee524be9577393d404bdf4fdeaa1dd99d40e9fa48b40c98d2b1334fe/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-wx3.0

%py_provides %oname
Requires: python-module-wx > 2.9

%description
Rapidly create GUI without any knowledge of wxpython.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.6-alt1
- automated PyPI update

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus

