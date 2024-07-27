%def_without check

Name: awx
Version: 24.6.1
Release: alt1

Summary: The official command line interface for Ansible AWX
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/ansible/awx

BuildArch: noarch

Source: %name-%version.tar
Patch0: reimplementation_of_strtobool_function.patch
Patch1: replace_distutils_version.patch
Patch2: awx-disable-aioredis.patch
Patch3: awx-disable-asciichartpy.patch

Requires: python3-module-logutils
Requires: python3-module-colorama
Requires: python3-module-django-extensions
Requires: python3-module-django-cors-headers
Requires: python3-module-django-debug-toolbar
Requires: python3-module-django-dbbackend-sqlite3
Requires: python3-module-python-tss-sdk

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%add_python3_req_skip defaults development

%description
AWX provides a web-based user interface, REST API, and task engine built on top
of Ansible. It is one of the upstream projects for Red Hat Ansible Automation Platform.

%prep
%setup
%autopatch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%_bindir/awx-manage
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%exclude %python3_sitelibdir/%name/conf/tests
%exclude %python3_sitelibdir/%name/sso/tests

%changelog
* Sun Jul 21 2024 Anton Vyatkin <toni@altlinux.org> 24.6.1-alt1
- Initial build for Sisyphus.
