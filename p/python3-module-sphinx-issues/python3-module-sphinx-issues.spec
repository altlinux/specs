%define  modulename sphinx_issues
%define  origname sphinx-issues

Name:    python3-module-%origname
Version: 5.0.0
Release: alt1

Summary: A Sphinx extension for linking to your project's issue tracker
License: MIT
Group:   Development/Python3
URL:     https://github.com/sloria/sphinx-issues

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-wheel
BuildRequires: python3-module-flit-core

BuildArch: noarch

Source: %origname-%version.tar

%description
A Sphinx extension for linking to your project's issue tracker. Includes
roles for linking to issues, pull requests, user profiles, with built-in
support for GitHub (though this works with other services).

%prep
%setup -n %origname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/%modulename
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Sat Oct 12 2024 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Tue Apr 16 2024 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- New version.

* Mon Jan 22 2024 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.

* Fri Jan 14 2022 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version.

* Wed Jan 05 2022 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
