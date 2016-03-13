%define oname Eve-SQLAlchemy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3
Release: alt1.dev0.git20150127.1.1
Summary: REST API framework powered by Flask, SQLAlchemy and good intentions
License: GPL / BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Eve-SQLAlchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/eve-sqlalchemy.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-eve-tests python-module-SQLAlchemy
#BuildPreReq: python-module-flask_sqlalchemy python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-eve-tests python3-module-SQLAlchemy
#BuildPreReq: python3-module-flask_sqlalchemy python3-modules-sqlite3
%endif

%py_provides eve_sqlalchemy
%py_requires eve sqlalchemy flask_sqlalchemy

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-jinja2 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-jinja2 python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
Powered by Eve, SQLAlchemy and good intentions this extenstion allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services with SQL-based backends.

%package -n python3-module-%oname
Summary: REST API framework powered by Flask, SQLAlchemy and good intentions
Group: Development/Python3
%py3_provides eve_sqlalchemy
%py3_requires eve sqlalchemy flask_sqlalchemy

%description -n python3-module-%oname
Powered by Eve, SQLAlchemy and good intentions this extenstion allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services with SQL-based backends.

%prep
%setup

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS CHANGES *.rst docs/*.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst docs/*.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.dev0.git20150127.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.dev0.git20150127.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev0.git20150127
- Version 0.3.dev0

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev0.git20150113
- Initial build for Sisyphus

