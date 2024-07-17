%define pypi_name jupyterlab-server
%define mod_name jupyterlab_server

%def_with check

Name: python3-module-%pypi_name
Version: 2.27.3
Release: alt1
Summary: A set of server components for JupyterLab and JupyterLab like applications
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/jupyterlab-server/
VCS: https://github.com/jupyterlab/jupyterlab_server
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jupyter_server
BuildRequires: python3-module-json5
BuildRequires: python3-module-babel
BuildRequires: python3-module-pytest-jupyter
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-requests-mock
BuildRequires: python3-module-mistune
BuildRequires: python3-module-strict-rfc3339
BuildRequires: python3-module-openapi-core
BuildRequires: /dev/pts
BuildRequires: python3-module-ruamel-yaml
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pip
%endif

%description
JupyterLab Server sits between JupyterLab and Jupyter Server, and provides
a set of REST API handlers and utilities that are used by JupyterLab.
It is a separate project in order to accommodate creating JupyterLab-like
applications from a more limited scope.

%prep
%setup
sed -i 's/--color=yes//' pyproject.toml
sed -i 's/--doctest-modules//' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
for p in \
  tests/translations/jupyterlab-some-package \
  tests/translations/jupyterlab-language-pack-es_CO
do
  %__python3 -m pip install --use-pep517 --no-build-isolation --disable-pip-version-check $p
done
%pyproject_run_pytest -v -W ignore::DeprecationWarning

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Wed Jul 17 2024 Anton Vyatkin <toni@altlinux.org> 2.27.3-alt1
- New version 2.27.3.

* Wed May 22 2024 Anton Vyatkin <toni@altlinux.org> 2.27.2-alt1
- New version 2.27.2.

* Wed Apr 24 2024 Anton Vyatkin <toni@altlinux.org> 2.27.1-alt1
- New version 2.27.1.

* Tue Apr 23 2024 Anton Vyatkin <toni@altlinux.org> 2.27.0-alt1
- New version 2.27.0.

* Tue Apr 09 2024 Anton Vyatkin <toni@altlinux.org> 2.26.0-alt1
- New version 2.26.0.

* Tue Mar 12 2024 Anton Vyatkin <toni@altlinux.org> 2.25.4-alt1
- New version 2.25.4.

* Thu Feb 15 2024 Anton Vyatkin <toni@altlinux.org> 2.25.3-alt1
- New version 2.25.3.

* Mon Jan 22 2024 Anton Vyatkin <toni@altlinux.org> 2.25.2-alt2
- Fixed FTBFS.

* Tue Nov 28 2023 Anton Vyatkin <toni@altlinux.org> 2.25.2-alt1
- New version 2.25.2.

* Thu Nov 09 2023 Anton Vyatkin <toni@altlinux.org> 2.25.1-alt1
- New version 2.25.1.

* Wed Sep 13 2023 Anton Vyatkin <toni@altlinux.org> 2.25.0-alt1
- New version 2.25.0.

* Mon Jul 24 2023 Anton Vyatkin <toni@altlinux.org> 2.24.0-alt1
- New version 2.24.0.

* Mon Jul 17 2023 Anton Vyatkin <toni@altlinux.org> 2.23.0-alt2
- Fix FTBFS.

* Fri Jun 16 2023 Anton Vyatkin <toni@altlinux.org> 2.23.0-alt1
- Initial build for Sisyphus
