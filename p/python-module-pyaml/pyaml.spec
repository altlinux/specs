%define oname pyaml
Name: python-module-%oname
Version: 15.02.1
Release: alt1.git20150216
Summary: pretty-yaml: Pretty YAML serialization
License: WTFPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pyaml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mk-fg/pretty-yaml.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-yaml
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
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
export PYTHONPATH=$PWD
python pyaml/tests/dump.py

%files
%doc COPYING *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.02.1-alt1.git20150216
- Version 15.02.1

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.12.10-alt1.git20141204
- Version 14.12.10

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.11.3-alt1.git20141110
- Version 14.11.3

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.05.7-alt1.git20140528
- Initial build for Sisyphus

