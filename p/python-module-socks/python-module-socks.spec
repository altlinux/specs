%define  modulename socks
%define  oname PySocks

Name:    python-module-%modulename
Version: 1.6.8
Release: alt1

Summary: A SOCKS proxy client and wrapper for Python.
License: BSD
Group:   Development/Python
URL:     https://github.com/Anorov/PySocks

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
%summary

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/socks*
%python_sitelibdir/*.egg-info

%changelog
* Sun Dec 24 2017 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- New version.

* Thu Sep 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.6.7-alt1
- Initial build for Sisyphus
