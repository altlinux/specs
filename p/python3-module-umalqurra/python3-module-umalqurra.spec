%def_disable snapshot
%define modname umalqurra

Name: python3-module-%modname
Version: 0.2
Release: alt1

Summary: Python Hijri Umalqurra
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

%if_disabled snapshot
Source: https://pypi.io/packages/source/u/%modname/%modname-%version.tar.gz
%else
#VCS: https://github.com/tytkal/python-hijiri-ummalqura.git
Source: %modname-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-pylint
%description

Python Umalqurra Calender is an API that will give you the ability to
convert Gregorian to Hijri and hijri to Gregorian it will give you the
day name in arabic and english , and the month name in Hijri arabic and
Gregorian.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py check

%files
%python3_sitelibdir_noarch/*
#%doc README*


%changelog
* Tue Jul 28 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- first build for Sisyphus



