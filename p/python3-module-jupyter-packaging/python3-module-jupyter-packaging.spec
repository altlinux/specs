%define  modulename jupyter-packaging

Name:    python3-module-%modulename
Version: 0.12.0
Release: alt1

Summary: Tools to help build and install Jupyter Python packages
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/jupyter/jupyter-packaging

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Tools to help build and install Jupyter Python packages that require a
pre-build step that may include JavaScript build steps.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install
rm -rf %buildroot%python3_sitelibdir/tests

%files
%doc *.md
%python3_sitelibdir/jupyter_packaging/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Apr 25 2022 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus.
