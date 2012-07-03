# BEGIN SourceDeps(oneline):
BuildRequires: perl(IO/Select.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:        Blitzed open proxy monitor library
Name:           libopm
Version:        0.1
Release:        alt3_11.20050731cvs
License:        GPLv2+
Group:          System/Libraries
URL:            http://wiki.blitzed.org/BOPM
# cvs -z3 -d:pserver:anon@cvs.blitzed.org:/ co -D "20050731 23:59" libopm
# find libopm -type f -name .cvsignore -exec rm -f {} ';'
# find libopm -type d -name CVS -exec rm -rf {} 2>/dev/null ';'
# mv -f libopm libopm-$(grep AC_INIT libopm/configure.in | sed -e 's/.*\[\(.*\)\].*/\1/')
Source:         %{name}-%{version}.tar.gz
Patch:          libopm-0.1-multilib.patch
BuildRequires:  doxygen
Source44: import.info

%description
An open proxy detection library, developed by the blitzed
IRC network team. Its original use was to detect open proxies
running on clients connecting to various IRC servers, but it
has evolved to become a generic open proxy detection library.

%package devel
Summary:        Headers and development libraries for libopm
Group:          Development/C
Requires:       libopm = %{version}-%{release}

%description devel
The libopm-devel package contains the header files and libraries
necessary for developing applications which use libopm.

%prep
%setup -q
%patch -p1 -b .multilib

%build
%configure --disable-static
make %{?_smp_mflags}
cd doc && doxygen && mv -f api html

%install
make DESTDIR=$RPM_BUILD_ROOT install

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%doc ChangeLog LICENSE
%{_libdir}/%{name}.so.*

%files devel
%doc doc/libopm-api.txt doc/html
%{_includedir}/opm*
%{_libdir}/%{name}.so

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_11.20050731cvs
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_11.20050731cvs
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_10.20050731cvs
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_10.20050731cvs
- initial import by fcimport

