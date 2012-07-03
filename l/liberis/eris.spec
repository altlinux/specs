# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(AutoLoader.pm) perl(overload.pm) perl-devel perl-podlators pkgconfig(atlascpp-0.6) pkgconfig(glib-2.0) pkgconfig(mercator-0.3) pkgconfig(skstream-0.3) pkgconfig(wfmath-0.3)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname eris
Name:           liberis
Version:        1.3.19
Release:        alt3_4
Summary:        Client-side session layer for Atlas-C++

Group:          Development/C++
# All files untagged except for Eris/Operations.{cpp,h} which is labeled
# LGPL with no version.
License:        LGPLv2+
URL:            http://worldforge.org/dev/eng/libraries/eris
Source0:        http://downloads.sourceforge.net/worldforge/%{oldname}-%{version}.tar.bz2
# The following patch is essentiall upstream and should be dropped at the next release

BuildRequires: mercator-devel doxygen
BuildRequires: atlascpp-devel >= 0.5.98
BuildRequires: wfmath-devel >= 0.3.2
BuildRequires: skstream-devel >= 0.3.5

BuildRequires:  libsigc++2-devel glib-devel
Source44: import.info
Provides: eris = %{version}-%{release}

%description
A client side session layer for WorldForge; Eris manages much of the generic
work required to communicate with an Atlas server. Client developers can extend
Eris in a number of ways to rapidly add game and client specific functions, and
quickly tie game objects to whatever output representation they are using.


%package devel
Summary:        Development files for Eris
Group:          Development/C++
Requires:       eris = %{version}-%{release}
Provides: eris-devel = %{version}-%{release}


%description devel
Libraries and header files for developing applications that use Eris.


%prep
%setup -q -n %{oldname}-%{version}


%build
%configure
make %{?_smp_mflags}
make doc

# Remove timestamps from the generated documentation to avoid
# multiarch conflicts

for file in docs/html/*.html ; do
    sed -i -e 's/Generated on .* for Eris by/Generated for Eris by/' $file
done

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{oldname}-1.3.la

# They seem to hang sometimes.
%check
# Run tests in debug mode so asserts won't be skipped
sed -i -e 's/-DNDEBUG/-DDEBUG/' test/Makefile
make %{?_smp_mflags} check


%files
%doc AUTHORS ChangeLog CHANGES-1.4 COPYING NEWS README TODO
%{_libdir}/lib%{oldname}-1.3.so.*


%files devel
%doc docs/html/*
%{_includedir}/Eris-1.3
%{_libdir}/lib%{oldname}-1.3.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt3_4
- rebuild with new libmercator

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_4
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_3
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_1
- rebuild with new libwfmath

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt1_1
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.18-alt1_3
- initial release by fcimport

