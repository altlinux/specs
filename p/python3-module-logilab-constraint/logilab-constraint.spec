%define oname logilab-constraint

%def_with check

Name: python3-module-%oname
Version: 0.8.0
Release: alt1

Summary: A constraint satisfaction problem solver written in 100%% pure Python
License: LGPL
Group: Development/Python3
URL: https://pypi.org/project/logilab-constraint

BuildArch: noarch

Source: constraint-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-logilab-common
BuildRequires: python3-module-six
%endif

%description
The constraint package is a constraint satisfaction problem solver
written in 100%% pure Python. The implementation uses constraint
propagation algorithms. Constraints and Domain implementations are
provided to work with finite domains and finite intervals. It should be
fairly easy to add new kind of domains such as finite integer domains,
together with specialized constraints.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -k 'not Abstract'

%files
%doc COPYING ChangeLog README.* examples
%python3_sitelibdir/logilab
%python3_sitelibdir/logilab_constraint-%version.dist-info

%changelog
* Thu Jan 04 2024 Anton Vyatkin <toni@altlinux.org> 0.8.0-alt1
- new version 0.8.0

* Thu Dec 28 2023 Anton Vyatkin <toni@altlinux.org> 0.7.1-alt1
- new version 0.7.1

* Wed Apr 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.0-alt1
- Version updated to 0.6.0
- build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5.0-alt2.hg20130911.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt2.hg20130911.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt2.hg20130911.1
- NMU: Use buildreq for BR.

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.hg20130911
- New snapshot

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.hg20120329
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.0-alt1.hg20120329.1
- Rebuild with Python-3.3

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.hg20120329
- Version 0.5.0
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt3.1
- Rebuild with Python-2.7

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3
- Extracted tests into separate package

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Rebuilt with python 2.6

* Fri Oct 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

