# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dot /usr/bin/doxygen /usr/bin/pkg-config /usr/bin/xmlto boost-devel-headers gcc-c++ libpq5.4-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared

Name:           libpqxx
Epoch:          1
Version:        3.2
Release:        alt1_0.5
Summary:        C++ client API for PostgreSQL

Group:          System/Libraries
License:        BSD
URL:            http://pqxx.org/
Source0:        http://pqxx.org/download/software/libpqxx/libpqxx-%{version}.tar.gz
Source1:        http://pqxx.org/download/software/libpqxx/libpqxx-%{version}.tar.gz.md5sum

Patch3:         libpqxx-2.6.8-multilib.patch

BuildRequires:  postgresql-devel
Source44: import.info

%description
C++ client API for PostgreSQL. The standard front-end (in the sense of
"language binding") for writing C++ programs that use PostgreSQL.
Supersedes older libpq++ interface.

%package devel
Summary:        Development tools for %{name} 
Group:          Development/C
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
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
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


%check 
# not enabled, by default, takes awhile.
%{?_with_check:make check}

%files
%doc AUTHORS ChangeLog COPYING NEWS README VERSION
%{_libdir}/libpqxx-3.2.so

%files devel
%doc README-UPGRADE
%{_bindir}/pqxx-config
%{_includedir}/pqxx/
%{_libdir}/libpqxx.so
%{_libdir}/pkgconfig/libpqxx.pc


%changelog
* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.2-alt1_0.5
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.2-alt1_0.4
- initial fc import

