%define _unpackaged_files_terminate_build 1
%define pypi_name jupyter_server

%def_with check

Name:    python3-module-%pypi_name
Version: 2.9.1
Release: alt1

Summary: The backend -core services, APIs, and REST endpoints-to Jupyter web applications
License: BSD-3-Clause
Group:   Development/Python3
URL: https://pypi.org/project/jupyter-server
VCS: https://github.com/jupyter-server/jupyter_server

BuildArch: noarch

Source0: %pypi_name-%version.tar
Source1: bootstrap.min.css
Source2: bootstrap-theme.min.css

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-jupyter-builder
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-jupyter
BuildRequires: python3-module-nbformat
BuildRequires: python3-module-nbconvert
BuildRequires: python3-module-jupyter-events
BuildRequires: python3-module-prometheus_client
BuildRequires: python3-module-jupyter_client
BuildRequires: python3-module-websocket-client
BuildRequires: python3-module-overrides
BuildRequires: python3-module-anyio
BuildRequires: python3-module-send2trash
BuildRequires: python3-module-pytest-console-scripts
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-traitlets-tests
BuildRequires: python3-module-flaky
BuildRequires: python3-module-argon2-cffi
BuildRequires: /proc
BuildRequires: /dev/pts
%endif

%description
The Jupyter Server provides the backend (i.e. the core services, APIs,
and REST endpoints) for Jupyter web applications like Jupyter notebook,
JupyterLab, and Voila.

%prep
%setup -n %pypi_name-%version
cp %SOURCE1 jupyter_server/static/style/
cp %SOURCE2 jupyter_server/static/style/

sed -i pyproject.toml -e 's/--color=yes//'

%build
%pyproject_build

%install
%pyproject_install

%check
# Cause pytest error.
rm -rf examples/

# test_connection and test_restart_kernel randomly fail
%pyproject_run_pytest -v -W ignore::DeprecationWarning -m 'not network' -k "\
not test_restart_kernel \
and not test_connection"

%files
%doc README.*
%_bindir/*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 25 2023 Anton Vyatkin <toni@altlinux.org> 2.9.1-alt1
- New version 2.9.1.

* Tue Oct 24 2023 Anton Vyatkin <toni@altlinux.org> 2.8.0-alt1
- New version 2.8.0.

* Wed Sep 20 2023 Ivan A. Melnikov <iv@altlinux.org> 2.7.3-alt1.1
- NMU: explicit BR on python3-module-nbconvert
  (fixes build on loongarch64).

* Fri Sep 01 2023 Anton Vyatkin <toni@altlinux.org> 2.7.3-alt1
- New version 2.7.3.

* Fri Aug 18 2023 Anton Vyatkin <toni@altlinux.org> 2.7.2-alt1
- New version 2.7.2.

* Thu Aug 17 2023 Anton Vyatkin <toni@altlinux.org> 2.7.1-alt1
- New version 2.7.1.

* Tue Jun 27 2023 Anton Vyatkin <toni@altlinux.org> 2.7.0-alt1
- New version 2.7.0.

* Fri Jun 02 2023 Anton Vyatkin <toni@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus
