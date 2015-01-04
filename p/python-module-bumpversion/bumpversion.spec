%define oname bumpversion

%def_with python3

Name: python-module-%oname
Version: 0.5.1
Release: alt1.dev.git20141228
Summary: Version-bump your software with a single command!
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bumpversion/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/peritus/bumpversion.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
A small command line tool to simplify releasing software by updating all
version strings in your source code by the correct increment. Also
creates commits and tags:

* version formats are highly configurable
* works without any VCS, but happily reads tag information from and
  writes commits and tags to Git and Mercurial if available
* just handles text files, so it's not specific to any programming
  language

%package -n python3-module-%oname
Summary: Version-bump your software with a single command!
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A small command line tool to simplify releasing software by updating all
version strings in your source code by the correct increment. Also
creates commits and tags:

* version formats are highly configurable
* works without any VCS, but happily reads tag information from and
  writes commits and tags to Git and Mercurial if available
* just handles text files, so it's not specific to any programming
  language

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|@PY3@|.py3|g' ../python3/tests.py
%endif

sed -i 's|@PY3@||g' tests.py

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
	mv $i $i.py3
done
popd
%endif

%python_install

%check
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=$PWD
export LC_ALL=en_US.UTF-8
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.dev.git20141228
- Initial build for Sisyphus

