Group: Development/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           pstreams-devel
Version:        1.0.3
Release:        alt1_1
Summary:        POSIX Process Control in C++

License:        Boost
URL:            http://pstreams.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pstreams/pstreams-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  perl
BuildRequires:  gawk
BuildArch:      noarch
Source44: import.info
Provides: pstreams = %version
Conflicts: pstreams < %version
Obsoletes: pstreams < %version


%description
PStreams classes are like C++ wrappers for the POSIX.2 functions
popen(3) and pclose(3), using C++ iostreams instead of C's stdio
library.

%prep
%setup -q -n pstreams-%{version}

%build
%make_build
make docs

%install
make install  DESTDIR=$RPM_BUILD_ROOT includedir=%{_includedir}

%files
%doc --no-dereference LICENSE_1_0.txt
%doc doc/html README AUTHORS ChangeLog
%{_includedir}/pstreams


%changelog
* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_8
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_6
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_6
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_5
- fc import

