%define oname Eve-SQLAlchemy

%def_disable check
%def_with bootstrap

Name: python3-module-%oname
Version: 0.3
Release: alt4

Summary: REST API framework powered by Flask, SQLAlchemy and good intentions
License: GPL / BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Eve-SQLAlchemy/
# https://github.com/RedTurtle/eve-sqlalchemy.git
BuildArch: noarch

Source: %name-%version.tar

%py3_provides eve_sqlalchemy
%add_python3_req_skip flask.ext.sqlalchemy
%if_with bootstrap
%py3_requires eve sqlalchemy flask_sqlalchemy
%endif

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest


%description
Powered by Eve, SQLAlchemy and good intentions this extenstion allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services with SQL-based backends.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc AUTHORS CHANGES *.rst docs/*.rst examples
%python3_sitelibdir/*


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt4
- python2 disabled

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
