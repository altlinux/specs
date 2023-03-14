%define _unpackaged_files_terminate_build 1
%define oname flask_restx

%def_enable check

Name: python3-module-flask-restx
Version: 1.1.0
Release: alt1

Summary: Flask-RESTX is a community driven fork of Flask-RESTPlus
License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/python-restx/flask-restx

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-flask
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-pytz
BuildRequires: python3-module-aniso8601

%if_enabled check
BuildRequires: /dev/pts
BuildRequires: python3-module-tox
BuildRequires: python3-module-faker
BuildRequires: python3-module-blinker
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-flask
%endif

BuildArch: noarch

Source0: %name-%version.tar
Source1: node_modules.tar.gz
Patch0: %name-%version-%release.patch

%description
Flask-RESTX is an extension for Flask that adds support for quickly building 
REST APIs. Flask-RESTX encourages best practices with minimal setup. If you 
are familiar with Flask, Flask-RESTX should be easy to pick up. It provides 
a coherent collection of decorators and tools to describe your API and expose 
its documentation properly using Swagger.


%prep
%setup -a 1
%autopatch -p1

%build
# copy swaggerui code from npm modules
mkdir -p flask_restx/static
cp node_modules/swagger-ui-dist/{swagger-ui*.{css,js}{,.map},favicon*.png,oauth2-redirect.html} \
	flask_restx/static
cp node_modules/typeface-droid-sans/index.css flask_restx/static/droid-sans.css
cp -R node_modules/typeface-droid-sans/files flask_restx/static/
%pyproject_build

%install
%pyproject_install

%check
# override upstream tox.ini
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs}
EOF

# excluded: DNS resolution related tests
EXCLUDE_TESTS_CONDITION="not (\
  (URLTest and test_check) or \
  (EmailTest and test_valid_value_check)\
)"

%tox_check_pyproject -- -vra --ignore=tests/benchmarks -k "$EXCLUDE_TESTS_CONDITION"

%files
%doc LICENSE README.rst CHANGELOG.rst CONTRIBUTING.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Mon Mar 13 2023 Danil Shein <dshein@altlinux.org> 1.1.0-alt1
- new version 1.1.0
  + update SwaggerUI

* Wed Nov 30 2022 Danil Shein <dshein@altlinux.org> 1.0.3-alt1
- new version 1.0.3
  + update SwaggerUI
  + clean-up spec

* Tue Sep 20 2022 Danil Shein <dshein@altlinux.org> 0.5.1-alt4
- fix Werkzeug 2.2.x compatibility
  + merge upstream dev branch (git a017c3c) 
  + migrate to pyproject macroses
  + update SwaggerUI
  + get rid of patches that excludes particular tests

* Tue Apr 12 2022 Danil Shein <dshein@altlinux.org> 0.5.1-alt3
- update SwaggerUI

* Fri Mar 04 2022 Danil Shein <dshein@altlinux.org> 0.5.1-alt2
- enable tests

* Tue Sep 07 2021 Danil Shein <dshein@altlinux.org> 0.5.1-alt1
- new version 0.5.1

* Thu Jul 01 2021 Danil Shein <dshein@altlinux.org> 0.4.0-alt1
- initial build for ALT
- without tests

