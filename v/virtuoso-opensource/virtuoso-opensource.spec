
Name: virtuoso-opensource
Version: 6.1.5
Release: alt2
Serial: 2

Group: Databases
Summary: OpenLink Virtuoso Database System Open-Source Edition
Url: http://virtuoso.openlinksw.com/
License: GPLv2

Requires: %name-applications = %version-%release
#Requires: %name-conductor = %version-%release
#Requires: %name-jars = %version-%release

Source0: %name-%version.tar
# FC
Patch1: virtuoso-opensource-6.1.0-extern-iodbc.patch
Patch2: virtuoso-opensource-6.1.0-nodemos_buildfix.patch
Patch3: virtuoso-opensource-6.1.4-no_strip.patch
Patch4: virtuoso-opensource-6.1.2-no_strip.patch
# SuSE
Patch101: virtuoso-wrong-memset.patch
Patch102: rpmlint-fixes.diff
Patch103: isql-buffer-overflow.patch

BuildRequires: glibc-devel libssl-devel bison flex gperf libxml2-devel libiodbc-devel libldap-devel /usr/bin/openssl libwbxml2-devel libexpat-devel


%description
Virtuoso is a scalable cross-platform server that combines SQL/RDF/XML
Data Management with Web Application Server and Web Services Platform
functionality.

Virtuoso is at the core a high performance object-relational SQL
database. As a database, it provides transactions, a smart SQL
compiler, powerful stored procedure language with optional Java and
.Net server side hosting, hot backup, SQL 99 and more. It has all
major data access interfaces, as in ODBC, JDBC, ADO .Net and OLE/DB.

Virtuoso has a built-in web server which can serve dynamic web pages
written in Virtuoso's web page language as well as PHP, ASP .Net and
others. This same web server provides SOAP and REST access to Virtuoso
stored procedures, supporting a broad set of WS protocols such as
WS-Security, WS-Reliable Messaging and others. A BPEL4WS run time is
also available as part of Virtuoso's SOA suite.


%package -n %name-conductor
Summary: Virtuoso open source edition Server Pages
Group: Development/Databases
%description -n %name-conductor
Virtuoso is a scalable cross-platform server that combines SQL/RDF/XML
Data Management with Web Application Server and Web Services Platform
functionality.

%package -n %name-applications
Summary: Virtuoso open source applications
Group: Development/Databases
%description -n %name-applications
Virtuoso is a scalable cross-platform server that combines SQL/RDF/XML
Data Management with Web Application Server and Web Services Platform
functionality.

%package -n %name-jars
Summary: Virtuoso open source jar files
Group: Development/Databases
%description -n %name-jars
Virtuoso is a scalable cross-platform server that combines SQL/RDF/XML
Data Management with Web Application Server and Web Services Platform
functionality.


%prep
%setup -q -n %name-%version
%patch1 -p0 -b .iodbc
%patch2 -p0
%patch3 -p1
#%patch4 -p1
%patch101 -p1
%patch102 -p0
%patch103 -p0
#./autogen.sh
%autoreconf


%build
%configure \
    --with-layout=redhat \
    --disable-static \
    --enable-shared \
    --localstatedir=/var \
    --with-iodbc=%prefix \
    --without-internal-zlib \
    --enable-openssl \
    --disable-imagemagick \
    --disable-all-vads
%make


%install
%make install DESTDIR=%buildroot
mkdir -p %buildroot%_var/lib/virtuoso/{db,vsp}
mkdir -p %buildroot%_libdir/virtuoso/plugins
mkdir -p %buildroot%_datadir/virtuoso/vad
mkdir -p %buildroot%_libdir/virtuoso/hosting
mv %buildroot%_libdir/*.la %buildroot%_libdir/virtuoso/plugins/
cp -f %buildroot%_libdir/virtuoso/plugins/* %buildroot%_libdir/

rm -fr %buildroot%_libdir/*.a
mv %buildroot%_libdir/*.so %buildroot%_libdir/virtuoso/plugins/
mkdir -p %buildroot%_libdir/virtuoso/jars
mv %buildroot%_libdir/jdbc-2.0 %buildroot%_libdir/virtuoso/jars/jdbc2.0
mv %buildroot%_libdir/jdbc-3.0 %buildroot%_libdir/virtuoso/jars/jdbc3.0
mv %buildroot%_libdir/jdbc-4.0 %buildroot%_libdir/virtuoso/jars/jdbc4.0
mv %buildroot%_libdir/jena %buildroot%_libdir/virtuoso/jars/jena
mv %buildroot%_libdir/sesame %buildroot%_libdir/virtuoso/jars/sesame
mkdir -p %buildroot%_sysconfdir/virtuoso
mv %buildroot%_var/lib/virtuoso/db/virtuoso.ini %buildroot%_sysconfdir/virtuoso/


%files -n %name
%doc LICENSE AUTHORS CREDITS ChangeLog NEWS README*
%_bindir/*
#conflicts with unixODBC
%exclude %_bindir/isql
%_sysconfdir/virtuoso/virtuoso.ini
%dir %_libdir/virtuoso
%dir %_libdir/virtuoso/hosting
%dir %_libdir/virtuoso/plugins
%dir %_libdir/virtuoso/jars
%dir %_datadir/virtuoso
%dir %_datadir/virtuoso/vad
%dir %_var/lib/virtuoso
%dir %_var/lib/virtuoso/db
%dir %_var/lib/virtuoso/vsp

#%files -n %name-conductor
#%_var/lib/virtuoso/vsp/*

%files -n %name-applications
%_libdir/virtuoso/plugins/*.so

%files -n %name-jars
%_libdir/virtuoso/jars/*
%_libdir/hibernate/virt_dialect.jar

%changelog
* Thu Jun 07 2012 Sergey V Turchin <zerg@altlinux.org> 2:6.1.5-alt2
- 6.1.5 again; built without aio

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 2:6.1.2-alt5.M60P.1
- built for M60P

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 2:6.1.2-alt6
- fix build requires

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 2:6.1.2-alt4.M60P.1
- built for M60P

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 2:6.1.2-alt5
- built with aio and wbxml

* Fri May 25 2012 Sergey V Turchin <zerg@altlinux.org> 2:6.1.2-alt3.M60P.1
- build for M60P

* Fri May 25 2012 Sergey V Turchin <zerg@altlinux.org> 2:6.1.2-alt4
- downgrade

* Thu Mar 29 2012 Sergey V Turchin <zerg@altlinux.org> 1:6.1.5-alt0.M60P.1
- built for M60P

* Thu Mar 29 2012 Sergey V Turchin <zerg@altlinux.org> 1:6.1.5-alt1
- new version

* Wed Feb 15 2012 Sergey V Turchin <zerg@altlinux.org> 1:6.1.4-alt0.M60P.1
- built for M60P

* Mon Feb 13 2012 Sergey V Turchin <zerg@altlinux.org> 1:6.1.4-alt1
- new version
- update FC and SuSE patches

* Fri Jun 10 2011 Sergey V Turchin <zerg@altlinux.org> 1:6.1.2-alt3
- revert to 6.1.2

* Wed May 04 2011 Sergey V Turchin <zerg@altlinux.org> 6.1.3-alt1
- new version

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt2
- rebuilt with new ssl

* Fri Apr 30 2010 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0.M51.1
- built for M51

* Tue Feb 09 2010 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- new version

* Mon Feb 01 2010 Sergey V Turchin <zerg@altlinux.org> 5.0.12-alt1
- initial specfile

