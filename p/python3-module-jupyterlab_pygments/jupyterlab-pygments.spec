%define _unpackaged_files_terminate_build 1

%define oname jupyterlab_pygments

Name: python3-module-%oname
Version: 0.1.2
Release: alt1
Summary: Pygments theme using JupyterLab CSS variables
License: BSD-3-Clause and MIT and Python
Group: Development/Python3
Url: https://pypi.org/project/jupyterlab-pygments

BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
Pygments theme using JupyterLab CSS variables

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%doc README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt1
- Updated to upstream version 0.1.2.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt1
- Initial build for ALT.
