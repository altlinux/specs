# BEGIN SourceDeps(oneline):
BuildRequires: libirman-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libirman
Epoch:          1
Version:        0.5.2
Release:        alt1_4
Summary:        Library for IRMAN hardware

Group:          System/Libraries

#The files which make up the library are covered under the GNU Library
#General Public License, which is in the file COPYING.lib.
#The files which make up the test programs and the documentation are covered
#under the GNU General Public License, which is in the file COPYING.
License:        GPLv2+ and LGPLv2+
URL:            http://sourceforge.net/projects/libirman/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf-common, automake-common, libtool-common
BuildRequires:  liblirc-devel >= 0.9.4
Source44: import.info

%description
Runtime libraries for accessing the IrMan hardware.

The IrMan hardware((http://www.intolect.com/irmandetail.htm) is  nowadays
discontinued. However, some modern hardware (notably the irtoy) is able to
emulate the irman protocol.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    devel
Libraries and header files for developing applications that use %{name}.

The IrMan hardware((http://www.intolect.com/irmandetail.htm) is  nowadays
discontinued. However, some modern hardware (notably the irtoy) is able to
emulate the irman protocol.


%package  -n    lirc-drv-irman
Group: System/Libraries
Summary:        lircd(8) plugin for handling IrMan devices.
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       lirc >= 0.9.4

%description  -n lirc-drv-irman
A lirc plugin with a single driver, replacing the irman support which
was built-in in lirc prior to 0.9.4.


%prep
%setup -q


%build
libtoolize --force --copy --install
autoreconf -i
%configure --disable-static
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete
rm  $RPM_BUILD_ROOT%{_docdir}/libirman/TECHNICAL


%files
%doc COPYING* README TODO NEWS
%config(noreplace) %{_sysconfdir}/irman.conf
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%doc TECHNICAL
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libirman.pc

%files -n lirc-drv-irman
%{_libdir}/lirc/plugins/irman.so
%{_docdir}/lirc/plugindocs/irman.html
%{_datadir}/lirc/configs/irman.conf


%changelog
* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.5.2-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt3_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt3_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt3_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt3_10
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt3_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt3_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt3_7
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt3_6
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt2_5
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1_5
- initial import by fcimport

