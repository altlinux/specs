%define oname pybox2d
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name:           python3-module-%oname
Version:        2.3.2
Release:        alt2

Summary:        A 2D rigid body simulation library for Python
License:        zlib
Group:          Development/Python3
URL:            https://github.com/pybox2d/%{oname}

Source0:        https://github.com/pybox2d/%{oname}/archive/%{version}.tar.gz#/%{oname}-%{version}.tar.gz
Source44:       import.info

# Replace deprecated use of _swigconstant
# Upstream pull request: https://github.com/pybox2d/pybox2d/pull/90
Patch0:         replace-deprecated-swigconstant.patch

BuildRequires(pre): rpm-build-python3
BuildRequires:  gcc gcc-c++
BuildRequires:  swig

%{?python_provide:%python_provide python3-%{oname}}


%description
Programmer's can use Box2D in their games to make objects move in
believable ways and make the world seem more interactive. From the
game's point of view a physics engine is just a system for procedural
animation.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')


%build
%python3_build

%install
%python3_install

%files
%doc --no-dereference LICENSE
%doc README.md examples/*
%{python3_sitelibdir}/*


%changelog
* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3.2-alt2
- python2 disabled

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

