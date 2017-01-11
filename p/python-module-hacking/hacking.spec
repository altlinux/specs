%define _unpackaged_files_terminate_build 1
%define oname hacking

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 0.13.0
Release: alt1
Summary: OpenStack Hacking Guideline Enforcement
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/hacking/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/openstack-dev/hacking.git
Source0: https://pypi.python.org/packages/b6/be/67678ca6d422e99ff39a054a62403dcb1f8b95666de392dd8354d828acfb/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: git
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pbr python-tools-pep8 pyflakes
#BuildPreReq: python-module-flake8 python-module-mccabe
#BuildPreReq: python-module-six python-module-coverage
#BuildPreReq: python-module-discover python-module-fixtures
#BuildPreReq: python-module-mock python-module-subunit
#BuildPreReq: python-module-sphinx python-module-oslosphinx
#BuildPreReq: python-module-testrepository python-module-testscenarios
#BuildPreReq: python-module-testtools python-module-mimeparse
#BuildPreReq: python-module-eventlet
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pbr python3-tools-pep8 python3-pyflakes
#BuildPreReq: python3-module-flake8 python3-module-mccabe
#BuildPreReq: python3-module-six python3-module-coverage
#BuildPreReq: python3-module-discover python3-module-fixtures
#BuildPreReq: python3-module-mock python3-module-subunit
#BuildPreReq: python3-module-sphinx python3-module-oslosphinx
#BuildPreReq: python3-module-testrepository python3-module-testscenarios
#BuildPreReq: python3-module-testtools python3-module-mimeparse
#BuildPreReq: python3-module-eventlet python3-module-requests
%endif

%py_provides %oname
%py_requires mccabe flake8

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-dns python-module-enum34 python-module-extras python-module-fixtures python-module-flake8 python-module-genshi python-module-greenlet python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pbr python-module-psycopg2 python-module-pyasn1 python-module-pytest python-module-pytz python-module-requests python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-subunit python-module-testscenarios python-module-testtools python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-discover python3-module-dns python3-module-docutils python3-module-enum34 python3-module-extras python3-module-fixtures python3-module-flake8 python3-module-genshi python3-module-greenlet python3-module-hacking python3-module-jinja2 python3-module-linecache2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-ndg-httpsclient python3-module-ntlm python3-module-pbr python3-module-pip python3-module-psycopg2 python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-requests python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx_rtd_theme python3-module-subunit python3-module-testscenarios python3-module-testtools python3-module-traceback2 python3-module-unittest2 python3-module-urllib3 python3-module-yieldfrom.http.client python3-pyflakes python3-tools-pep8
BuildRequires: git-core python-module-coverage python-module-discover python-module-docutils python-module-eventlet python-module-html5lib python-module-mock python-module-oslosphinx python-module-setuptools-tests python-module-testrepository python3-module-coverage python3-module-eventlet python3-module-html5lib python3-module-jinja2-tests python3-module-mock python3-module-oslosphinx python3-module-setuptools-tests python3-module-sphinx python3-module-testrepository python3-module-yieldfrom.urllib3 rpm-build-python3

%description
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack Hacking Guideline Enforcement
Group: Development/Python3
%py3_provides %oname
%py3_requires mccabe flake8

%description -n python3-module-%oname
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

git init-db
git config user.email "real at altlinux.org"
git config user.name "REAL"
git add . -A
git commit -a -m "commit"
git tag %version

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
mv %buildroot%python_sitelibdir/hacking-*-py%_python_version.egg-info \
	%buildroot%python_sitelibdir/hacking-py%_python_version.egg-info

%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%python3_sitelibdir/hacking-*-py%_python3_version.egg-info \
	%buildroot%python3_sitelibdir/hacking-py%_python3_version.egg-info
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst doc/source/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/source/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.2-alt3.git20150723.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.2-alt3.git20150723.1
- NMU: Use buildreq for BR.

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt3.git20150723
- Added necessary requirements

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt2.git20150723
- Enabled check

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20150723
- Version 0.10.2
- Disabled check (for bootstrap)

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20141105
- Initial build for Sisyphus

