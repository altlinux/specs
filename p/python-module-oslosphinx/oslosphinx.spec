%define oname oslosphinx

%def_with python3

Name: python-module-%oname
Version: 3.2.0
Release: alt1.1
Summary: OpenStack Sphinx Extensions and Theme
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/oslosphinx/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/openstack/oslosphinx.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: git
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pbr >= 1.6 python-module-sphinx-devel
#BuildPreReq: python-module-hacking python-module-mccabe
#BuildPreReq: python-module-flake8 pyflakes
#BuildPreReq: python-module-requests >= 2.5.2

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pbr python3-module-sphinx
#BuildPreReq: python3-module-hacking python3-module-mccabe
#BuildPreReq: python3-module-flake8 python3-pyflakes
#BuildPreReq: python3-module-requests
%endif

%py_provides %oname
%py_requires hacking

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-flake8 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-ndg-httpsclient python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx_rtd_theme python3-module-urllib3 python3-pyflakes python3-tools-pep8 xz
BuildRequires: git-core python-module-alabaster python-module-docutils python-module-hacking python-module-html5lib python-module-objects.inv python-module-requests python-module-setuptools-tests python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-requests python3-module-setuptools-tests python3-module-sphinx rpm-build-python3 time

%description
Theme and extension support for Sphinx documentation from the OpenStack
project.

%package -n python3-module-%oname
Summary: OpenStack Sphinx Extensions and Theme
Group: Development/Python3
%py3_provides %oname
%py3_requires hacking

%description -n python3-module-%oname
Theme and extension support for Sphinx documentation from the OpenStack
project.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Theme and extension support for Sphinx documentation from the OpenStack
project.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Theme and extension support for Sphinx documentation from the OpenStack
project.

This package contains documentation for %oname.

%prep
%setup

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
%python_install
mv %buildroot%python_sitelibdir/%oname-*-py%_python_version.egg-info \
	%buildroot%python_sitelibdir/%oname-py%_python_version.egg-info

%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%python3_sitelibdir/%oname-*-py%_python3_version.egg-info \
	%buildroot%python3_sitelibdir/%oname-py%_python3_version.egg-info
%endif

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
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.2.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1
- Version 3.0.0

* Fri May 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.git20141011
- Added necessary requirements
- Enabled testing

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20141011
- Initial build for Sisyphus

