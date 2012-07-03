# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/zip gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname skstream
Name:           libskstream
Version:        0.3.8
Release:        alt1_3
Summary:        C++ I/O library for WorldForge clients/servers

Group:          Development/C++
License:        GPLv2+
URL:            http://worldforge.org/dev/eng/libraries/skstream
Source0:        http://downloads.sourceforge.net/worldforge/%{oldname}-%{version}.tar.bz2
Patch1:         skstream-0.3.6-gcc44.patch

BuildRequires:  cppunit-devel
Source44: import.info
Provides: skstream = %{version}-%{release}

%description
skstream is an iotream C++ socket library and is recommended for use as a
transport for Atlas-C++. It is capable of creating iostream-based socket
connections for both clients and servers.


%package devel
Summary:        Development files for skstream
Group:   Development/C++
Requires: libskstream = %{version}-%{release}
Provides: skstream-devel = %{version}-%{release}


%description devel
Libraries and header files for developing applications that use skstream.


%prep
%setup -q -n %{oldname}-%{version}
%patch1 -p0


%build
%configure
make %{?_smp_mflags}

# It looks like upstream forgot the doxygen input file?
#make docs


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{oldname}-0.3.la

### cleaning up redundant docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{oldname}-%{version}

# Fix one file that gets installed incorrectly
mv $RPM_BUILD_ROOT%{_libdir}/%{oldname}-0.3/include/%{oldname}/*.h $RPM_BUILD_ROOT%{_includedir}/%{oldname}-0.3/%{oldname}
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{oldname}-%{version}

%check
# Run tests in debug mode so asserts won't be skipped
sed -i -e 's/-DNDEBUG/-DDEBUG/' test/Makefile
make %{?_smp_mflags} check || :

%files
%doc AUTHORS COPYING README README.FreeSockets TODO ChangeLog
%{_libdir}/lib%{oldname}-0.3.so.*


%files devel
%{_includedir}/%{oldname}-0.3
%{_libdir}/lib%{oldname}-0.3.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.8-alt1_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.8-alt1_2
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.8-alt1_1
- initial release by fcimport

