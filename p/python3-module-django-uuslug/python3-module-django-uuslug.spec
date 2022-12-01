%define _unpackaged_files_terminate_build 1
%define pypi_name django-uuslug
%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1
Summary: A Django slugify application that also handles Unicode
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/django-uuslug/
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(slugify)
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%py3_provides %pypi_name

%description
A Django slugify application that guarantees Uniqueness and handles Unicode

%prep
%setup

%build
%pyproject_build

%if_with check
%check
cat > tox.ini <<EOF
[testenv]
commands =
    python3 manage.py test
EOF
%tox_check_pyproject
%endif

%install
%pyproject_install

%files
%python3_sitelibdir/uuslug
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 30 2022 Alexander Makeenkov <amakeenk@altlinux.org> 2.0.0-alt1
- Initial build for ALT

