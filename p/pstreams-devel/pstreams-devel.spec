# for tests
BuildRequires:  /proc
Group: Development/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           pstreams-devel
Version:        1.0.3
Release:        alt1_10
Summary:        POSIX Process Control in C++

License:        BSL-1.0
URL:            http://pstreams.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pstreams/pstreams-%{version}.tar.gz
Patch0:         pstreams-make-check.patch
Patch1:         pstreams-doxyfile.patch
Patch2:         pstreams-test-race.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  perl
BuildRequires:  gawk
BuildRequires:  coreutils
BuildArch:      noarch
Source44: import.info
Provides: pstreams = %version
Conflicts: pstreams < %version
Obsoletes: pstreams < %version


%description
PStreams classes are like C++ wrappers for the POSIX.2 functions
popen(3) and pclose(3), using C++ iostreams instead of C's stdio
library.

%package -n pstreams-doc
Group: Development/Other
Summary: Documentation for pstreams
BuildArch: noarch

%description -n pstreams-doc
API documentation for the pstreams-devel package, in HTML format.

%prep
%setup -q -n pstreams-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build docs

%check
make %{?_smp_mflags} EXTRA_CXXFLAGS="$CXXFLAGS" check

%install
make install  DESTDIR=$RPM_BUILD_ROOT includedir=%{_includedir}

%files
%doc --no-dereference LICENSE_1_0.txt
%{_includedir}/pstreams

%files -n pstreams-doc
%doc doc/html README AUTHORS ChangeLog

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1.0.3-alt1_10
- update to new release by fcimport

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

