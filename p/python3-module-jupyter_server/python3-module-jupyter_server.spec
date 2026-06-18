%define _unpackaged_files_terminate_build 1
%define pypi_name jupyter_server

%def_with check

Name:    python3-module-%pypi_name
Version: 2.20.0
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
BuildRequires: python3-module-jupyter-server-terminals
BuildRequires: python3-module-requests
BuildRequires: pandoc
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
%pyproject_run_pytest -v -W default -m 'not network' -k "\
not test_restart_kernel \
and not test_connection"

%files
%doc README.*
%_bindir/*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jun 18 2026 Anton Vyatkin <toni@altlinux.org> 2.20.0-alt1
- New version 2.20.0.

* Tue Jun 02 2026 Anton Vyatkin <toni@altlinux.org> 2.19.0-alt1
- New version 2.19.0.

* Wed May 06 2026 Anton Vyatkin <toni@altlinux.org> 2.18.2-alt1
- New version 2.18.2.

* Tue May 05 2026 Anton Vyatkin <toni@altlinux.org> 2.18.0-alt1
- New version 2.18.0.

* Fri Aug 22 2025 Anton Vyatkin <toni@altlinux.org> 2.17.0-alt1
- New version 2.17.0.

* Mon May 12 2025 Anton Vyatkin <toni@altlinux.org> 2.16.0-alt1
- New version 2.16.0.

* Sat Mar 08 2025 Anton Vyatkin <toni@altlinux.org> 2.15.0-alt2
- Fixed FTBFS.

* Fri Dec 20 2024 Anton Vyatkin <toni@altlinux.org> 2.15.0-alt1
- New version 2.15.0.

* Wed Dec 18 2024 Anton Vyatkin <toni@altlinux.org> 2.14.2-alt2
- Fix FTBFS.

* Sat Jul 13 2024 Anton Vyatkin <toni@altlinux.org> 2.14.2-alt1
- New version 2.14.2.

* Sat Jun 01 2024 Anton Vyatkin <toni@altlinux.org> 2.14.1-alt1
- New version 2.14.1.

* Sat Apr 13 2024 Anton Vyatkin <toni@altlinux.org> 2.14.0-alt1
- New version 2.14.0.

* Tue Mar 05 2024 Anton Vyatkin <toni@altlinux.org> 2.13.0-alt1
- New version 2.13.0.

* Fri Jan 19 2024 Anton Vyatkin <toni@altlinux.org> 2.12.5-alt1
- New version 2.12.5.

* Thu Jan 04 2024 Anton Vyatkin <toni@altlinux.org> 2.12.2-alt1
- New version 2.12.2.

* Fri Dec 08 2023 Anton Vyatkin <toni@altlinux.org> 2.12.1-alt1
- New version 2.12.1.

* Wed Dec 06 2023 Anton Vyatkin <toni@altlinux.org> 2.12.0-alt1
- New version 2.12.0.

* Tue Nov 28 2023 Anton Vyatkin <toni@altlinux.org> 2.11.1-alt1
- New version 2.11.1.

* Thu Nov 16 2023 Anton Vyatkin <toni@altlinux.org> 2.10.1-alt1
- New version 2.10.1.

* Tue Nov 07 2023 Anton Vyatkin <toni@altlinux.org> 2.10.0-alt1
- New version 2.10.0.

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
