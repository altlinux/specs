Name: catch
Version: 1.9.7
Release: alt2

Summary: C++ Unit Test framework ("all in one header")

License: Boost Software License, Version 1.0
Group: Development/C++
Url: https://github.com/philsquared/Catch

Packager: Pavel Vainerman <pv@altlinux.ru>
BuildArch: noarch

# Source-url: https://github.com/philsquared/Catch/raw/master/single_include/catch.hpp
Source: %name-%version.tar

%description
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%package devel
Summary: C++ Unit Test framework ("all in one header")
Group: Development/C++
Conflicts: catch < 1.9.7-alt2
Obsoletes: catch < 1.9.7-alt2
Provides: catch = %EVR

%description devel
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%prep
%setup

%build

%install
mkdir -p %buildroot%_includedir
mv -f catch.hpp %buildroot%_includedir

%files devel
%_includedir/*.hpp

%changelog
* Thu Dec 14 2017 Pavel Vainerman <pv@altlinux.ru> 1.9.7-alt2
- returned version 1.x

# * Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2
# - NMU: added proper devel subpackage

# * Fri Nov 03 2017 Pavel Vainerman <pv@altlinux.ru> 2.0.1-alt1
# - new version (2.0.1) with rpmgs script

* Fri Aug 11 2017 Pavel Vainerman <pv@altlinux.ru> 1.9.7-alt1
- new version (1.9.7) with rpmgs script

* Wed Jun 14 2017 Pavel Vainerman <pv@altlinux.ru> 1.9.4-alt1
- build new version

* Sat May 06 2017 Pavel Vainerman <pv@altlinux.ru> 1.9.3-alt2
- up build 

* Sat May 06 2017 Pavel Vainerman <pv@altlinux.ru> 1.9.3-alt1
- new version

* Mon Mar 13 2017 Pavel Vainerman <pv@altlinux.ru> 1.8.2-alt1
- new version (1.8.2) with rpmgs script

* Wed Feb 22 2017 Pavel Vainerman <pv@altlinux.ru> 1.7.2-alt1
- new version (1.7.2) with rpmgs script

* Mon Jan 16 2017 Pavel Vainerman <pv@altlinux.ru> 1.6.0-alt2
- new version (1.6.0) with rpmgs script

* Mon Jan 16 2017 Pavel Vainerman <pv@altlinux.ru> 1.6.0-alt1
- build new version

* Sat Oct 29 2016 Pavel Vainerman <pv@altlinux.ru> 1.5.8-alt1
- build new version

* Fri Sep 30 2016 Pavel Vainerman <pv@altlinux.ru> 1.5.7-alt1
- build new version

* Mon Jul 18 2016 Pavel Vainerman <pv@altlinux.ru> 1.5.6-alt1
- build new version

* Mon May 09 2016 Pavel Vainerman <pv@altlinux.ru> 1.5.2-alt1
- build new version

* Fri Apr 29 2016 Pavel Vainerman <pv@altlinux.ru> 1.5.1-alt1
- build new version

* Sat Apr 16 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.0-alt2
- minor update

* Fri Mar 18 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.0-alt1
- build new version

* Tue Mar 01 2016 Pavel Vainerman <pv@altlinux.ru> 1.3.5-alt1
- build new version

* Fri Feb 19 2016 Pavel Vainerman <pv@altlinux.ru> 1.3.4-alt1
- build new version

* Wed Dec 16 2015 Pavel Vainerman <pv@altlinux.ru> 1.3.1-alt1
- build new version

* Mon Oct 26 2015 Pavel Vainerman <pv@altlinux.ru> 1.2.1-alt3
- spec: fix URL for project

* Mon Oct 26 2015 Pavel Vainerman <pv@altlinux.ru> 1.2.1-alt2
- new build (merge changes from master repository)

* Tue Jun 30 2015 Pavel Vainerman <pv@altlinux.ru> 1.2.1-alt1
- new version

* Wed May 13 2015 Pavel Vainerman <pv@altlinux.ru> 1.1-alt2
- rebuild (new .gear/rules)

* Mon Mar 30 2015 Pavel Vainerman <pv@altlinux.ru> 1.1-alt1
- new upstream version

* Mon Oct 06 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt1.2
- test rebuild

* Fri Oct 03 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt1.1
- rename package Catch --> catch

* Thu Oct 02 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt1
- moved catch.hpp directly into %_includedir

* Tue Sep 30 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt0.2
- test build

* Tue Sep 30 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt0.1
- initial commit
