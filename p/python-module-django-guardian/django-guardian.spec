%define oname django-guardian

%def_with python3
%def_disable check
%def_disable tests

Name: python-module-%oname
Version: 1.4.9
Release: alt1
Summary: Implementation of per object permissions for Django 1.2 or later
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-guardian/

# https://github.com/lukaszb/django-guardian.git
Source: %oname-%version.tar
Patch0: %name-%version-%release.patch
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-django-tests python-module-mock
#BuildPreReq: python-module-six
#BuildPreReq: python-module-coverage
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-django-dbbackend-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-django-tests python3-module-mock
#BuildPreReq: python3-module-six
#BuildPreReq: python3-module-coverage
#BuildPreReq: python3-module-django-dbbackend-sqlite3
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-django python-module-funcsigs python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-markupsafe python-module-pbr python-module-psycopg2 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-traceback2 python-module-unittest2 python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-psycopg2 python3-module-pycparser python3-module-setuptools python3-module-yaml tzdata
BuildRequires: python-module-alabaster python-module-coverage python-module-django-dbbackend-sqlite3 python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-pytest python3-module-coverage python3-module-django python3-module-html5lib python3-module-pbr python3-module-pytest python3-module-unittest2 rpm-build-python3 time

%description
django-guardian is implementation of per object permissions as
authorization backend which is supported since Django 1.2. It won't work
with older Django releases.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
django-guardian is implementation of per object permissions as
authorization backend which is supported since Django 1.2. It won't work
with older Django releases.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Implementation of per object permissions for Django 1.2 or later
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
django-guardian is implementation of per object permissions as
authorization backend which is supported since Django 1.2. It won't work
with older Django releases.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
django-guardian is implementation of per object permissions as
authorization backend which is supported since Django 1.2. It won't work
with older Django releases.

This package contains tests for %oname.

%prep
%setup -n django-guardian-%version
%patch0 -p1

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

install -d %buildroot%python_sitelibdir/%oname

%check
python setup.py test
./run_test_and_report.sh
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|coverage|coverage3|g' run_test_and_report.sh
./run_test_and_report.sh
popd
%endif

%files
%doc AUTHORS CHANGES *.rst
%python_sitelibdir/guardian
%python_sitelibdir/*.egg-info
%dir %python_sitelibdir/%oname
%exclude %python_sitelibdir/guardian/test*

%if_enabled tests
%files tests
%python_sitelibdir/guardian/test*
%endif

%if_with python3
%files -n python3-module-%oname
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
%endif

%changelog
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

