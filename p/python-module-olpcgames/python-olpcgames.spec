# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
# END SourceDeps(oneline)
%define oldname python-olpcgames
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-module-olpcgames
Version:        1.6
Release:        alt1_12
Summary:        Utilities for developing games on the OLPC platform

Group:          Development/Python
License:        BSD
URL:            http://wiki.laptop.org/go/OLPCGames
Source0:        http://dev.laptop.org/~mcfletch/OLPCGames/OLPCGames-%{version}.tar.gz

Requires:       python-module-pygame
BuildArch:      noarch
BuildRequires:  python-dev
BuildRequires:  python-module-setuptools
Source44: import.info

%description
This python package contains various resources and utility classes for making
games on the OLPC system. Specifically it enables using PyGame in the Sugar 
environment.

%prep
%setup -q -n OLPCGames-%{version}


%build
export DISPLAY=:0.0
%{__python} setup.py build


%install
export DISPLAY=:0.0
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# remove shebang to calm rpmlint down
sed -i -e 1d $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/olpcgames/buildmanifest.py

%files
%doc NEWS olpcgames/COPYING
%{python_sitelibdir_noarch}/*


%changelog
* Tue May 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_12
- converted for ALT Linux by srpmconvert tools

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_7
- converted for ALT Linux by srpmconvert tools

