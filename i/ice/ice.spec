%define major 3.3
Name: ice
Version: %major.1
Release: alt2.2

Summary: Files common to all Ice packages

License: GPLv2
Group: System/Libraries
Url: http://www.zeroc.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# http://www.zeroc.com/download/Ice/%major/Ice-%version.tar.gz
# http://www.zeroc.com/download/Ice/%major/Ice-rpmbuild-%version.tar.gz
Source0: Ice-%version.tar
Source1: Ice-rpmbuild-%version.tar
Patch1: ice-3.3.1-rh-openssl.patch
Patch2: ice-3.3-alt-build.patch
Patch3: ice-3.3-ssl-krb.patch
Patch4: ice-3.3.1-alt-no-dbl-mv.patch
Patch5: ice-3.3.1-alt-gcc4.6.patch

%def_with krb

BuildRequires: bzlib-devel gcc-c++ libdb4_cxx-devel libexpat-devel libssl-devel libmcpp-devel >= 2.7.2 python-devel

%description
Ice is a modern alternative to object middleware such as CORBA or
COM/DCOM/COM+.  It is easy to learn, yet provides a powerful network
infrastructure for demanding technical applications. It features an
object-oriented specification language, easy to use C++, C#, Java,
Python, Ruby, PHP, and Visual Basic mappings, a highly efficient
protocol, asynchronous method invocation and dispatch, dynamic
transport plug-ins, TCP/IP and UDP/IP support, SSL-based security, a
firewall solution, and much more.

%package -n libice
Summary: The base runtime libraries for Ice applications
Group: System/Libraries
Requires: %name = %version-%release
%if_with krb
BuildRequires: openssl-krb-devel
Requires: openssl-krb
Provides: libice-ssl-krb = %version-%release
%endif

%description -n libice
Ice is a modern alternative to object middleware such as CORBA or
COM/DCOM/COM+.  It is easy to learn, yet provides a powerful network
infrastructure for demanding technical applications. It features an
object-oriented specification language, easy to use C++, C#, Java,
Python, Ruby, PHP, and Visual Basic mappings, a highly efficient
protocol, asynchronous method invocation and dispatch, dynamic
transport plug-ins, TCP/IP and UDP/IP support, SSL-based security, a
firewall solution, and much more.

%package -n libice-devel
Summary: Tools, libraries and headers for developing Ice applications in C++
Group: Development/C++
Requires: %name = %version-%release
Requires: ice-devel-utils = %version-%release
%if_with krb
Requires: libice-ssl-krb = %version
Provides: libice-ssl-krb-devel = %version-%release
%endif

%description -n libice-devel
Tools, libraries and headers for developing Ice applications in C++.

%package devel-utils
Summary: Tools for developing Ice applications
Group: Development/Other
Requires: %name = %version-%release

%description devel-utils
Ice is a modern alternative to object middleware such as CORBA or
COM/DCOM/COM+.  It is easy to learn, yet provides a powerful network
infrastructure for demanding technical applications. It features an
object-oriented specification language, easy to use C++, C#, Java,
Python, Ruby, PHP, and Visual Basic mappings, a highly efficient
protocol, asynchronous method invocation and dispatch, dynamic
transport plug-ins, TCP/IP and UDP/IP support, SSL-based security, a
firewall solution, and much more.

%package utils
Summary: Ice utilities and admin tools.
Group: System/Configuration/Other
Requires: %name = %version-%release

%description utils
Admin tools to manage Ice servers (IceGrid, IceStorm, IceBox etc.),
plus various Ice-related utilities.

%package servers
Summary: Ice servers and related files.
Group: System/Servers
Requires: ice-utils = %version-%release
#Requires(pre): shadow-utils
# Requirements for the init.d services
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description servers
Ice servers: glacier2router, icebox, icegridnode, icegridregistry, 
icebox, iceboxnet, icepatch2server and related files.

%prep
%setup -a1 -n Ice-%version
%patch1 -p1
%patch4 -p2
%patch5 -p2

cd cpp
%patch2 -p1
%if_with krb
%patch3 -p1
%endif

sed -i 's|\(\$(CPPFLAGS)\)|\1 -g|g' $(find ./ -name Makefile)

%build
cd cpp
%make_build OPTIMIZE=yes embedded_runpath_prefix="" DB_HOME=%prefix

%install
pushd cpp
%make_install prefix=%buildroot embedded_runpath_prefix="" install
popd

#
# move installed files
#
## dirs
mkdir -p %buildroot/%_prefix
mkdir -p %buildroot%_datadir/Ice-%version
## bins
mv %buildroot/bin %buildroot/%_bindir
## clean libs
mv %buildroot/lib/ImportKey.class %buildroot%_datadir/Ice-%version
## libs
mv %buildroot/%_lib %buildroot%_libdir
## includes
mv %buildroot/include %buildroot%_includedir
## slices
mv %buildroot/slice %buildroot%_datadir/Ice-%version
## scripts
mv %buildroot/config/* %buildroot%_datadir/Ice-%version

rm -rf %buildroot/doc %buildroot/ICE_LICENSE %buildroot/LICENSE
rm -f %buildroot%_libdir/libIceStormService.so

#
# Certificates
#
cp -r certs %buildroot%_datadir/Ice-%version

#
# Config files (for build another parts)
#
mkdir -p %buildroot%_datadir/Ice-%version/config
cp cpp/config/Make.rules.Linux %buildroot%_datadir/Ice-%version/config
cp config/Make.common.rules* %buildroot%_datadir/Ice-%version/config
cp config/PropertyNames.xml %buildroot%_datadir/Ice-%version/config
cp config/IceDevKey.snk %buildroot%_datadir/Ice-%version/config

#
# initrd files (for servers)
#
mkdir -p %buildroot%_sysconfdir
cp Ice-rpmbuild-%version/*.conf %buildroot%_sysconfdir
mkdir -p %buildroot%_initrddir
for i in icegridregistry icegridnode glacier2router
do
    cp Ice-rpmbuild-%version/$i.%_vendor %buildroot%_initrddir/$i
done

%files
%doc CHANGES ICE_LICENSE LICENSE RELEASE_NOTES Ice-rpmbuild-%version/THIRD_PARTY_LICENSE.Linux Ice-rpmbuild-%version/SOURCES.Linux Ice-rpmbuild-%version/README.Linux-RPM
%dir %_datadir/Ice-%version
%_datadir/Ice-%version/slice
%_datadir/Ice-%version/certs
%_datadir/Ice-%version/config

%files -n libice
%_libdir/libFreeze.so.*
%_libdir/libGlacier2.so.*
%_libdir/libIceBox.so.*
%_libdir/libIcePatch2.so.*
%_libdir/libIce.so.*
%_libdir/libIceSSL.so.*
%_libdir/libIceStorm.so.*
%_libdir/libIceUtil.so.*
%_libdir/libSlice.so.*
%_libdir/libIceXML.so.*
%_libdir/libIceGrid.so.*

%files -n libice-devel
%_includedir/*
%_libdir/libFreeze.so
%_libdir/libGlacier2.so
%_libdir/libIceBox.so
%_libdir/libIceGrid.so
%_libdir/libIcePatch2.so
%_libdir/libIce.so
%_libdir/libIceSSL.so
%_libdir/libIceStorm.so
%_libdir/libIceUtil.so
%_libdir/libIceXML.so
%_libdir/libSlice.so

%files devel-utils
%_bindir/slice2*

%files utils
%_bindir/dumpdb
%_bindir/transformdb
%_bindir/iceboxadmin
%_bindir/icepatch2calc
%_bindir/icepatch2client
%_bindir/icestormadmin
%_bindir/icegridadmin
%_bindir/iceca
%_datadir/Ice-%version/ImportKey.class
%attr(755,root,root) %_datadir/Ice-%version/convertssl.py*

%files servers
%_libdir/libIceStormService.so.*
%_bindir/glacier2router
%_bindir/icebox
%_bindir/icegridnode
%_bindir/icegridregistry
%_bindir/icepatch2server
%_bindir/icestormmigrate
%_datadir/Ice-%version/templates.xml
%attr(755,root,root) %_datadir/Ice-%version/upgradeicegrid.py*
%_datadir/Ice-%version/icegrid-slice.3.*.ice.gz
%_initrddir/icegridregistry
%_initrddir/icegridnode
%_initrddir/glacier2router
%config(noreplace) %_sysconfdir/icegridregistry.conf
%config(noreplace) %_sysconfdir/icegridnode.conf
%config(noreplace) %_sysconfdir/glacier2router.conf

%pre servers
getent group ice > /dev/null || groupadd -r ice
getent passwd ice > /dev/null || \
       useradd -r -g ice -d %_localstatedir/ice \
       -s /sbin/nologin -c "Ice Service account" ice
test -d %_localstatedir/ice/icegrid/registry || \
       mkdir -p %_localstatedir/ice/icegrid/registry; chown -R ice.ice %_localstatedir/ice
test -d %_localstatedir/ice/icegrid/node1 || \
       mkdir -p %_localstatedir/ice/icegrid/node1; chown -R ice.ice %_localstatedir/ice
exit 0

%post servers
/sbin/chkconfig --add icegridregistry
/sbin/chkconfig --add icegridnode
/sbin/chkconfig --add glacier2router

%preun servers
if [ $1 = 0 ]; then
        /sbin/service icegridnode stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del icegridnode
        /sbin/service icegridregistry stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del icegridregistry
        /sbin/service glacier2router stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del glacier2router
fi

%postun servers
if [ "$1" -ge "1" ]; then
        /sbin/service icegridnode condrestart >/dev/null 2>&1 || :
        /sbin/service icegridregistry condrestart >/dev/null 2>&1 || :
        /sbin/service glacier2router condrestart >/dev/null 2>&1 || :
fi


%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt2.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3.1-alt2.1.1
- Rebuild with Python-2.7

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt2.1
- Rebuilt for debuginfo

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 3.3.1-alt2
- Fixed build with openssl-1.0, patch from Fedora.

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.1
- Rebuilt with python 2.6

* Sun May 10 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.1-alt1
- Updated to release
- Clean obsoletes ldconfig scripts

* Sun Nov 02 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt9
- Rebuilt with last libdb4 that is libdb4.7 now

* Tue Sep 16 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt8
- Fixed segfault in Slice::Preprocessor::preprocess

* Sat Sep 13 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt7
- Removed unnecessary check at IceSSL for kerberos client principal

* Sat Aug 09 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt6
- Rebuilt with libssl7 at Sisyphus
- Enabled kerberos support

* Tue Jul 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt5
- Fixed install for x86_64 again
 + Moved ImportKey.class from
 + Moved libs from lib64 for x86_64

* Tue Jul 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt4
- Fixed install for x86_64

* Tue Jul 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt3
- Added IceDevKey.snk to config for IceCS

* Mon Jul 07 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt2
- Fixed spec for Sisyphus policy
- Moved all slice2* utilities to ice-devel-utils
- Added cpp/config/Make.rules.Linux to $datadir/Ice-3.3.0/config
- Added vendor specific services scripts (untested!)

* Sun Jul 06 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.3.0-alt1
- Updated to release
- Striped sources to different packages for supported languages

* Sat Jun 28 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.1-alt1.1.eter1
- Fixed SSL with kerberos support
 + KRB5 IceSSL.Cipher indentification potential problem
- Added requirement for openssl-krb and openssl-krb-devel
- Added libice-ssl-krb5 and libice-ssl-krb5-devel providing

* Wed Jun 18 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.1-alt1.1.debug2
- Rebuilt with libssl7

* Sat Feb 09 2008 Grigory Batalov <bga@altlinux.ru> 3.2.1-alt1.1
- Rebuilt with python-2.5.

* Fri Sep 21 2007 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt1
- new version 3.2.1 (with rpmrb script)

* Sat Aug 04 2007 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt2
- fix build on x86_64

* Fri Aug 03 2007 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- initial build to ALT Linux Sisyphus

* Fri Dec 6 2006 ZeroC Staff
- See source distributions or the ZeroC website for more information
  about the changes in this release

