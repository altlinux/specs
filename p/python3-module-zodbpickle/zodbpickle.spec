%define oname zodbpickle

%def_without check

Name: python3-module-%oname
Version: 0.6.1
Release: alt2
Summary: Fork of Python 3 pickle module

License: ZPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/zodbpickle/
# https://github.com/zopefoundation/zodbpickle.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%add_findreq_skiplist %python3_sitelibdir/%oname/pickle_2.py
%add_findreq_skiplist %python3_sitelibdir/%oname/pickletools_2.py
%add_findreq_skiplist %python3_sitelibdir/%oname/tests/pickletester_2.py

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-nose
BuildRequires: python3-module-pytest
%endif


%description
This package presents a uniform pickling interface for ZODB.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip __main__ cStringIO

%description -n python3-module-%oname-tests
This package presents a uniform pickling interface for ZODB.

This package contains tests for %oname.

%prep
%setup

sed -i 's|import cStringIO|from io import cStringIO|' \
    $(find ./ -name '*.py')

for i in $(find ../python3 -type f -name '*.py'); do
	2to3 -w -n $i ||:
done

%build
%add_optflags -fno-strict-aliasing

%python3_build_debug

%install
%python3_install

%if_with check
%check
python3 setup.py test
%endif

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt2
- disable python2, ebable python3

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1.dev0.git20150414.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1.dev0.git20150414.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.dev0.git20150414.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1.dev0.git20150414.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.dev0.git20150414
- Version 0.6.1.dev0
- Enabled check

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20130817
- Initial build for Sisyphus

