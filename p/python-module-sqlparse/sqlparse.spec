%define oname sqlparse

%def_with python3

Name: python-module-%oname
Version: 0.1.12
Release: alt1.git20140920
Summary: Non-validating SQL parser
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlparse/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/andialbrecht/sqlparse.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

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
%setup

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
%doc AUTHORS CHANGES *.rst TODO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/build/html
%_man1dir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst TODO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.12-alt1.git20140920
- Initial build for Sisyphus

