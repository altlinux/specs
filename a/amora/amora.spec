# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pkg-config pkgconfig(bluez) pkgconfig(dbus-1) pkgconfig(imlib2) pkgconfig(x11) pkgconfig(xtst)
# END SourceDeps(oneline)
Name:           amora
Version:        1.1
Release:        alt2_16
Summary:        A mobile remote assistant

Group:          Communications
License:        GPLv2+
URL:            http://code.google.com/p/amora
Source0:        http://amora.googlecode.com/files/amora-server-%{version}.tar.gz
Patch0:         amora-aarch64.patch

BuildRequires:  libbluez-devel
BuildRequires:  libdbus-devel
BuildRequires:  imlib2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
Source44: import.info

%description
Amora is an application that enables you to control your PC desktop using a
cellphone. It uses bluetooth to send mouse and keyboard events to the
graphical session. With it you can control your slides in OpenOffice.org,
movies or any other application. Amora also has a screenshot feature, where
you can see a thumbnail in the cellphone screen of the currently focused
window in your desktop.

In order to use amora, you need a mobile phone with amora-client
installed and running. The current client is implemented in Python
for S60 (Nokia cellphones) and is available at
http://code.google.com/p/amora/

%prep
%setup -q -n amora-server-%{version}
#patch to build on aarch64, upstream notified to use autoconf 2.69
%patch0 -p 1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"


%files
%doc README COPYING
%{_bindir}/amorad
%{_mandir}/man7/amora.7*
%{_mandir}/man8/amorad.8*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_15
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13
- update to new release by fcimport

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_10
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_8
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6
- initial release by fcimport

