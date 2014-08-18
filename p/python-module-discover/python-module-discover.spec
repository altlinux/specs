%def_with python3
Name:           python-module-discover
Version:        0.4.0
Release:        alt2
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

%if_with python3
%package -n python3-module-discover
Summary:        Test discovery for unittest. Backported from Python 2.7 for Python 24+
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3

%description -n python3-module-discover
This is the test discovery mechanism and ``load_tests`` protocol for unittest
backported from Python 2.7 to work with Python 2.4 or more recent (including 
Python 3).

%endif

%prep
%setup
%patch0 -p1

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.txt
%{python_sitelibdir}/*

%if_with python3
%files -n python3-module-discover
%doc README.txt
%{python3_sitelibdir}/*
%endif

%changelog
* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4.0-alt2
- Enable python3

* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4.0-alt1
- First build for ALT (based on OpenSuSe 0.4.0-2.2.src)

