%def_with openchange
%define sogo_user _sogo

Summary:      SOGo is a very fast and scalable modern collaboration suite (groupware)
Name:         sogo
Version:      2.3.6
Release:      alt1

License:      GPL
URL:          http://www.inverse.ca/contributions/sogo.html
# VCS:        https://github.com/inverse-inc/sogo
Group:        Communications
Packager:     Andrey Cherepanov <cas@altlinux.org>

Source:       SOGo-%version.tar.gz
Source1:      sogo.init
Patch:        %name-%version-%release.patch

BuildPreReq:   gnustep-make-devel rpm-build-apache2
BuildRequires: gcc-objc
BuildRequires: gnustep-base-devel
BuildRequires: sope-appserver-devel sope-core-devel sope-ldap-devel sope-mime-devel sope-xml-devel sope-gdl1-devel sope-sbjson-devel
BuildRequires: libcurl-devel
BuildRequires: libffi-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgmp-devel
BuildRequires: libgnutls-devel
BuildRequires: libicu-devel
BuildRequires: liblasso-devel
BuildRequires: libmemcached-devel
BuildRequires: libnanomsg-devel
BuildRequires: libobjc-devel
BuildRequires: libwbxml-devel
BuildRequires: openchange-devel
BuildRequires: zlib-devel
BuildRequires: python-module-samba-DC

Requires:      stmpclean
Requires:      zip

%filter_from_requires /^\/usr\/%_lib\/samba-dc\/lib/d
%{!?sogo_major_version: %global sogo_major_version %(/bin/echo %version | /bin/cut -f 1 -d .)}

%description
SOGo is a groupware server built around OpenGroupware.org (OGo) and
the SOPE application server.  It focuses on scalability.

The Inverse edition of this project has many feature enhancements:
- CalDAV and GroupDAV compliance
- full handling of vCard as well as vCalendar/iCalendar formats
- support for folder sharing and ACLs

The Web interface has been rewritten in an AJAX fashion to provided a
faster UI for the users, consistency in look and feel with the Mozilla
applications, and to reduce the load of the transactions on the server.

%package -n task-sogo
Summary: SOGo is a groupware server
Group: System/Servers
BuildArch: noarch
Requires: sogo
Requires: sogo-activesync
Requires: sogo-tool
Requires: sope-cards
Requires: apache2-base
Requires: apache2-mod_ngobjweb
Requires: memcached 
%if_with openchange
Requires: %name-openchange-backend
Requires: openchange-server
Requires: openchange-ocsmanager
Requires: openchange-rpcproxy
%endif

%description -n task-sogo
SOGo is a groupware server built around OpenGroupware.org (OGo) and
the SOPE application server.  It focuses on scalability.

The Inverse edition of this project has many feature enhancements:
- CalDAV and GroupDAV compliance
- full handling of vCard as well as vCalendar/iCalendar formats
- support for folder sharing and ACLs

The Web interface has been rewritten in an AJAX fashion to provided a
faster UI for the users, consistency in look and feel with the Mozilla
applications, and to reduce the load of the transactions on the server.

It supports MAPI access for Microsoft Outlook.

See http://altlinux.org/SOGo for more information about deployment and
configuration.

%package tool
Summary:      Command-line toolsuite for SOGo
Group:        Communications
Requires:     sogo = %version-%release

%description tool
Administrative tool for SOGo that provides the following internal commands:
  backup          -- backup user folders
  restore         -- restore user folders
  remove-doubles  -- remove duplicate contacts from the user addressbooks
  check-doubles   -- list user addressbooks with duplicate contacts

%package slapd-sockd
Summary:      SOGo backend for slapd and back-sock
Group:        Communications

%description slapd-sockd
SOGo backend for slapd and back-sock, enabling access to private
addressbooks via LDAP.

%package ealarms-notify
Summary:      SOGo utility for executing email alarms
Group:        Communications

%description ealarms-notify
SOGo utility executed each minute via a cronjob for executing email
alarms.

%package activesync
Summary:      SOGo module to handle ActiveSync requests
Group:        Communications
Requires:     sogo = %version-%release

%description activesync
SOGo module to handle ActiveSync requests

%package devel
Summary:      Development headers and libraries for SOGo
Group:        Development/Objective-C

%description devel
Development headers and libraries for SOGo. Needed to create modules.

%package -n sope-gdl1-contentstore
Summary:      Storage backend for folder abstraction.
Group:        Development/Objective-C
Requires:     sope-gdl1

%description -n sope-gdl1-contentstore
The storage backend implements the "low level" folder abstraction, which
is basically an arbitary "BLOB" containing some document.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package -n sope-gdl1-contentstore-devel
Summary:      Development files for the GNUstep database libraries
Group:        Development/Objective-C
Requires:     sope-gdl1

%description -n sope-gdl1-contentstore-devel
This package contains the header files for SOPE's GDLContentStore
library.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package -n sope-cards
Summary:      SOPE versit parsing library for iCal and VCard formats
Group:        Development/Objective-C

%description -n sope-cards
SOPE versit parsing library for iCal and VCard formats

%package -n sope-cards-devel
Summary:      SOPE versit parsing library for iCal and VCard formats
Group:        Development/Objective-C
Requires:     sope-cards

%description -n sope-cards-devel
SOPE versit parsing library for iCal and VCard formats

%if_with openchange
%package openchange-backend
Summary:      SOGo backend for OpenChange
Group:        Communications
Requires:     samba-DC-libs

%description openchange-backend
SOGo backend for OpenChange
%endif

%prep
%setup -q -n SOGo-%version
%patch -p1

%build
. /usr/share/GNUstep/Makefiles/GNUstep.sh
./configure \
            --enable-saml2 
#           --enable-ldap-config

%make_build CC="cc" LDFLAGS="$ldflags" messages=yes

# OpenChange
%if_with openchange
pushd OpenChange
subst 's@-Wall@-Wall -fobjc-exceptions@' GNUmakefile
export LD_LIBRARY_PATH=../SOPE/NGCards/obj:../SOPE/GDLContentStore/obj
make GNUSTEP_INSTALLATION_DOMAIN=SYSTEM CC="cc" LDFLAGS="$ldflags" messages=yes
popd
%endif

%install
export QA_SKIP_BUILD_ROOT=1

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM 

install -d %buildroot/etc/sysconfig
install -d %buildroot/var/lib/sogo
install -d %buildroot/var/log/sogo
install -d %buildroot/var/run/sogo
install -d %buildroot/var/spool/sogo

install -d -m 750 %buildroot/etc/sogo
install -D -m 640 Scripts/sogo.conf %buildroot/etc/sogo/sogo.conf

# Apache2 configuration
install -Dm0644 -p Apache/SOGo.conf %buildroot%apache2_sites_available/SOGo.conf
subst "s@/lib/@/%_lib/@g" %buildroot%apache2_sites_available/SOGo.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/SOGo.conf

install -Dm 600 Scripts/sogo.cron %buildroot/etc/cron.d/sogo
subst 's, sogo, %sogo_user,g' %buildroot/etc/cron.d/sogo
install -Dm 755 Scripts/tmpwatch %buildroot/etc/cron.daily/sogo-tmpwatch
install -D      Scripts/logrotate %buildroot%_logrotatedir/sogo
install -Dm 644 Scripts/sogo-systemd-redhat %buildroot%_unitdir/sogo.service
subst "s/^User=.*/User=%sogo_user/" %buildroot%_unitdir/sogo.service
install -Dm 644 Scripts/sogo-systemd.conf %buildroot%_tmpfilesdir/sogo.conf
subst "s/ sogo/ %sogo_user/g" %buildroot%_tmpfilesdir/sogo.conf
install -Dm 755 %SOURCE1 %buildroot%_initdir/sogo

cp Scripts/sogo-default %buildroot/etc/sysconfig/sogo
echo "USER=%sogo_user" >> %buildroot/etc/sysconfig/sogo

rm -rf %buildroot%_bindir/test_quick_extract

export LD_LIBRARY_PATH=%buildroot%_libdir

# OpenChange
%if_with openchange
pushd OpenChange
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM
popd
%endif

# ActiveSync
pushd ActiveSync
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM 
install -Dm0644 LICENSE %buildroot%_defaultdocdir/sogo-activesync-%version/LICENSE
install -Dm0644 README  %buildroot%_defaultdocdir/sogo-activesync-%version/README
popd

%files
%doc ChangeLog NEWS Scripts/*sh Scripts/updates.php Apache/SOGo-apple-ab.conf
%config(noreplace) %attr(0640, root, %sogo_user) %_sysconfdir/sogo/sogo.conf
%config(noreplace) %_logrotatedir/sogo
%config(noreplace) %_sysconfdir/cron.d/sogo
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf
%config(noreplace) %_sysconfdir/sysconfig/sogo
%_unitdir/sogo.service
%_tmpfilesdir/sogo.conf
%_initdir/sogo
%_sysconfdir/cron.daily/sogo-tmpwatch
%dir %attr(0700, %sogo_user, %sogo_user) %_var/lib/sogo
%dir %attr(0700, %sogo_user, %sogo_user) %_logdir/sogo
%dir %attr(0755, %sogo_user, %sogo_user) %_runtimedir/sogo
%dir %attr(0700, %sogo_user, %sogo_user) %_spooldir/sogo
%dir %attr(0750, root, %sogo_user) %_sysconfdir/sogo
%_sbindir/sogod
%_libdir/sogo/libSOGo.so.*
%_libdir/sogo/libSOGoUI.so.*
%_libdir/GNUstep/SOGo/AdministrationUI.SOGo
%_libdir/GNUstep/SOGo/Appointments.SOGo
%_libdir/GNUstep/SOGo/CommonUI.SOGo
%_libdir/GNUstep/SOGo/Contacts.SOGo
%_libdir/GNUstep/SOGo/ContactsUI.SOGo
%_libdir/GNUstep/SOGo/MailPartViewers.SOGo
%_libdir/GNUstep/SOGo/Mailer.SOGo
%_libdir/GNUstep/SOGo/MailerUI.SOGo
%_libdir/GNUstep/SOGo/MainUI.SOGo
%_libdir/GNUstep/SOGo/PreferencesUI.SOGo
%_libdir/GNUstep/SOGo/SchedulerUI.SOGo
%_libdir/GNUstep/Frameworks/SOGo.framework/Resources
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/sogo/libSOGo.so.*
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/Resources
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/Current
%_libdir/GNUstep/SOGo/Templates
%_libdir/GNUstep/SOGo/WebServerResources
%_libdir/GNUstep/OCSTypeModels
%_libdir/GNUstep/WOxElemBuilders-*

%files -n sogo-tool
%{_sbindir}/sogo-tool

%files -n sogo-ealarms-notify
%{_sbindir}/sogo-ealarms-notify

%files -n sogo-slapd-sockd
%{_sbindir}/sogo-slapd-sockd

%files -n sogo-activesync
%doc %_defaultdocdir/sogo-activesync-%version
%_libdir/GNUstep/SOGo/ActiveSync.SOGo

%files -n sogo-devel
%_includedir/SOGo
%_includedir/SOGoUI
%_libdir/sogo/libSOGo.so
%_libdir/sogo/libSOGoUI.so
%_libdir/GNUstep/Frameworks/SOGo.framework/Headers
%_libdir/GNUstep/Frameworks/SOGo.framework/sogo/libSOGo.so
%_libdir/GNUstep/Frameworks/SOGo.framework/sogo/SOGo
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/Headers
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/sogo/libSOGo.so
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/sogo/SOGo

%files -n sope-gdl1-contentstore
%_libdir/sogo/libGDLContentStore*.so.*

%files -n sope-gdl1-contentstore-devel
%_includedir/GDLContentStore
%_libdir/sogo/libGDLContentStore*.so

%files -n sope-cards
%_libdir/sogo/libNGCards.so.*
%_libdir/GNUstep/SaxDrivers-*
%_libdir/GNUstep/SaxMappings
%_libdir/GNUstep/Libraries/Resources/NGCards

%files -n sope-cards-devel
%_includedir/NGCards
%_libdir/sogo/libNGCards.so

%if_with openchange
%files openchange-backend
%_libdir/GNUstep/SOGo/*.MAPIStore
%_libdir/mapistore_backends/*
%endif

%files -n task-sogo

%pre
if ! id %sogo_user >& /dev/null; then
  /usr/sbin/useradd -d %{_var}/lib/sogo -c "SOGo daemon" -s /sbin/nologin -M -r %sogo_user
fi

%post
%post_service sogo

%preun
%preun_service sogo

%changelog
* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.6-alt1
- New version
- Move memcached requirement to task-sogo

* Tue Jan 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- New version

* Sat Dec 26 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.4-alt2
- Add metapackage task-sogo for completely install SOGo
- Spec cleanup

* Thu Dec 17 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.4-alt1
- New version

* Mon Nov 23 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.3-alt1
- Initial build in Sisyphus (spec is based on upstream spec file)

