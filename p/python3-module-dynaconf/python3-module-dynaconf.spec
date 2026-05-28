%define modname dynaconf

%def_with check

%add_python3_req_skip msvcrt

Name: python3-module-%modname
Version: 3.2.13
Release: alt1

Summary: Configuration Management for Python
License: MIT
Group:   Development/Python3
URL: https://github.com/dynaconf/dynaconf.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-flask
BuildRequires: python3-module-django
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-docker
BuildRequires: python3-module-django-debug-toolbar
BuildRequires: python3-module-redis
BuildRequires: python3-module-configobj
BuildRequires: python3-module-boto3
BuildRequires: python3-module-commentjson
BuildRequires: python3-module-python-dotenv
BuildRequires: python3-module-toml
BuildRequires: python3-module-tox
BuildRequires: python3-module-ipython
BuildRequires: python3-module-ipdb
BuildRequires: python3-module-radon
BuildRequires: python3-module-mypy
BuildRequires: python3-module-ruff
BuildRequires: python3-module-pre-commit
%endif


%description
Configuration Management for Python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest \
    --ignore=tests/test_vault.py \
    --ignore=tests/test_redis.py \
    --ignore=tests_functional/django_pytest \
    --ignore=tests_functional/django_pytest_pure \
    --ignore=tests_functional/pytest_example \
    --ignore=tests_functional/issues/575_603_666_690__envvar_with_template_substitution \
    --ignore=tests_functional/issues/658_nested_envvar_override \
    --ignore=tests_functional/issues/835_926_enable-merge-equal-false \
    --ignore=tests_functional/issues/994_validate_on_update_fix \
    tests/
  
%files
%doc README.* LICENSE MANIFEST.*
%_bindir/*
%python3_sitelibdir/%{pyproject_distinfo %modname}
%python3_sitelibdir/%modname/

%changelog
* Tue May 05 2026 Nikita Panov <nexxy@altlinux.org> 3.2.13-alt1
- Initial build for Sisyphus.

