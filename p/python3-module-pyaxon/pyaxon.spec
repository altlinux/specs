%define oname pyaxon

%def_disable check

Name: python3-module-%oname
Version: 0.5.11
Release: alt6.1

Summary: Python library for AXON
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyaxon/

# https://github.com/intellimath/pyaxon.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython
BuildRequires: python3-module-sphinx

%py3_provides %oname axon
%py3_requires json


%description
pyaxon is an MIT Licensed python library for AXON. AXON is eXtended
Object Notation. It's a simple text based format for interchanging
objects, documents and data. It tries to combine the best of JSON, XML
and YAML.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires yaml
%add_python3_req_skip test_construct test_anonymous

%add_python3_self_prov_path %buildroot%python3_sitelibdir/axon/test/

%description tests
pyaxon is an MIT Licensed python library for AXON. AXON is eXtended
Object Notation. It's a simple text based format for interchanging
objects, documents and data. It tries to combine the best of JSON, XML
and YAML.

This package contains tests for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 test_benchmark.py
%__python3 test_all.py

%files
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/*/test


%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.5.11-alt6.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 0.5.11-alt6
- drop unused BR: rpm-macros-sphinx

* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.11-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.11-alt1.git20150217.2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.11-alt1.git20150217.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sat Mar 26 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.5.11-alt1.git20150217.2
- NMU: Fixed BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.11-alt1.git20150217.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.11-alt1.git20150217
- Initial build for Sisyphus

