# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pkg-config pkgconfig(x11)
# END SourceDeps(oneline)
Name:           amora
Version:        1.1
Release:        alt2_7
Summary:        A mobile remote assistant

Group:          Communications
License:        GPLv2+
URL:            http://code.google.com/p/amora
Source0:        http://amora.googlecode.com/files/amora-server-%{version}.tar.gz

BuildRequires:  libX11 libXtst-devel libbluez-devel imlib2-devel libdbus-devel
Source44: import.info
#Requires:       

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


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

%files
%doc README COPYING
%{_bindir}/amorad
%{_mandir}/man7/amora.7.*
%{_mandir}/man8/amorad.8.*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6
- initial release by fcimport

