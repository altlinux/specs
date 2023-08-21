%define _unpackaged_files_terminate_build 1

Name: py3dephell
Version: 0.1.0
Release: alt1

Summary: Bunch of tools to control project dependencies and provides
License: GPLv2
Group: Development/Python3

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python3(setuptools) python3(wheel)
BuildRequires: python3-module-pyproject-installer rpm-build-python3

%description
%summary

%package -n python3-module-%name
Summary: python3 modules to control python3 project dependencies and provides
Group: Development/Python3

%description -n python3-module-%name
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
env PYTHONPATH=%buildroot%python3_sitelibdir_noarch python3 -m unittest discover -s tests -v

%files -n python3-module-%name
%doc README.md
%python3_sitelibdir_noarch/%{name}*
%_bindir/py3*

%changelog
* Mon Aug 07 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
