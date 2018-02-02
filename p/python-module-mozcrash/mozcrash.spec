%define _unpackaged_files_terminate_build 1
%define oname mozcrash
Name: python-module-%oname
Version: 1.0
Release: alt1.1
Summary: Library for printing stack traces from minidumps left behind by crashed processes
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mozcrash/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/fa/a7/5caf82d2d44ac2bea78dbd6465ec11e692f408ed15dd65adad4438d49745/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-mozfile python-module-mozlog

%py_provides %oname

%description
Library for printing stack traces from minidumps left behind by crashed
processes.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1
- Initial build for Sisyphus

