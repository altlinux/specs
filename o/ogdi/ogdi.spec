Name: ogdi
Version: 3.2.0
Release: alt1.beta2.1
Summary: Open Geographic Datastore Interface
Group: Sciences/Geosciences
License: BSD
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://ogdi.sourceforge.net/
Source0: http://dl.sourceforge.net/ogdi/%name-%version.beta2.tar.gz
Source1: http://ogdi.sourceforge.net/ogdi.pdf

BuildRequires: libunixODBC-devel zlib-devel
BuildRequires: libexpat-devel libproj-devel tcl-devel

%description
OGDI is the Open Geographic Datastore Interface. OGDI is an
application programming interface (API) that uses a standardized
access methods to work in conjunction with GIS software packages (the
application) and various geospatial data products. OGDI uses a
client/server architecture to facilitate the dissemination of
geospatial data products over any TCP/IP network, and a
driver-oriented approach to facilitate access to several geospatial
data products/formats.

%package devel
Summary: OGDI header files and documentation
Group: Development/Other
Requires: %name = %version-%release
Requires: pkgconfig
Requires: zlib-devel libexpat-devel libproj-devel

%description devel
OGDI header files and developer's documentation.

%package odbc
Summary: ODBC driver for OGDI
Group: System/Libraries
Requires: %name = %version-%release

%description odbc
ODBC driver for OGDI.

%package tcl
Summary: TCL wrapper for OGDI
Group: System/Libraries
Requires: %name = %version-%release

%description tcl
TCL wrapper for OGDI.

%prep
%setup -q -n %name-%version.beta2

# include documentation
cp -p %SOURCE1 .

%build
TOPDIR=`pwd`; TARGET=Linux; export TOPDIR TARGET
INST_LIB=%_libdir/;export INST_LIB
export CFG=debug # for -g

%add_optflags -I$PWD/proj
# do not compile with ssp. it will trigger internal bugs (to_fix_upstream)
OPT_FLAGS=`echo %optflags|sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//g'`
export CFLAGS="$OPT_FLAGS -fPIC -DPIC -DDONT_TD_VOID -DUSE_TERMIO"
%configure \
        --with-binconfigs \
        --with-expat \
        --with-proj \
        --with-zlib

# WARNING !!!
# using %{?_smp_mflags} may break build
make

# build tcl interface
make -C ogdi/tcl_interface \
          TCL_LINKLIB="-ltcl"

# build contributions
make -C contrib/gdal

# build odbc drivers
ODBC_LINKLIB="-lodbc"
make -C ogdi/attr_driver/odbc \
          ODBC_LINKLIB="-lodbc"

%install


# export env
TOPDIR=`pwd`; TARGET=Linux; export TOPDIR TARGET

make install \
        INST_INCLUDE=%buildroot%_includedir/%name \
        INST_LIB=%buildroot%_libdir \
        INST_BIN=%buildroot%_bindir

# install plugins olso
make install -C ogdi/tcl_interface \
        INST_LIB=%buildroot%_libdir
make install -C contrib/gdal \
        INST_LIB=%buildroot%_libdir
make install -C ogdi/attr_driver/odbc \
        INST_LIB=%buildroot%_libdir

# remove example binary
rm %buildroot%_bindir/example?

# we have multilib ogdi-config
%if "%_lib" == "lib"
%define cpuarch 32
%else
%define cpuarch 64
%endif

# fix file(s) for multilib issue
touch -r ogdi-config.in ogdi-config

# install pkgconfig file and ogdi-config
mkdir -p %buildroot%_libdir/pkgconfig
install -p -m 644 ogdi.pc %buildroot%_libdir/pkgconfig/
install -p -m 755 ogdi-config %buildroot%_bindir/ogdi-config-%cpuarch
# ogdi-config wrapper for multiarch
cat > %buildroot%_bindir/%name-config <<EOF
#!/bin/bash

ARCH=\$(uname -m)
case \$ARCH in
x86_64 | ppc64 | ia64 | s390x | sparc64 | alpha | alphaev6 )
ogdi-config-64 \${*}
;;
*)
ogdi-config-32 \${*}
;;
esac
EOF
chmod 755 %buildroot%_bindir/%name-config
touch -r ogdi-config.in %buildroot%_bindir/%name-config


%files
%doc LICENSE NEWS ChangeLog README
%_bindir/gltpd
%_bindir/ogdi_*
%_libdir/libogdi.so.*
%dir %_libdir/ogdi
%exclude %_libdir/%name/liblodbc.so
%exclude %_libdir/%name/libecs_tcl.so
%_libdir/%name/lib*.so

%files devel
%doc ogdi.pdf
%doc ogdi/examples/example1/example1.c
%doc ogdi/examples/example2/example2.c
%_bindir/%name-config
%_bindir/%name-config-%cpuarch
%_libdir/pkgconfig/%name.pc
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/libogdi.so

%files odbc
%_libdir/%name/liblodbc.so

%files tcl
%_libdir/%name/libecs_tcl.so

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1.beta2.1
- Fixed build

* Sun Dec 12 2010 Ilya Mashkin <oddity@altlinux.ru> 3.2.0-alt1.beta2
- Build for ALT Linux

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-0.14.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-0.13.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May  28 2008 Balint Cristian <rezso@rdsor.ro> - 3.2.0-0.12.beta2
- fix for RHEL4 and RHEL5

* Wed May  28 2008 Balint Cristian <rezso@rdsor.ro> - 3.2.0-0.11.beta2
- fix a spourios permission

* Wed May  28 2008 Balint Cristian <rezso@rdsor.ro> - 3.2.0-0.10.beta2
- new bugfix upstream
- drop all patches, upstream now

* Mon May  26 2008 Balint Cristian <rezso@rdsor.ro> - 3.2.0-0.9.beta1
- fix debuginfo bz#329921

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.2.0-0.8.beta1
- Autorebuild for GCC 4.3

* Wed Jan  9 2008 Balint Cristian <rezso@rdsor.ro> - 3.2.0-0.7.beta1
- fix multilib issue for ogdi-config

* Thu Jan  3 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 3.2.0-0.6.beta1
- Rebuild for new Tcl 8.5

* Thu Mar 01 2007 Balint Cristian <cbalint@redhat.com> 3.2.0-0.5.beta1
- fix fc-6 tag upstream fedora-extras

* Thu Mar 01 2007 Balint Cristian <cbalint@redhat.com> 3.2.0-0.4.beta1
- disable only the hurting flag

* Thu Mar 01 2007 Balint Cristian <cbalint@redhat.com> 3.2.0-0.3.beta1
- disable fedora specific compile flags to avoid internal bugs

* Tue Feb 24 2007 Balint Cristian <cbalint@redhat.com> 3.2.0-0.2.beta1
- rename the release for correct fedora n-v-r
- fix -devel requires

* Tue Feb 24 2007 Balint Cristian <cbalint@redhat.com> 3.2.0.beta1-1
- new upstream release.

* Tue Feb 13 2007 Balint Cristian <cbalint@redhat.com> 3.1.6-5
- matrix.c is Public Domain.

* Tue Feb 13 2007 Balint Cristian <cbalint@redhat.com> 3.1.6-4
- add diff to latest CVS.
- solve matrix algebra license issue from CVS.

* Tue Feb 13 2007 Balint Cristian <cbalint@redhat.com> 3.1.6-3
- _dont_ duplicate any docs, so leave odbc and tcl without.

* Tue Feb 13 2007 Balint Cristian <cbalint@redhat.com> 3.1.6-2
- fix timestamps of source file.
- no need to duplicate the documentation
- fix post install script
- fix odbc lib innclusion

* Mon Feb 12 2007 Balint Cristian <cbalint@redhat.com> 3.1.6-1
- new upstream version.
- drop all patches, now they are upstream.
- remove useless source code cleanup from spec.
- pkgconfig is now autogenerated.

* Mon Feb 12 2007 Balint Cristian <cbalint@redhat.com> 3.1.5-8
- get rid of autoconf, useless.
- fix cp usage in specs.

* Mon Feb 12 2007 Balint Cristian <cbalint@redhat.com> 3.1.5-7
- include soname proposal patch
- cleanup more in specs

* Sun Feb 11 2007 Balint Cristian <cbalint@redhat.com> 3.1.5-6
- massive cleanup in sources.
- use -DUSE_TERMIO flag for linux.
- fix dlopen path.

* Sat Feb 10 2007 Balint Cristian <cbalint@redhat.com> 3.1.5-5
- more minor nits in spec
- pack the examples in devel
- drop tdvoid patch use CFLAGS instead
- patch instead use sed in spec (will try merge mainstream)
- fill requires for pkgconf file

* Sat Feb 10 2007 Balint Cristian <cbalint@redhat.com> 3.1.5-4
- preserves for external doc.

* Fri Feb 09 2007 Balint Cristian <cbalint@redhat.com> 3.1.5-3
- add dlopen path for lib64 too.
- add more docs
- fix export of CFLAGS
- move include files and add pkgconf module

* Fri Feb 09 2007 Balint Cristian <cbalint@redhat.com> 3.1.5-2
- add -soname versioning on shared libs
- remove polish lang from spec
- fix packing of libs
- tcl is plugin dont separate package name

* Wed Feb 08 2007 Balint Cristian <cbalint@redhat.com> 3.1.5-1
- first build for fedora extras
- require -fPIC, at least on x86_64
- odbc compile fix use DONT_TD_VOID
