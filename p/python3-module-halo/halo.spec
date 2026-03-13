%define   modulename halo

%def_with check

Name:     python3-module-%modulename
Version:  0.0.31
Release:  alt1

Summary:  Beautiful spinners for terminal, IPython and Jupyter

License:  MIT
Group:    Development/Python3
URL:      https://pypi.org/project/halo
VCS:      https://github.com/manrajgrover/halo

BuildArch: noarch

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar
Patch:    halo-alt-fix-tests.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-spinners
BuildRequires: python3-module-log-symbols
BuildRequires: python3-module-six
BuildRequires: python3-module-termcolor
BuildRequires: python3-module-ipywidgets
%endif

%description
%summary.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%python3_sitelibdir/%modulename
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Fri Mar 13 2026 Grigory Ustinov <grenka@altlinux.org> 0.0.31-alt1
- Initial build for Sisyphus.
