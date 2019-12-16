%define _unpackaged_files_terminate_build 1
%define oname django-guardian

%def_disable check
%def_disable tests

Name: python3-module-%oname
Version: 2.1.0
Release: alt1

Summary: Implementation of per object permissions for Django 1.2 or later
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-guardian/
BuildArch: noarch

# https://github.com/lukaszb/django-guardian.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage python3-module-django
BuildRequires: python3-module-html5lib python3-module-pbr
BuildRequires: python3-module-pytest python3-module-unittest2
BuildRequires: python3-module-pytest-runner

%py3_provides %oname


%description
django-guardian is implementation of per object permissions as
authorization backend which is supported since Django 1.2. It won't work
with older Django releases.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
django-guardian is implementation of per object permissions as
authorization backend which is supported since Django 1.2. It won't work
with older Django releases.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

install -d %buildroot%python3_sitelibdir/%oname

%check
%__python3 setup.py test
sed -i 's|coverage|coverage3|g' run_test_and_report.sh
./run_test_and_report.sh

%files
%doc AUTHORS CHANGES *.rst
%python3_sitelibdir/guardian
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/guardian/test*
%exclude %python3_sitelibdir/guardian/*/test*

%if_enabled tests
%files -n python3-module-%oname-tests
%python3_sitelibdir/guardian/test*
%python3_sitelibdir/guardian/*/test*
%endif


%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1.0-alt1
- Version updated to 2.1
- build for python2 disabled

* Fri Dec 21 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.9-alt1
- update to 1.4.9

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.4-alt1.git20140714.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.4-alt1.git20140714.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1.git20140714.1
- NMU: Use buildreq for BR.

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.git20140714
- Initial build for Sisyphus

