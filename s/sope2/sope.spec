%def_without sqlite3
%def_without oracle_support
%define sope_makeflags %nil
%define sope_version 4.9
%define sbjson_major_version 2
%define module_name ngobjweb

Summary:      SOPE is an extensive set of frameworks which form a complete Web application server environment
Name:         sope2
Version:      2.3.10
Release:      alt2
License:      GPL
URL:          http://sogo.nu/
Group:        Development/Objective-C
Packager:     Andrey Cherepanov <cas@altlinux.org>

Source:       SOPE-%version.tar.gz
Patch:	      %name-%version-%release.patch

BuildRequires(pre): gnustep-make-devel 
BuildRequires(pre): rpm-build-apache2
BuildRequires: gcc-objc
BuildRequires: gnustep-base-devel
BuildRequires: postgresql-devel
BuildRequires: libffi-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgmp-devel
BuildRequires: libgnutls-devel
BuildRequires: libicu-devel
BuildRequires: libldap-devel
BuildRequires: libmysqlclient-devel
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: apache2-devel
BuildRequires: libapr1-devel
BuildRequires: /proc

Conflicts: sope >= 3.0.0

%description
SOPE is an extensive set of frameworks which form a complete Web
application server environment. Besides the Apple WebObjects compatible
appserver extended with Zope concepts, it contains a large set of
reusable classes: XML processing (SAX, DOM, XML-RPC), MIME/IMAP4
processing, LDAP connectivity, RDBMS connectivity, and iCalendar
parsing.

%package xml
Summary:      SOPE libraries for XML processing
Group:        Development/Objective-C
Conflicts: sope-xml >= 3.0.0

%description xml
The SOPE libraries for XML processing contain:

  * a SAX2 Implementation for Objective-C
  * an attempt to implement DOM on top of SaxObjC
  * an XML-RPC implementation (without a transport layer)

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package xml-devel
Summary:      Development files for the SOPE XML libraries
Group:        Development/Objective-C
Requires:     %name-xml libxml2-devel
Conflicts: sope-xml-devel >= 3.0.0

%description xml-devel
This package contains the development files of the SOPE XML libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package sbjson
Summary:      JSON framework
Group:        Development/Objective-C
Conflicts: sope-sbjson >= 3.0.0

%description sbjson
The SBJson library is a high performance JSON library in Objective-C.

Project homepage is: http://code.google.com/p/json-framework/

%package sbjson-devel
Summary:      JSON framework (devel)
Group:        Development/Objective-C
Conflicts: sope-sbjson-devel >= 3.0.0

%description sbjson-devel
The SBJson library is a high performance JSON library in Objective-C.

Those are the files required for development.

Project homepage is: http://code.google.com/p/json-framework/

%package core
Summary:      Core libraries of the SOPE application server
Group:        Development/Objective-C
Requires:     %name-xml
Conflicts: sope-core >= 3.0.0

%description core
The SOPE core libraries contain:

  * various Foundation extensions
  * a java.io like stream and socket library

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package core-devel
Summary:      Development files for the SOPE core libraries
Group:        Development/Objective-C
Requires:     %name-core
Conflicts: sope-core-devel >= 3.0.0

%description core-devel
This package contains the header files for the SOPE core
libraries,  which are part of the SOPE application server framework.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package mime
Summary:      SOPE libraries for MIME processing
Group:        Development/Objective-C
Requires:     %name-core %name-xml
Conflicts: sope-mime >= 3.0.0

%description mime
The SOPE libraries for MIME processing contain:

  * classes for processing MIME entities
  * a full IMAP4 implementation
  * prototypical POP3 and SMTP processor

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package mime-devel
Summary:      Development files for the SOPE MIME libraries
Group:        Development/Objective-C
Requires:     %name-mime
Conflicts: sope-mime-devel >= 3.0.0

%description mime-devel
This package contains the development files of the SOPE
MIME libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package appserver
Summary:      SOPE application server libraries
Group:        Development/Objective-C
Requires:     %name-xml %name-core %name-mime
Conflicts: sope-appserver >= 3.0.0

%description appserver
The SOPE application server libraries provide:

  * template rendering engine, lots of dynamic elements
  * HTTP client/server
  * XML-RPC client
  * WebDAV server framework
  * session management
  * scripting extensions for Foundation, JavaScript bridge
  * DOM tree rendering library

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package appserver-devel
Summary:      Development files for the SOPE application server libraries
Group:        Development/Objective-C
Requires:     %name-appserver
Conflicts: sope-appserver-devel >= 3.0.0

%description appserver-devel
This package contains the development files for the SOPE application
server libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package ldap
Summary:      SOPE libraries for LDAP access
Group:        Development/Objective-C
Requires:     %name-core %name-xml
Conflicts: sope-ldap >= 3.0.0

%description ldap
The SOPE libraries for LDAP access contain an Objective-C wrapper for
LDAP directory services.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package ldap-devel
Summary:      Development files for the SOPE LDAP libraries
Group:        Development/Objective-C
Requires:     %name-ldap
Conflicts: sope-ldap-devel >= 3.0.0

%description ldap-devel
This package contains the development files of the SOPE
LDAP libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package gdl1
Summary:      GNUstep database libraries for SOPE
Group:        Development/Objective-C
Requires:     %name-core %name-xml
Conflicts: sope-gdl1 >= 3.0.0

%description gdl1
This package contains a fork of the GNUstep database libraries used
by the SOPE application server (excluding GDLContentStore).

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package gdl1-postgresql
Summary:      PostgreSQL connector for SOPE's fork of the GNUstep database environment
Group:        Development/Objective-C
Requires:     %name-gdl1 
#Requires:    postgresql-libs
Conflicts: sope-gdl1-postgresql >= 3.0.0

%description gdl1-postgresql
This package contains the PostgreSQL connector for SOPE's fork of the
GNUstep database libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%if_with oracle_support
%package gdl1-oracle
Summary:      Oracle connector for SOPE's fork of the GNUstep database environment
Group:        Development/Objective-C
Requires:     %name-gdl1
#Requires:    oracle-instantclient-basic
Conflicts: sope-gdl1-oracle >= 3.0.0

%description gdl1-oracle
This package contains the Oracle connector for SOPE's fork of the
GNUstep database libraries.
%endif

%package gdl1-mysql
Summary:      MySQL connector for SOPE's fork of the GNUstep database environment
Group:        Development/Objective-C
Requires:     %name-gdl1
Conflicts: sope-gdl1-mysql >= 3.0.0

%description gdl1-mysql
This package contains the MySQL connector for SOPE's fork of the
GNUstep database libraries.

%if_with sqlite3
%package gdl1-sqlite3
Summary:      SQLite3 connector for SOPE's fork of the GNUstep database environment
Group:        Development/Objective-C
Requires:     %name-gdl1
Conflicts: sope-gdl1-sqlite3 >= 3.0.0

%description gdl1-sqlite3
This package contains the SQLite3 connector for SOPE's fork of the
GNUstep database libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.
%endif

%package gdl1-devel
Summary:      Development files for the GNUstep database libraries
Group:        Development/Objective-C
Requires:     %name-gdl1
Conflicts: sope-gdl1-devel >= 3.0.0

%description gdl1-devel
This package contains the header files for SOPE's fork of the GNUstep
database libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package -n apache2-mod_ngobjweb-sope2
Summary:      mod_ngobjweb module for Apache2
Group:        System/Servers
Conflicts: apache2-mod_ngobjweb >= 3.0.0

%description -n apache2-mod_ngobjweb-sope2
Enables apache2 to handle HTTP requests for the
OpenGroupware.org application server.

%prep
%setup -q -n SOPE2
%patch -p1

%build
%ifarch x86_64
  ORACLELIB_PATH="%_libdir/oracle/11.2/client64/lib/"
%else
  ORACLELIB_PATH="%_libdir/oracle/11.2/client/lib/"
%endif

. /usr/share/GNUstep/Makefiles/GNUstep.sh
./configure --with-gnustep

make %{sope_makeflags} apr=/usr/bin/apr-1-config apxs=%apache2_apxs apu=/usr/bin/apu-1-config

pushd sope-gdl1/MySQL
make LDFLAGS="-L%_libdir/mysql" %{sope_makeflags}
popd

%if_with oracle_support
pushd Oracle8
make LDFLAGS="-L$ORACLELIB_PATH" %{sope_makeflags}
popd
%endif


%install
install -d %buildroot%apache2_libexecdir
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM %{sope_makeflags} apxs="%apache2_apxs -S LIBEXECDIR=%buildroot%apache2_libexecdir"

pushd sope-gdl1/MySQL
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM %{sope_makeflags}
popd

%if_with oracle_support
pushd Oracle8
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM %{sope_makeflags}
popd
%endif

rm -f  %buildroot%_bindir/otest
rm -fr %buildroot%_libdir/GNUstep/GDLAdaptors-%{sope_version}/SQLite3.gdladaptor

# Fix path to NGObjWeb in sope-appserver
mkdir -p %buildroot%_datadir/sope-%{sope_version}
mv %buildroot%_libdir/GNUstep/Resources/NGObjWeb %buildroot%_datadir/sope-%{sope_version}/ngobjweb

install -d %buildroot%apache2_mods_available
echo "LoadModule ngobjweb_module %apache2_libexecdir/mod_ngobjweb.so" > %buildroot%apache2_mods_available/%module_name.load
#install -Dpm644 %module_name.conf %buildroot%apache2_mods_available/%module_name.conf
install -d %buildroot%apache2_mods_start
echo "%module_name=yes" > %buildroot%apache2_mods_start/100-%module_name.conf

%files xml
%_libdir/libDOM*.so.%{sope_version}*
%_libdir/libSaxObjC*.so.%{sope_version}*
%_libdir/libXmlRpc*.so.%{sope_version}*
%_libdir/GNUstep/SaxDrivers-%{sope_version}

%files xml-devel
%_includedir/DOM
%_includedir/SaxObjC
%_includedir/XmlRpc
%_libdir/libDOM*.so
%_libdir/libSaxObjC*.so
%_libdir/libXmlRpc*.so

%files sbjson
%_libdir/libSBJson.so.%{sbjson_major_version}*

%files sbjson-devel
%_includedir/SBJson
%_libdir/libSBJson.so

%files core
%_libdir/libEOControl*.so.%{sope_version}*
%_libdir/libNGExtensions*.so.%{sope_version}*
%_libdir/libNGStreams*.so.%{sope_version}*

%files core-devel
%_includedir/EOControl
%_includedir/NGExtensions
%_includedir/NGStreams
%_libdir/libEOControl*.so
%_libdir/libNGExtensions*.so
%_libdir/libNGStreams*.so

%files mime
%_libdir/libNGMime*.so.%{sope_version}*

%files mime-devel
%_includedir/NGImap4
%_includedir/NGMail
%_includedir/NGMime
%_libdir/libNGMime*.so

%files appserver
%_libdir/libNGObjWeb*.so.%{sope_version}*
%_libdir/libWEExtensions*.so.%{sope_version}*
%_libdir/libWOExtensions*.so.%{sope_version}*
#_libdir/GNUstep/Resources/NGObjWeb/*
%_datadir/sope-%{sope_version}/ngobjweb
%_libdir/GNUstep/SoProducts-%{sope_version}
%_libdir/GNUstep/WOxElemBuilders-%{sope_version}

%files appserver-devel
%_bindir/wod
%_includedir/NGHttp
%_includedir/NGObjWeb
%_includedir/WEExtensions
%_includedir/WOExtensions
%_libdir/libNGObjWeb*.so
%_libdir/libWEExtensions*.so
%_libdir/libWOExtensions*.so
%_datadir/GNUstep/Makefiles

%files ldap
%_libdir/libNGLdap*.so.%{sope_version}*

%files ldap-devel
%_includedir/NGLdap
%_libdir/libNGLdap*.so

%files gdl1
%_bindir/connect-EOAdaptor
%_bindir/load-EOAdaptor
%_libdir/libGDLAccess*.so.%{sope_version}*

%files gdl1-postgresql
%_libdir/GNUstep/GDLAdaptors-%{sope_version}/PostgreSQL.gdladaptor

%if_with oracle_support
%files gdl1-oracle
%_libdir/GNUstep/GDLAdaptors-%{sope_version}/Oracle8.gdladaptor
%endif

%files gdl1-mysql
%_libdir/GNUstep/GDLAdaptors-%{sope_version}/MySQL.gdladaptor

%if_with sqlite3
%files gdl1-sqlite3
%_libdir/GNUstep/GDLAdaptors-%{sope_version}/SQLite3.gdladaptor
%endif

%files gdl1-devel
%_includedir/GDLAccess
%_libdir/libGDLAccess*.so

%files -n apache2-mod_ngobjweb-sope2
%apache2_libexecdir/*.so
#%config(noreplace) %apache2_mods_available/%module_name.conf
%config            %apache2_mods_available/%module_name.load
%config            %apache2_mods_start/100-%module_name.conf


%post -n apache2-mod_ngobjweb-sope2
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/%module_name.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
        service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
        echo "To use %module_name check configuration and start %apache2_dname service."
    echo
    fi
else
    echo "Apache2 %module_name module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with '%module_name=no' lines."
    echo
fi

%preun -n apache2-mod_ngobjweb-sope2
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/%module_name.load ] && %apache2_sbindir/a2dismod %module_name 2>&1 >/dev/null ||:
fi


%postun -n apache2-mod_ngobjweb-sope2
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
        service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
        echo "To complete %module_name uninstalling check configuration and restart %apache2_dname service."
        echo
    fi
fi


%changelog
* Fri Apr 29 2016 Sergey Alembekov <rt@altlinux.ru> 2.3.10-alt2
- rebuild with apache-2.4

* Tue Apr 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.10-alt1
- New version
- Rename package to sope2
- Fix unowned directory

* Tue Jan 26 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.7-alt1
- New version

* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.6-alt1
- New version

* Tue Jan 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- New version

* Mon Nov 30 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.3-alt1
- Inital build in Sisyphus
- Build apache2-mod_ngobjweb
