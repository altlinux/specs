%define _unpackaged_files_terminate_build 1
%define oname mozfile
Name: python-module-%oname
Version: 1.2
Release: alt1.1
Summary: Library of file utilities for use in Mozilla testing
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mozfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/83/e2/ea5cbdecefd2fd824a836fc5bd16c254a903e1597e9708fab427b4024e0b/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-mozhttpd

%py_provides %oname

%description
Library of file utilities for use in Mozilla testing.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

