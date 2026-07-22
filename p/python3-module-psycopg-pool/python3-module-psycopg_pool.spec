%define _unpackaged_files_terminate_build 1
%define oname psycopg_pool

%def_enable check

Name: python3-module-psycopg-pool
Version: 3.3.1
Release: alt1

Summary: PostgreSQL database adapter for Python
License: LGPL-3.0-only
Group: Development/Python3
Url: https://github.com/psycopg/psycopg.git

Source0: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: postgresql-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
This distribution package is an optional component of Psycopg 3: it 
contains the optional connection pool package psycopg_pool.

%prep
%setup -q -n %{oname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info


%changelog
* Thu Jul 09 2026 Nikita Panov <nexxy@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus.
