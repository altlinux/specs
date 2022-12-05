%define pypi_name kobo
%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-%pypi_name
Version: 0.25.0
Release: alt1
Summary: A collection of Python utilities
License: LGPLv2.1 
Group: Development/Python3
Url: https://pypi.org/project/kobo/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%py3_provides %pypi_name

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(requests-gssapi)
BuildRequires: python3(django)
BuildRequires: python3(mock)
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: mailcap
BuildRequires: coreutils
%endif

%description 
A pile of python modules used by Red Hat release engineering
to build their tools.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export DJANGO_SETTINGS_MODULE=tests.settings                                     
export TOX_TESTENV_PASSENV='DJANGO_SETTINGS_MODULE'
%tox_check_pyproject

%files 
%_bindir/kobo-admin
%python3_sitelibdir/kobo/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 30 2022 Mikhail Chernonog <snowmix@altlinux.org> 0.25.0-alt1
- Initial build for Sisyphus
