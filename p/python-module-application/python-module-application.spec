%define modulename application

Name:    python-module-%modulename
Version: 2.6.0
Release: alt1

Summary: Basic building blocks for Python applications
License: LGPLv2+
Group:   Development/Python
URL:     https://github.com/AGProjects/python-application

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-zope.interface

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This package is a collection of modules that are useful when building
python applications. Their purpose is to eliminate the need to divert
resources into implementing the small tasks that every application needs
to do in order to run successfully and focus instead on the application
logic itself.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Fri May 31 2019 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version.

* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- New version.

* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
