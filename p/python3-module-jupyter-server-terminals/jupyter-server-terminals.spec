%define pypi_name jupyter-server-terminals
%define mod_name jupyter_server_terminals

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: A Jupyter Server Extension Providing Support for Terminals
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/jupyter-server-terminals/
VCS: https://github.com/jupyter-server/jupyter_server_terminals

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-pytest-jupyter
BuildRequires: python3-module-jupyter_server
BuildRequires: /dev/pts
%endif

%description
%summary.

%prep
%setup
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

# Move config file to proper location
install -d -m 755 %buildroot%_sysconfdir/jupyter/jupyter_server_config.d
mv %buildroot/usr/etc/jupyter/jupyter_server_config.d/*.json \
   %buildroot%_sysconfdir/jupyter/jupyter_server_config.d

%check
%pyproject_run_pytest -v -W ignore::ImportWarning -W ignore::DeprecationWarning

%files
%doc README.*
%dir %_sysconfdir/jupyter/
%dir %_sysconfdir/jupyter/jupyter_server_config.d/
%_sysconfdir/jupyter/jupyter_server_config.d/*
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Dec 12 2023 Anton Vyatkin <toni@altlinux.org> 0.5.0-alt1
- New version 0.5.0.

* Mon Jul 17 2023 Anton Vyatkin <toni@altlinux.org> 0.4.4-alt2
- Fix FTBFS.

* Wed Jun 14 2023 Anton Vyatkin <toni@altlinux.org> 0.4.4-alt1
- Initial build for Sisyphus
