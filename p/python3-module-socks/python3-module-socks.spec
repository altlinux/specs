%define _unpackaged_files_terminate_build 1

%define  modulename socks
%define  pypi_name PySocks

Name:    python3-module-%modulename
Version: 1.7.1
Release: alt3

Summary: A SOCKS proxy client and wrapper for Python.
License: BSD
Group:   Development/Python
URL:     https://github.com/Anorov/PySocks

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildArch: noarch

# PyPI name
%py3_provides %pypi_name
Provides: python3-module-%pypi_name = %EVR

Source:  %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/socks*
%python3_sitelibdir/__pycache__/socks*
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Tue Jul 26 2022 Stanislav Levin <slev@altlinux.org> 1.7.1-alt3
- Provided well-known PyPI name.

* Mon Dec 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.1-alt2
- Built version for python-3.

* Sat Oct 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- New version.

* Sun May 12 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- New version.

* Sun Dec 24 2017 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- New version.

* Thu Sep 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.6.7-alt1
- Initial build for Sisyphus
