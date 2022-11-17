%define  modulename resolvelib

Name:    python3-module-%modulename
Version: 0.9.0
Release: alt1

Summary: Resolve abstract dependencies into concrete ones 
License: ISC
Group:   Development/Python3
URL:     https://github.com/sarugaku/resolvelib

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
ResolveLib at the highest level provides a Resolver class that includes
dependency resolution logic. You give it some things, and a little information
on how it should interact with them, and it will spit out a resolution result.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst CHANGELOG.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Nov 17 2022 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- New version.

* Fri Nov 26 2021 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1
- New version.

* Thu Oct 28 2021 Andrey Cherepanov <cas@altlinux.org> 0.5.5-alt1
- Initial build for Sisyphus.
