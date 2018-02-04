%define oname pyScss

%def_with python3

Name: python-module-%oname
Version: 1.3.5
Release: alt1.1
Summary: pyScss, a Scss compiler for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyScss/

# https://github.com/Kronuz/pyScss.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: libpcre-devel python-module-Pillow python-module-alabaster python-module-docutils python-module-enum34 python-module-html5lib python-module-objects.inv python-module-pathlib python-module-pytest-cov python-module-setuptools time
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-Pillow python3-module-enum34 python3-module-pathlib python3-module-pytest-cov python3-module-setuptools python3-module-six
%endif

%py_provides %oname scss
%py_requires six pathlib logging PIL

%description
pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.

%package -n python3-module-%oname
Summary: pyScss, a Scss compiler for Python
Group: Development/Python3
%py3_provides %oname scss
%py3_requires six pathlib logging PIL

%description -n python3-module-%oname
pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -I%_includedir/pcre -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%add_optflags -I%_includedir/pcre -fno-strict-aliasing
%if_with python3
pushd ../python3
%python3_install
install -p -m644 scss/grammar/*.g \
	%buildroot%python3_sitelibdir/scss/grammar/
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
install -p -m644 scss/grammar/*.g \
	%buildroot%python_sitelibdir/scss/grammar/

CFLAGS="%optflags" python setup.py build_ext -i
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test -vv --cov scss
%if_with python3
pushd ../python3
py.test3 -vv --cov scss
popd
%endif

%files
%doc DESCRIPTION *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc DESCRIPTION *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt1
- Updated to upstream release version 1.3.5.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.4-alt1.git20150122.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.4-alt1.git20150122.1
- NMU: Use buildreq for BR.

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20150122
- Initial build for Sisyphus

