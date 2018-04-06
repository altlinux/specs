Name:           x2goclient
Version:        4.1.1.1
Release:        alt2
Summary:        X2Go Client application (Qt4)

Group:          Communications
License:        GPLv2+
URL:            http://www.x2go.org
Source0:        %name-%version.tar
# Drop clumsy attempt at Kerberos delegation
# http://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=731
Patch0:         x2goclient-krb5.patch
# ensure RPM_LD_FLAGS/RPM_OPT_FLAGS are used
# https://bugzilla.redhat.com/show_bug.cgi?id=1306463
Patch2:         x2goclient-optflags.patch

BuildRequires(pre): rpm-build-apache2
BuildRequires:  gcc-c++
BuildRequires:  libcups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libssh-devel
BuildRequires:  libXpm-devel
BuildRequires:  man
BuildRequires:  libldap-devel
BuildRequires:  qt4-devel
BuildRequires:  qtbrowserplugin-static
BuildRequires:  libX11-devel
BuildRequires:  libssl-devel
BuildRequires:  perl-base
BuildRequires:  perl-Proc-Simple
BuildRequires:  perl-Term-ReadPassword
BuildRequires:  zlib-devel
Requires:       icon-theme-hicolor
Requires:       nx-libs >= 3.5.0.31
Requires:       nxproxy >= 3.5.0.31
# For GSSAPI authenticated connections
Requires:       openssh-clients
# For local folder sharing and printing
Requires:       openssh-server

%description
X2Go is a server-based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client-side mass storage mounting support
- client-side printing support
- audio support
- authentication by smartcard and USB stick

X2Go Client is a graphical client (Qt4) for the X2Go system.
You can use it to connect to running sessions and start new sessions.


%package -n x2goplugin
Summary:        X2Go Client (Qt4) as browser plugin
Group:          Communications
Requires:       browser-plugins-npapi
Requires:       nx-libs
# For GSSAPI authenticated connections
Requires:       openssh-clients
# For local folder sharing and printing
Requires:       openssh-server

%description -n x2goplugin
X2Go is a server-based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client-side mass storage mounting support
- client-side printing support
- audio support
- authentication by smartcard and USB stick

X2Go Client is a graphical client (qt4) for the X2Go system.
You can use it to connect to running sessions and start new sessions.

This package provides X2Go Client as QtBrowser-based Mozilla plugin.


%package -n x2goplugin-provider
Summary:        Provide X2Go Plugin via Apache webserver
Group:          Communications
Requires:       httpd

%description -n x2goplugin-provider
X2Go is a server-based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client-side mass storage mounting support
- client-side printing support
- audio support
- authentication by smartcard and USB stick

This package provides an example configuration for providing
the X2Go Plugin via an Apache webserver.


%prep
%setup -q
%patch0 -p1
%patch2 -p1
# Fix up install issues
sed -i -e 's/-o root -g root//' Makefile
sed -i -e '/^MOZPLUGDIR=/s/lib/%{_lib}/' Makefile
# Use system qtbrowserplugin
sed -i -e '/CFGPLUGIN/aTEMPLATE=lib' x2goclient.pro
sed -i -e '/^LIBS /s/$/ -ldl/' x2goclient.pro
sed -i -e 's/include.*qtbrowserplugin.pri)/LIBS += -lqtbrowserplugin/' x2goclient.pro
find -name qtbrowserplugin\* -delete

%build
export PATH=%{_qt4_bindir}:$PATH
%make_build

%install
%makeinstall_std PREFIX=%_prefix
desktop-file-validate %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_sysconfdir/httpd/conf.d
ln -s ../../x2go/x2goplugin-apache.conf %buildroot%_sysconfdir/httpd/conf.d/x2goplugin-provider.conf

%files
%doc AUTHORS COPYING LICENSE 
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/%name/
%_man1dir/%name.1*

%files -n x2goplugin
%doc AUTHORS COPYING LICENSE 
%_libdir/mozilla/plugins/libx2goplugin.so

%files -n x2goplugin-provider
%doc AUTHORS COPYING LICENSE 
%_sysconfdir/httpd/conf.d/x2goplugin-provider.conf
%dir %_sysconfdir/x2go
%dir %_sysconfdir/x2go/plugin-provider
%config(noreplace) %_sysconfdir/x2go/plugin-provider/x2goplugin.html
%config(noreplace) %_sysconfdir/x2go/x2goplugin-apache.conf
%_datadir/x2go/

%changelog
* Tue Apr 10 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.1.1-alt2
- Use nx-libs.

* Thu Feb 22 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.1.1-alt1
- New version.
- Return to old nx.

* Wed Feb 07 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.1.0-alt2
- Use nxproxy-x2go

* Mon Nov 06 2017 Andrey Cherepanov <cas@altlinux.org> 4.1.1.0-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 4.1.0.1-alt1
- New version

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 4.1.0.0-alt2
- New version

* Fri Aug 04 2017 Andrey Cherepanov <cas@altlinux.org> 4.0.5.0-alt2
- Initial build in Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.5.0-alt1_4
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 4.0.5.0-alt1_3
- update to new release by fcimport

* Mon Nov 10 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.3.0-alt1_1
- new version

