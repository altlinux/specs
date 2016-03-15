%define oname oslotest

%def_with python3

Name: python-module-%oname
Version: 1.11.0
Release: alt1.1.1
Summary: OpenStack test framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/oslotest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/openstack/oslotest.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests git
#BuildPreReq: python-module-pbr >= 1.6
#BuildPreReq: python-module-fixtures >= 1.3.1 python-module-subunit
#BuildPreReq: python-module-six python-module-testrepository
#BuildPreReq: python-module-testscenarios python-module-testtools
#BuildPreReq: python-module-mock >= 1.2 python-module-mox3
#BuildPreReq: python-module-hacking python-module-coverage
#BuildPreReq: python-module-mimeparse python-module-mccabe
#BuildPreReq: python-module-flake8 pyflakes
#BuildPreReq: python-module-sphinx-devel python-module-oslosphinx
#BuildPreReq: python-module-requests
#BuildPreReq: python-module-os-client-config >= 1.4.0
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pbr >= 1.6
#BuildPreReq: python3-module-fixtures python3-module-subunit
#BuildPreReq: python3-module-six python3-module-testrepository
#BuildPreReq: python3-module-testscenarios python3-module-testtools
#BuildPreReq: python3-module-mock python3-module-mox3
#BuildPreReq: python3-module-hacking python3-module-coverage
#BuildPreReq: python3-module-mimeparse python3-module-mccabe
#BuildPreReq: python3-module-flake8 python3-pyflakes
#BuildPreReq: python3-module-sphinx python3-module-oslosphinx
#BuildPreReq: python3-module-requests
#BuildPreReq: python-module-os-client-config
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-extras python-module-fixtures python-module-flake8 python-module-funcsigs python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pbr python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-subunit python-module-testtools python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-extras python3-module-fixtures python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-linecache2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-ndg-httpsclient python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-subunit python3-module-testtools python3-module-traceback2 python3-module-unittest2 python3-module-yieldfrom.http.client python3-pyflakes python3-tools-pep8 xz
BuildRequires: git-core python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-mock python-module-mox3 python-module-objects.inv python-module-oslosphinx python-module-setuptools-tests python-module-testrepository python3-module-chardet python3-module-coverage python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-mock python3-module-mox3 python3-module-setuptools-tests python3-module-sphinx python3-module-testrepository python3-module-urllib3 python3-module-yieldfrom.urllib3 rpm-build-python3 time

%description
OpenStack test framework and test fixtures.

%package -n python3-module-%oname
Summary: OpenStack test framework
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
OpenStack test framework and test fixtures.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
OpenStack test framework and test fixtures.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
OpenStack test framework and test fixtures.

This package contains documentation for %oname.

%prep
%setup
# let RPM handle deps
rm -rf {test-,}requirements.txt

git init-db
git config user.email "real at altlinux.org"
git config user.name "REAL"
git add . -A
git commit -a -m "commit"
git tag %version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	sed -i 's|python|python3|g' $i
	sed -i 's|python33|python3|g' $i
	sed -i 's|tox|tox.py3|g' $i
	mv $i $i.py3
done
popd
mv %buildroot%python3_sitelibdir/%oname-*-py%_python3_version.egg-info \
	%buildroot%python3_sitelibdir/%oname-py%_python3_version.egg-info
%endif

%python_install
mv %buildroot%python_sitelibdir/%oname-*-py%_python_version.egg-info \
	%buildroot%python_sitelibdir/%oname-py%_python_version.egg-info

export PYTHONPATH=$PWD
pushd doc
sphinx-build -b pickle -d build/doctrees source build/pickle
sphinx-build -b html -d build/doctrees source build/html
popd

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.11.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Fri May 15 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20141105
- Initial build for Sisyphus

