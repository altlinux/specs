# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dot /usr/bin/doxygen /usr/bin/xmlto boost-devel-headers gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name:           libpqxx
Summary:        C++ client API for PostgreSQL
Epoch:          1
Version:        4.0.1
Release:        alt2_10

License:        BSD
URL:            http://pqxx.org/
Source0:        http://pqxx.org/download/software/libpqxx/libpqxx-%{version}.tar.gz
Source1:        http://pqxx.org/download/software/libpqxx/libpqxx-%{version}.tar.gz.md5sum

Patch3:         libpqxx-2.6.8-multilib.patch
Patch4:         libpqxx_configure.patch

BuildRequires:  libecpg6-devel libpq5-devel postgresql10-devel
BuildRequires:  python
Source44: import.info

%description
C++ client API for PostgreSQL. The standard front-end (in the sense of
"language binding") for writing C++ programs that use PostgreSQL.
Supersedes older libpq++ interface.

%package devel
Group: Development/C
Summary:        Development tools for %{name} 
Requires:       %{name} = %{epoch}:%{version}-%{release}
%description devel
%{summary}.

%package doc
Group: System/Libraries
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.


%prep
%setup -q

# fix spurious permissions
chmod -x COPYING

%patch3 -p1 -b .multilib
%patch4 -p1


%build
%configure --enable-shared --disable-static

%make_build


%install
make install DESTDIR=%{buildroot}

rm -fv %{buildroot}%{_libdir}/lib*.la


%check 
# FIXME: most/all fail, need already-running postgresql instance?
make %{?_smp_mflags} check ||:


%files
%doc AUTHORS ChangeLog COPYING NEWS README VERSION
%{_libdir}/libpqxx-4.0.so

%files devel
%doc README-UPGRADE
%{_bindir}/pqxx-config
%{_includedir}/pqxx/
%{_libdir}/libpqxx.so
%{_libdir}/pkgconfig/libpqxx.pc

%files doc
%doc doc/html/*


%changelog
* Wed Jan 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.0.1-alt2_10
- Updated build dependencies.

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_10
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_8
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_6
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_5
- update to new release by fcimport

* Sat Jul 11 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.2-alt2_0.6.1
- Rebuilt for gcc5 C++11 ABI (ALT#31135).

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.2-alt2_0.6
- fixed build

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.2-alt1_0.6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.2-alt1_0.5
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.2-alt1_0.4
- initial fc import

