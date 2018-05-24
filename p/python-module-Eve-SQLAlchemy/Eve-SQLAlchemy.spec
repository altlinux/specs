%define oname Eve-SQLAlchemy

%def_disable check
%def_with bootstrap

Name: python-module-%oname
Version: 0.3
Release: alt3

Summary: REST API framework powered by Flask, SQLAlchemy and good intentions
License: GPL / BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Eve-SQLAlchemy/
# https://github.com/RedTurtle/eve-sqlalchemy.git
BuildArch: noarch

Source: %name-%version.tar

%py_provides eve_sqlalchemy
%py_requires eve sqlalchemy flask_sqlalchemy

BuildRequires: python-module-pytest

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-pytest


%description
Powered by Eve, SQLAlchemy and good intentions this extenstion allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services with SQL-based backends.

%package -n python3-module-%oname
Summary: REST API framework powered by Flask, SQLAlchemy and good intentions
Group: Development/Python3
%py3_provides eve_sqlalchemy
%add_python3_req_skip flask.ext.sqlalchemy
%if_with bootstrap
%py3_requires eve sqlalchemy flask_sqlalchemy
%endif

%description -n python3-module-%oname
Powered by Eve, SQLAlchemy and good intentions this extenstion allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services with SQL-based backends.

%prep
%setup

cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
python setup.py test

pushd ../python3
python3 setup.py test
popd

%files
%doc AUTHORS CHANGES *.rst docs/*.rst examples
%python_sitelibdir/*

%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst docs/*.rst examples
%python3_sitelibdir/*


%changelog
* Thu May 24 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt3
- rebuild with all requires

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.dev0.git20150127.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.dev0.git20150127.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev0.git20150127
- Version 0.3.dev0

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev0.git20150113
- Initial build for Sisyphus
