%define _unpackaged_files_terminate_build 1
%define oname minipg

%def_disable check

Name: python3-module-%oname
Version: 0.7.6
Release: alt2

Summary: Yet another PostgreSQL database driver
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/minipg/
# https://github.com/nakagami/minipg.git

Source0: https://pypi.python.org/packages/08/5b/672bb919188d537ac67e3a201b9218208db2ebe156b31cd8b61407706739/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-Cython

%py3_provides %oname


%description
Yet another Python PostgreSQL database driver.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Yet another Python PostgreSQL database driver.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
exit 1

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*


%changelog
* Mon Nov 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.6-alt2
- disable python2

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.7.6-alt1
- Build new version for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.6-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1
- automated PyPI update

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.3-alt1.git20150208.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sat Mar 26 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.3-alt1.git20150208.2
- NMU: Fixed BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1.git20150208.1
- NMU: Use buildreq for BR.

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.git20150208
- Initial build for Sisyphus

