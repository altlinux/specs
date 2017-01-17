%define _unpackaged_files_terminate_build 1
%define oname sqlparse

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1
Summary: Non-validating SQL parser
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlparse/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/andialbrecht/sqlparse.git
Source0: https://pypi.python.org/packages/55/ce/3944e990b03f80f36f0050b407ad46cde192a210d473f0d705b554bddd1d/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

%description
sqlparse is a non-validating SQL parser module. It provides support for
parsing, splitting and formatting SQL statements.

%package -n python3-module-%oname
Summary: Non-validating SQL parser
Group: Development/Python3

%description -n python3-module-%oname
sqlparse is a non-validating SQL parser module. It provides support for
parsing, splitting and formatting SQL statements.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
sqlparse is a non-validating SQL parser module. It provides support for
parsing, splitting and formatting SQL statements.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
sqlparse is a non-validating SQL parser module. It provides support for
parsing, splitting and formatting SQL statements.

This package contains documentation for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

install -d %buildroot%_man1dir
install -p -m644 docs/*.1 %buildroot%_man1dir/

%files
%doc AUTHORS *.rst TODO CHANGELOG PKG-INFO docs
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html
%_man1dir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst TODO CHANGELOG PKG-INFO docs
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.12-alt1.git20140920.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.12-alt1.git20140920.1
- NMU: Use buildreq for BR.

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.12-alt1.git20140920
- Initial build for Sisyphus

