%define oname Flask

Name: python3-module-flask
Version: 1.1.2
Release: alt1

Summary: A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
License: BSD
Group: Development/Python3

URL: http://flask.pocoo.org/
BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-simplejson
BuildRequires: python3-module-jinja2

# /usr/bin/flask
Obsoletes: python-module-flask
Provides: python-module-flask

%py3_requires click.testing

%description
Flask is called a "micro-framework" because the idea to keep the core
simple but extensible. There is no database abstraction layer, no form
validation or anything else where different libraries already exist that
can handle that.  However Flask knows the concept of extensions that can
add this functionality into your application as if it was implemented in
Flask itself. There are currently extensions for object relational
mappers, form validation, upload handling, various open authentication
technologies and more.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
#pytest3

%files
%doc README.rst LICENSE.rst
%_bindir/flask
%python3_sitelibdir/flask/
%python3_sitelibdir/%oname-*.egg-info

%changelog
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

