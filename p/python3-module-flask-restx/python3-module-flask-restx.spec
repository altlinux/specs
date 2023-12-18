%define _unpackaged_files_terminate_build 1
%define pypi_name flask-restx
%define mod_name flask_restx

%def_enable check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Flask-RESTX is a community driven fork of Flask-RESTPlus
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/flask-restx/
Vcs: https://github.com/python-restx/flask-restx

BuildArch: noarch

Source0: %name-%version.tar
Source1: node_modules.tar.gz
Source2: %pyproject_deps_config_name
Patch0: %name-%version-%release.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_enabled check
%add_pyproject_deps_check_filter pytest-profiling
%pyproject_builddeps_metadata_extra test
%endif

%description
Flask-RESTX is an extension for Flask that adds support for quickly building
REST APIs. Flask-RESTX encourages best practices with minimal setup. If you
are familiar with Flask, Flask-RESTX should be easy to pick up. It provides
a coherent collection of decorators and tools to describe your API and expose
its documentation properly using Swagger.

%prep
%setup -a 1
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
# excluded: DNS resolution related tests
EXCLUDE_TESTS_CONDITION="not (\
  (URLTest and test_check) or \
  (EmailTest and test_valid_value_check)\
)"

%pyproject_run_pytest -vra --ignore=tests/benchmarks -k "$EXCLUDE_TESTS_CONDITION"

%files
%doc LICENSE README.rst CHANGELOG.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%mod_name-%version.dist-info/

%changelog
* Wed Dec 13 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

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

