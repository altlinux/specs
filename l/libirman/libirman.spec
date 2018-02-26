# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libirman
Version:        0.4.5
Release:        alt3_6
Summary:        Library for IRMAN hardware

Group:          System/Libraries
#The files which make up the library are covered under the GNU Library
#General Public License, which is in the file COPYING.lib.
#The files which make up the test programs and the documentation are covered
#under the GNU General Public License, which is in the file COPYING.
License:        GPLv2+ and LGPLv2+
URL:            http://lirc.sourceforge.net/software/snapshots/
Source0:        http://downloads.sourceforge.net/lirc/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf automake libtool
Source44: import.info

%description
A library for accessing the IRMAN hardware from Linux and other Unix systems.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libirman = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
libtoolize --force --copy
autoreconf
%configure --disable-static --disable-rpath \
  --prefix=%{_prefix} \
  --mandir=%{_mandir} \
  --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc COPYING* README TODO NEWS
%config(noreplace) %{_sysconfdir}/irman.conf
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%doc TECHNICAL
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt3_6
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt2_5
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1_5
- initial import by fcimport

