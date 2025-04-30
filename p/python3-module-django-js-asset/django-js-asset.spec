%define _unpackaged_files_terminate_build 1

%define modname django-js-asset

%def_with check

Name: python3-module-%modname
Version: 3.1.2
Release: alt1

Summary: script tag with additional attributes for django.forms.Media
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/django-js-asset/
VCS: https://github.com/matthiask/django-js-asset.git
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(coverage)
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
django-js-asset -- script tag with additional attributes for django.forms.Media

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
export DJANGO_SETTINGS_MODULE=tests.testapp.settings
export TOX_TESTENV_PASSENV='DJANGO_SETTINGS_MODULE'
%tox_check_pyproject

%files
%doc LICENSE README.*
%python3_sitelibdir/*


%changelog
* Tue Apr 29 2025 Dmitry Lyalyaev <fruktime@altlinux.org> 3.1.2-alt1
- 1.2.2 -> 3.1.2

* Tue Jul 13 2021 Alexey Shabalin <shaba@altlinux.org> 1.2.2-alt1
- Build python3 only package.

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt1
- Initial build for Sisyphus
