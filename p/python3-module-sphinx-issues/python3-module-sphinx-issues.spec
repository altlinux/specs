%define  modulename sphinx-issues

Name:    python3-module-%modulename
Version: 3.0.1
Release: alt1

Summary: A Sphinx extension for linking to your project's issue tracker
License: MIT
Group:   Development/Python3
URL:     https://github.com/sloria/sphinx-issues

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
A Sphinx extension for linking to your project's issue tracker. Includes
roles for linking to issues, pull requests, user profiles, with built-in
support for GitHub (though this works with other services).

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Jan 14 2022 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version.

* Wed Jan 05 2022 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
