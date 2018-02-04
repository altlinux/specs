%define oname pyres

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.5
Release: alt2.git20140901.1
Summary: Python resque clone
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pyres/

# https://github.com/binarydud/pyres.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose python-module-simplejson
BuildRequires: python-module-redis-py python-module-setproctitle
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-simplejson
BuildRequires: python3-module-redis-py python3-module-setproctitle
BuildRequires: python-tools-2to3
%endif

%py_provides %oname
%py_requires redis

%description
Resque is a great implementation of a job queue by the people at github.
It's written in ruby, which is great, but I primarily work in python. So
I took on the task of porting over the code to python and PyRes was the
result.

%if_with python3
%package -n python3-module-%oname
Summary: Python resque clone
Group: Development/Python3
%py3_provides %oname
%py3_requires redis

%description -n python3-module-%oname
Resque is a great implementation of a job queue by the people at github.
It's written in ruby, which is great, but I primarily work in python. So
I took on the task of porting over the code to python and PyRes was the
result.
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md *.markdown LICENSE CHANGES.txt
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
%doc *.md *.markdown LICENSE CHANGES.txt
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5-alt2.git20140901.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5-alt2.git20140901
- Updated runtime dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20140901.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5-alt1.git20140901.1
- NMU: Use buildreq for BR.

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20140901
- Initial build for Sisyphus

