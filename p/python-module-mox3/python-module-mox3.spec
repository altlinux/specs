%global pypi_name mox3

Name:           python-module-%{pypi_name}
Version:        0.7.0
Release:        alt1
Summary:        Mock object framework for Python
License:        Apache-2.0
Group:		Development/Python
Url:            http://www.openstack.org/
Source:         %{name}-%{version}.tar
BuildRequires:  python-devel
BuildRequires:  python-module-pbr
BuildRequires:  python-module-setuptools
Requires:       python-module-pbr >= 0.5.21

BuildArch:      noarch

%description
Mox3 is an unofficial port of the Google mox framework
(http://code.google.com/p/pymox/) to Python 3. It was meant to be as compatible
with mox as possible, but small enhancements have been made. The library was
tested on Python version 3.2, 2.7 and 2.6.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc COPYING.txt ChangeLog AUTHORS README.rst
%{python_sitelibdir}/*

%changelog
* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.7.0-alt1
- First build for ALT (based on Suse 0.7.0-2.1.src)

