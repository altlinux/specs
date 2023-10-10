%define  modulename pypuppetdb

Name:    python3-module-%modulename
Version: 3.2.0
Release: alt1
Epoch: 1

Summary: Python library for working with the PuppetDB API
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/voxpupuli/pypuppetdb

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This library is a thin wrapper around the REST API providing some
convenience functions and objects to request and hold data from
PuppetDB.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install
rm -f %buildroot%_prefix/requirements_for_tests/requirements-test.txt

%files
%doc README.md CHANGELOG.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Tue Oct 10 2023 Andrey Cherepanov <cas@altlinux.org> 1:3.2.0-alt1
- New version.

* Tue May 02 2023 Andrey Cherepanov <cas@altlinux.org> 1:3.1.0-alt1
- New version.

* Thu Jun 27 2019 Andrey Cherepanov <cas@altlinux.org> 3.3.3-alt1
- Initial build for Sisyphus
