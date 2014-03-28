%define  modulename testfixtures

Name:    python-module-%modulename
Version: 3.0.1
Release: alt1

Summary: A collection of helpers and mock objects for unit tests and doc tests
License: MIT
Group:   Development/Python
URL:     http://www.simplistix.co.uk/software/python/testfixtures

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

Source:  %modulename-%version.tar

%description
TestFixtures is a collection of helpers and mock objects that are useful
when writing unit tests or doc tests.

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
* Fri Mar 28 2014 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- Initial build for ALT Linux
