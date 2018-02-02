%define _unpackaged_files_terminate_build 1
%define oname pyaml
Name: python-module-%oname
Version: 16.12.2
Release: alt1.1
Summary: pretty-yaml: Pretty YAML serialization
License: WTFPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pyaml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mk-fg/pretty-yaml.git
Source0: https://pypi.python.org/packages/aa/bc/68c34bd6c5a7bd6d2ecf94ba7cd2337c9f9be58d670e2edef16fa1e0d6a2/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-yaml
BuildPreReq: python-module-unidecode

%py_provides %oname

%description
PyYAML-based module to produce pretty and readable YAML-serialized data.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
PyYAML-based module to produce pretty and readable YAML-serialized data.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
export PYTHONPATH=$PWD
python pyaml/tests/dump.py

%files
%doc COPYING PKG-INFO README README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 16.12.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 16.12.2-alt1
- automated PyPI update

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.02.1-alt1.git20150216
- Version 15.02.1

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.12.10-alt1.git20141204
- Version 14.12.10

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.11.3-alt1.git20141110
- Version 14.11.3

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.05.7-alt1.git20140528
- Initial build for Sisyphus

