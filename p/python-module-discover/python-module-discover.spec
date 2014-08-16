Name:           python-module-discover
Version:        0.4.0
Release:        alt1
Summary:        Test discovery for unittest. Backported from Python 2.7 for Python 24+
License:        BSD-3-Clause
Group:          Development/Python
Url:            http://pypi.python.org/pypi/discover/
Source:         %{name}-%{version}.tar
# https://code.google.com/p/unittest-ext/issues/detail?id=79
Patch0:         bug-79-fix.patch
BuildRequires:  python-devel
BuildArch:      noarch

%description
This is the test discovery mechanism and ``load_tests`` protocol for unittest
backported from Python 2.7 to work with Python 2.4 or more recent (including 
Python 3).

%prep
%setup
%patch0 -p1

%build
%python_build

%install
%python_install

%files
%doc README.txt
%{python_sitelibdir}/*

%changelog
* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4.0-alt1
- First build for ALT (based on OpenSuSe 0.4.0-2.2.src)

