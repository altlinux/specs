%define mname scikits
%define oname %mname.bootstrap

%def_with check

Name: python3-module-%oname
Version: 1.1.0
Release: alt1

Summary: Bootstrap confidence interval estimation routines for Numpy/Scipy/Pandas
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/scikits.bootstrap/
VCS: https://github.com/cgevans/scikits-bootstrap.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-erf
BuildRequires: python3-module-pytest-cov
%endif

%py3_provides %oname

%description
Scikits.bootstrap provides bootstrap statistics confidence interval algorithms
for Numpy/Scipy/Pandas. It originally required scipy, but no longer needs it.

It also provides an algorithm which estimates the probability that the
statistics lies satisfies some criteria, e.g., lies in some interval.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%ifnarch %ix86
%tox_check
%else
%tox_check -- -k 'not test_abc_simple'
%endif

%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%files
%doc LICENSE *.md
%python3_sitelibdir/%mname
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Tue Mar 14 2023 Anton Vyatkin <toni@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Tue Aug 25 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2
- Fixed build with new numpy.

* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt1
- version updated to 1.0.1
- build for python2 disabled

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1.1
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20150327.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20150327.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20150327
- New snapshot

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20140521
- Initial build for Sisyphus

