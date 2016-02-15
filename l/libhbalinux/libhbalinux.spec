# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(HBAAPI) pkgconfig(pciaccess)
# END SourceDeps(oneline)
BuildRequires: pkgconfig(libudev)
%add_optflags %optflags_shared
Name:               libhbalinux
Version:            1.0.17
Release:            alt1_3
Summary:            FC-HBAAPI implementation using scsi_transport_fc interfaces
Group:              System/Libraries
License:            LGPLv2
URL:                http://www.open-fcoe.org
Source0:            %{name}-%{version}.tar.gz
Patch0:             libhbalinux-1.0.13-conf.patch
Patch1:             libhbalinux-fix-non-pci-netdev.patch
BuildRequires:      libhbaapi-devel >= 2.2.9
BuildRequires:      libpciaccess-devel libtool automake systemd-devel
Requires:           libhbaapi >= 2.2.9
Requires(post):     grep
Requires(postun):   grep
Source44: import.info

%description
SNIA HBAAPI vendor library built on top of the scsi_transport_fc interfaces.

%package devel
Summary:            A file needed for libhbalinux application development
Group:              Development/C
Requires:           %{name}%{?_isa} = %{version}
Requires:           pkgconfig

%description devel
The libhbalinux-devel package contains the library pkgconfig file.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./bootstrap.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post
ORG=org.open-fcoe.libhbalinux
LIB=%{_libdir}/libhbalinux.so.2.0.2
STR="$ORG	$LIB"
CONF=%{_sysconfdir}/hba.conf
if test -f $CONF; then
  grep -E -q ^[[:space:]]*$ORG[[:space:]]+$LIB $CONF
  if test $? -ne 0; then
    echo $STR >> $CONF;
  fi
fi

%postun
ORG=org.open-fcoe.libhbalinux
CONF=%{_sysconfdir}/hba.conf
if test -f $CONF; then
  grep -v $ORG $CONF > %{_sysconfdir}/hba.conf.new
  mv %{_sysconfdir}/hba.conf.new %{_sysconfdir}/hba.conf
fi

%files
%doc README COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.17-alt1_3
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.17-alt1_2
- new version

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.16-alt1_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.16-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.16-alt1_3
- update to new release by fcimport

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.16-alt1_2
- update to new release by fcimport

* Mon Jun 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.16-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.14-alt1_5
- update to new release by fcimport

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.14-alt1_4
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.14-alt1_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.14-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.14-alt1_1
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt2_3
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_1
- initial import by fcimport

