%define oname sqlcmd

%def_with python3

Name: python-module-%oname
Version: 0.7.1
Release: alt1.git20110314.1
Summary: A cross-platform, cross-database SQL command line tool
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlcmd
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bmc/sqlcmd.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-grizzled python-module-enum
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-grizzled python3-module-enum
%endif

%py_provides %oname
%py_requires grizzled enum

%description
sqlcmd is a SQL command line tool, similar in concept to tools like
Oracle's SQL*Plus, the PostgreSQL psql command, and MySQL's mysql tool.

%if_with python3
%package -n python3-module-%oname
Summary: A cross-platform, cross-database SQL command line tool
Group: Development/Python3
%py3_provides %oname
%py3_requires grizzled enum

%description -n python3-module-%oname
sqlcmd is a SQL command line tool, similar in concept to tools like
Oracle's SQL*Plus, the PostgreSQL psql command, and MySQL's mysql tool.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
iconv -f latin1 -tUTF-8 ../python3/sqlcmd/__init__.py \
	> ../python3/sqlcmd/__init__.py.u
mv -f ../python3/sqlcmd/__init__.py.u ../python3/sqlcmd/__init__.py
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
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
export LC_ALL=en_US.UTF-8
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc CHANGELOG *.md TO-DO doc
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md TO-DO doc
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1.git20110314.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20110314
- Initial build for Sisyphus

