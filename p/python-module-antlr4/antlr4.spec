%define oname antlr4
Name: python-module-%oname
Version: 4.6
Release: alt1.1
Summary: ANTLR 4.5 runtime for Python 2
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/antlr4-python2-runtime/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/65/bd/a66d3ed6862bbad1ef47bbb045ef4e08564b480b6f08f95dd52d785be362/%{oname}-python2-runtime-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools

%py_provides %oname

%description
ANTLR 4.5 runtime for Python 2.

%prep
%setup -q -n %{oname}-python2-runtime-%{version}

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.6-alt1
- automated PyPI update

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.2-alt1
- Version 4.5.2

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5-alt1
- Initial build for Sisyphus

