%define _unpackaged_files_terminate_build 1
%define oname jellyfish

Name: python3-module-%oname
Version: 0.5.6
Release: alt2

Summary: A library for doing approximate and phonetic matching of strings
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/jellyfish/

# https://github.com/sunlightlabs/jellyfish.git
Source0: https://pypi.python.org/packages/94/48/ddb1458d966f0a84e472d059d87a9d1527df7768a725132fc1d810728386/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


%description
Jellyfish is a python library for doing approximate and phonetic
matching of strings.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Jellyfish is a python library for doing approximate and phonetic
matching of strings.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.6-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.6-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20140812.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20140812
- Initial build for Sisyphus

