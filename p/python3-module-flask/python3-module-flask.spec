%define _unpackaged_files_terminate_build 1
%define oname Flask

%def_enable check

Name: python3-module-flask
Version: 2.0.3
Release: alt1

Summary: Flask is a lightweight WSGI web application framework.
License: BSD-3-Clause
Group: Development/Python3
URL: https://palletsprojects.com/p/flask/
VCS:  https://github.com/pallets/flask

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-werkzeug >= 2.0
BuildRequires: python3-module-itsdangerous
BuildRequires: python3-module-click
%if_enabled check
BuildRequires: pytest3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tox
BuildRequires: python3-module-tox-no-deps
BuildRequires: python3-module-tox-console-scripts
%endif

# /usr/bin/flask
Obsoletes: python-module-flask
Conflicts: python-module-flask

BuildArch: noarch

Source0: %name-%version.tar

%description
Flask is a lightweight WSGI web application framework. It is designed to 
make getting started quick and easy, with the ability to scale up to complex 
applications. It began as a simple wrapper around Werkzeug and Jinja and 
has become one of the most popular Python web application frameworks.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir/
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -- -vra

%files
%doc *.rst
%_bindir/flask
%python3_sitelibdir/flask/
%python3_sitelibdir/%oname-*.egg-info

%changelog
* Thu Mar 03 2022 Danil Shein <dshein@altlinux.org> 2.0.3-alt1
- new version 1.1.2 -> 2.0.3
  + enable tests

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt2
- set Conflicts to python2 module instead of Provides

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- new version 1.1.2 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- build python3 package separately

* Fri Aug 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.1-alt1
- Version updated to 1.1.1

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.0.2-alt1
- 1.0.2

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.12.2-alt4
- Updated runtime dependencies.

* Wed Mar 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.12.2-alt3
- Fixed spec.

* Wed Mar 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.12.2-alt2
- Fixed spec.

* Wed Mar 07 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.12.2-alt1
- Version 0.12.2

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Version 0.10.1
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2.1
- Fixed build

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt2
- Don't package testsuite.

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt1
- Initial build for Sisyphus.

