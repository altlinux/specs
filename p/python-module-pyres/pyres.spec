%define oname pyres

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.5
Release: alt1.git20140901
Summary: Python resque clone
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyres/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/binarydud/pyres.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-simplejson
BuildPreReq: python-module-redis-py python-module-setproctitle
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-simplejson
BuildPreReq: python3-module-redis-py python3-module-setproctitle
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Resque is a great implementation of a job queue by the people at github.
It's written in ruby, which is great, but I primarily work in python. So
I took on the task of porting over the code to python and PyRes was the
result.

%package -n python3-module-%oname
Summary: Python resque clone
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Resque is a great implementation of a job queue by the people at github.
It's written in ruby, which is great, but I primarily work in python. So
I took on the task of porting over the code to python and PyRes was the
result.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Resque is a great implementation of a job queue by the people at github.
It's written in ruby, which is great, but I primarily work in python. So
I took on the task of porting over the code to python and PyRes was the
result.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Resque is a great implementation of a job queue by the people at github.
It's written in ruby, which is great, but I primarily work in python. So
I took on the task of porting over the code to python and PyRes was the
result.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%if_disabled check
rm -f requirements*
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
rm -f requirements*

%files
%doc *.md *.txt *.markdown
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.txt *.markdown
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20140901
- Initial build for Sisyphus

