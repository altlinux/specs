%define _unpackaged_files_terminate_build 1

%define oname jupyterlab_pygments

Name: python3-module-%oname
Version: 0.3.0
Release: alt1
Summary: Pygments theme using JupyterLab CSS variables
License: BSD-3-Clause and MIT and Python
Group: Development/Python3
Url: https://pypi.org/project/jupyterlab-pygments

BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-jupyter-builder
BuildRequires: python3-module-hatch-nodejs-version

%description
Pygments theme using JupyterLab CSS variables.

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%_datadir/jupyter/labextensions/jupyterlab_pygments
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Nov 28 2023 Anton Vyatkin <toni@altlinux.org> 0.3.0-alt1
- new version 0.3.0

* Mon Jul 03 2023 Anton Vyatkin <toni@altlinux.org> 0.2.2-alt1
- New version 0.2.2.

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1
- Updated to upstream version 0.1.2.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt1
- Initial build for ALT.
