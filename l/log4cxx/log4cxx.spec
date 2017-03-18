# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dot /usr/bin/iodbc-config gcc-c++ libesmtp-devel libunixODBC-devel
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: log4cxx
Version: 0.10.0
Release: alt1_23
Summary: A port to C++ of the Log4j project

License: ASL 2.0
URL: http://logging.apache.org/log4cxx/index.html
Source0: http://www.apache.org/dist/logging/log4cxx/%{version}/apache-%{name}-%{version}.tar.gz
# Filed into upstream bugtracker at:
# https://issues.apache.org/jira/browse/LOGCXX-332
Patch0: log4cxx-cstring.patch
# From Debian:
# https://anonscm.debian.org/cgit/collab-maint/log4cxx.git/plain/debian/patches/170-gcc6-fix.patch
Patch1: log4cxx-gcc6.patch
Patch2: log4cxx-gcc6-tests.patch

BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: doxygen

%description
Log4cxx is a popular logging package written in C++. One of its distinctive
features is the notion of inheritance in loggers. Using a logger hierarchy it
is possible to control which log statements are output at arbitrary
granularity. This helps reduce the volume of logged output and minimize the
cost of logging.

%package devel
Group: Development/C
Requires: %{name} = %{version}-%{release}
Summary: Header files for Log4xcc - a port to C++ of the Log4j project

%description devel
Header files and documentation you can use to develop with %{name}.

%package doc
Group: System/Libraries
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
Documentation for %{name}.


%prep
%setup -q -n apache-%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
sed -i.libdir_syssearch -e \
 '/sys_lib_dlsearch_path_spec/s|/usr/lib |/usr/lib /usr/lib64 /lib /lib64 |' \
 configure
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/html .
rm $RPM_BUILD_ROOT/%{_libdir}/liblog4cxx.la

%files
%{_libdir}/liblog4cxx.so.10.0.0
%{_libdir}/liblog4cxx.so.10

%doc NOTICE KEYS
%doc LICENSE


%files devel
%{_includedir}/log4cxx
%{_libdir}/liblog4cxx.so
%{_libdir}/pkgconfig/liblog4cxx.pc

%files doc
%doc LICENSE
%doc html/

%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_23
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_19
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_17
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_16
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_15
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_14
- initial fc import

