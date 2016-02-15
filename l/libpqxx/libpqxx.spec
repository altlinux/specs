# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dot /usr/bin/doxygen /usr/bin/pkg-config /usr/bin/xmlto boost-devel-headers gcc-c++ libpq5.8-devel libsocket
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared

Name:           libpqxx
Summary:        C++ client API for PostgreSQL
Epoch:          1
Version:        4.0.1
Release:        alt1_6

License:        BSD
URL:            http://pqxx.org/
Source0:        http://pqxx.org/download/software/libpqxx/libpqxx-%{version}.tar.gz
Source1:        http://pqxx.org/download/software/libpqxx/libpqxx-%{version}.tar.gz.md5sum

Patch3:         libpqxx-2.6.8-multilib.patch

BuildRequires:  postgresql-devel
BuildRequires:  python
Source44: import.info

%description
C++ client API for PostgreSQL. The standard front-end (in the sense of
"language binding") for writing C++ programs that use PostgreSQL.
Supersedes older libpq++ interface.

%package devel
Group: Development/C
Summary:        Development tools for %{name} 
Requires:       %{name}%{?_isa} = %{epoch}:%{version}
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


%build
%configure --enable-shared --disable-static

make %{?_smp_mflags}


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

