%define _unpackaged_files_terminate_build 1
%define oname pyaml

Name: python3-module-%oname
Version: 16.12.2
Release: alt2

Summary: pretty-yaml: Pretty YAML serialization
License: WTFPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyaml/
# https://github.com/mk-fg/pretty-yaml.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/aa/bc/68c34bd6c5a7bd6d2ecf94ba7cd2337c9f9be58d670e2edef16fa1e0d6a2/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-yaml
BuildRequires: python3-module-unidecode

%py3_provides %oname


%description
PyYAML-based module to produce pretty and readable YAML-serialized data.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
PyYAML-based module to produce pretty and readable YAML-serialized data.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
export PYTHONPATH=$PWD
%__python3 pyaml/tests/dump.py

%files
%doc COPYING PKG-INFO README README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 16.12.2-alt2
- python2 -> python3

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

