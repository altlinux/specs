Group: Development/Python
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
BuildRequires: python-devel python-module-setuptools python3-module-setuptools
# END SourceDeps(oneline)
%define oldname pybox2d
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           python-module-pybox2d
Version:        2.3.2
Release:        alt1.1_10
Summary:        A 2D rigid body simulation library for Python

License:        zlib
URL:            https://github.com/pybox2d/%{oldname}
Source0:        https://github.com/pybox2d/%{oldname}/archive/%{version}.tar.gz#/%{oldname}-%{version}.tar.gz

# Replace deprecated use of _swigconstant
# Upstream pull request: https://github.com/pybox2d/pybox2d/pull/90
Patch0:			replace-deprecated-swigconstant.patch

BuildRequires:  gcc gcc-c++
BuildRequires:  swig
Source44: import.info

%description
Programmer's can use Box2D in their games to make objects move in
believable ways and make the world seem more interactive. From the
game's point of view a physics engine is just a system for procedural
animation.

%package -n python3-module-pybox2d
Group: Development/Python
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-module-distribute

%{?python_provide:%python_provide python3-%{oldname}}

%description -n python3-module-pybox2d
Programmer's can use Box2D in their games to make objects move in
believable ways and make the world seem more interactive. From the
game's point of view a physics engine is just a system for procedural
animation.

This package provides the Python 3 build of %{oldname}.

%prep
%setup -q -n %{oldname}-%{version}
%patch0 -p1


%build
%python_build
%python3_build

%install
%python_install
%python3_install

 
%files -n python-module-pybox2d
%doc --no-dereference LICENSE
%doc README.md examples/*
%{python_sitelibdir}/*

%files -n python3-module-pybox2d
%doc --no-dereference LICENSE
%doc README.md examples/*
%{python3_sitelibdir}/*

%changelog
* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1.1_10
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1.1_5
- update to new release by fcimport

* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1.1
- applied repocop patch

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1
- automated PyPI update

* Tue May 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_1
- converted for ALT Linux by srpmconvert tools

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.2b2-alt1_13
- fixed build

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2b2-alt1_8
- new version

