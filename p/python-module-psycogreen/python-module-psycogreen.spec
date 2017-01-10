%define  modulename psycogreen

Name:    python-module-%modulename
Version: 1.0
Release: alt1

Summary: psycopg2 integration with coroutine libraries
License: BSD
Group:   Development/Python
URL:     https://bitbucket.org/dvarrazzo/psycogreen

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  %modulename-%version.tar

%description
The psycogreen package enables psycopg2 to work with coroutine
libraries, using asynchronous calls internally but offering a blocking
interface so that regular code can run unmodified.

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
* Tue Jan 10 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
