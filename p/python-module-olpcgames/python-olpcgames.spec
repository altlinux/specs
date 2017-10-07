# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define oldname python-olpcgames
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-module-olpcgames
Version:        1.6
Release:        alt1_16
Summary:        Utilities for developing games on the OLPC platform

Group:          Development/Other
License:        BSD
URL:            http://wiki.laptop.org/go/OLPCGames
Source0:        http://dev.laptop.org/~mcfletch/OLPCGames/OLPCGames-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools

%global _description\
This python package contains various resources and utility classes for making\
games on the OLPC system. Specifically it enables using PyGame in the Sugar\
environment.
Source44: import.info

%description %_description

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

%files -n python-module-olpcgames
%doc NEWS olpcgames/COPYING
%{python_sitelibdir_noarch}/*


%changelog
* Sat Oct 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_16
- applied repocop patch

* Tue May 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_12
- converted for ALT Linux by srpmconvert tools

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_7
- converted for ALT Linux by srpmconvert tools

