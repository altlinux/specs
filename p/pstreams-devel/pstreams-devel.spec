# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define packagename pstreams

Name:           pstreams-devel
Version:        0.7.0
Release:        alt1_7
Summary:        POSIX Process Control in C++

Group:          Development/C
License:        LGPLv3+
URL:            http://%{packagename}.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{packagename}/%{packagename}-%{version}.tar.gz

BuildRequires:  doxygen
BuildArch:      noarch
Source44: import.info
Provides: pstreams = %version
Conflicts: pstreams < %version
Obsoletes: pstreams < %version


%description
PStreams class is like a C++ wrapper for the POSIX.2 functions
popen(3) and pclose(3), using C++ iostreams instead of C's stdio
library.

%prep
%setup -q -n %{packagename}-%{version}

%build
make %{?_smp_mflags}

%install
make install  DESTDIR=$RPM_BUILD_ROOT prefix=/usr

%files
%doc doc/html COPYING.LIB README AUTHORS ChangeLog
%{_includedir}/pstreams

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_6
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_5
- fc import

