%define  modulename resolvelib

Name:    python3-module-%modulename
Version: 1.1.0
Release: alt1

Summary: Resolve abstract dependencies into concrete ones 
License: ISC
Group:   Development/Python3
URL:     https://github.com/sarugaku/resolvelib

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %modulename-%version.tar

%description
ResolveLib at the highest level provides a Resolver class that includes
dependency resolution logic. You give it some things, and a little information
on how it should interact with them, and it will spit out a resolution result.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst CHANGELOG.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version.dist-info/

%changelog
* Fri Nov 01 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.
- Built using pyproject macros.

* Fri Mar 10 2023 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version.

* Wed Mar 08 2023 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version.

* Thu Nov 17 2022 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- New version.

* Fri Nov 26 2021 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1
- New version.

* Thu Oct 28 2021 Andrey Cherepanov <cas@altlinux.org> 0.5.5-alt1
- Initial build for Sisyphus.
