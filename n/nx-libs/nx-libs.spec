%def_with system_locale

Name:    nx-libs
Version: 3.5.99.26.1
Release: alt3.1

Summary: NX X11 protocol compression libraries

Group:   System/Libraries
License: GPLv2+
URL:     https://github.com/ArcticaProject/nx-libs/

# Source0-url: https://github.com/ArcticaProject/nx-libs/archive/%version.tar.gz
Source0: %name-%version.tar
#Source1: Makefile.alt
Source2: patches.etersoft.tar

# riscv64 support (from https://github.com/ArcticaProject/nx-libs/pull/1023)
Patch2: nx-libs-github-pull-1023-riscv64-support.patch
# loongarch64 support (from https://github.com/ArcticaProject/nx-libs/pull/1062)
Patch3: nx-libs-github-pull-1062-loongarch64-support.patch

BuildRequires: gcc-c++
BuildRequires: fontconfig-devel
BuildRequires: gccmakedep
BuildRequires: imake
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXext-devel
BuildRequires: libXfont2-devel
BuildRequires: libXfixes-devel
BuildRequires: libXinerama-devel
BuildRequires: libXpm-devel
BuildRequires: libXrandr-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
BuildRequires: libXmu-devel
BuildRequires: libexpat-devel
BuildRequires: libfontenc-devel
BuildRequires: libfreetype-devel
BuildRequires: libjpeg-devel
BuildRequires: libpixman-devel
BuildRequires: libpng-devel
BuildRequires: libtirpc-devel
BuildRequires: libxml2-devel
BuildRequires: xorg-proto-devel
BuildRequires: zlib-devel
%if "%_vendor" == "alt"
BuildRequires: patchelf
%endif
BuildRequires(pre): rpm-build-python3

Obsoletes: nx < %EVR
Provides:  nx = %EVR
%if_with system_locale
Requires: libX11-locales
%endif

Obsoletes: libXcomp
Provides:  libXcomp = %EVR
Obsoletes: libNX_X11
Provides:  libNX_X11 = %EVR

%description
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network  especially a slow one.

This package provides the core nx-X11 libraries customized for
nxagent/x2goagent.

%package devel
Summary: Header files for development with nx
Group: Development/C
Requires: %name = %EVR
Obsoletes: nx-devel
Provides: nx-devel = %EVR

Obsoletes: libNX_X11-devel
Provides:  libNX_X11-devel = %EVR


%description devel
Header files for development with nx-libs

%package -n nxagent
Group:   Networking/Remote access
Summary: NX agent
# For /usr/share/X11/xkb
Requires: xkeyboard-config
Requires: nx-libs = %EVR

Obsoletes: nxauth < 3.5.99.1
Requires: xorg-font-utils
Requires: xkeyboard-config
Requires: xkbcomp
Requires: fonts-bitmap-misc

%description -n nxagent
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network  especially a slow one.

nxagent is an agent providing NX transport of X sessions. The
application is based on the well-known Xnest server. nxagent  like
Xnest  is an X server for its own clients, and at the same time, an X
client for a system's local X server.

The main scope of nxagent is to eliminate X round-trips or transform
them into asynchronous replies. nxagent works together with nxproxy.
nxproxy itself does not make any effort to minimize round-trips by
itself  this is demanded of nxagent.

Being an X server  nxagent is able to resolve all the property/atoms
related requests locally  ensuring that the most common source of
round-trips are nearly reduced to zero.

%package -n nxproxy
Group:   Networking/Remote access
Summary: NX Proxy
Requires: nx-libs = %EVR

%description -n nxproxy
This package provides the NX proxy (client) binary.


%package -n nxdialog
Group:   Networking/Remote access
Summary:        NX Dialog

%description -n nxdialog
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

This package provides the nxdialog helper script.

%prep
%setup
%patch2 -p1
%patch3 -p1

# Apply all patches from debian/patches
cat debian/patches/series | while read patchfile;do 
	test -e debian/patches/$patchfile && patch -p1 < debian/patches/$patchfile
done

tar -xf %SOURCE2
# Apply etersoft patches
for patchfile in $(ls patches.etersoft/*.patch); do
	test -e $patchfile || exit
	cat $patchfile | sed -e 's|\([ab]/\)nx-libs/|\1|' | patch -p1
done

# remove build cruft that is in Git (also taken from roll-tarball.sh)
rm -Rf nx*/configure nx*/autom4te.cache*
# Install into /usr
sed -i -e 's,/usr/local,/usr,' nx-X11/config/cf/site.def
# Fix FSF address
find -name LICENSE | xargs sed -i \
  -e 's/59 Temple Place/51 Franklin Street/' -e 's/Suite 330/Fifth Floor/' \
  -e 's/MA  02111-1307/MA  02110-1301/'
# Fix source permissions
find -type f -name '*.[hc]' | xargs chmod -x

# Use rpm optflags
sed -i -e 's|-O3|%{optflags}|' nx-X11/config/cf/host.def
sed -i -e 's|-O3|%{optflags}|' nx-X11/config/cf/linux.cf
echo "#define DefaultGcc2Ppc64Opt %optflags" >> nx-X11/config/cf/host.def



%__subst "s:\$(NLSSUBDIR):nls:" nx-X11/Imakefile


# set locale path for ALT Linux
%if_with system_locale
%__subst "s|#define XLocaleDir \$(LIBDIR)/locale|#define XLocaleDir %_datadir/X11/locale|g" nx-X11/config/cf/X11.tmpl
%else
%__subst "s|#define XLocaleDir \$(LIBDIR)/locale|#define XLocaleDir %_datadir/nx/X11/locale|g" nx-X11/config/cf/X11.tmpl
%endif

#cp %SOURCE1 nx-X11


%build
cat >"my_configure" <<'EOF'
#!/bin/sh -x
%configure \
  --disable-selective-werror \
  --disable-strict-compilation \
  "${@}"
EOF
chmod a+x my_configure;
# The RPM macro for the linker flags does not exist on EPEL
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
SHLIBGLOBALSFLAGS="%{__global_ldflags}"
LOCAL_LDFLAGS="%{__global_ldflags}"
CDEBUGFLAGS="%{?__global_cppflags} %{?__global_cflags} %{?optflags}"
IMAKE_DEFINES=''
FORCE_TIRPC='YES'
IMAKE_DEFINES="-DUseTIRPC=${FORCE_TIRPC}"
# TODO: fix parallel build on aarch64/ppc64le
%make_build CONFIGURE="$PWD/my_configure" PREFIX=%{_prefix} LIBDIR=%{_libdir} CDEBUGFLAGS="${CDEBUGFLAGS}" LOCAL_LDFLAGS="${LOCAL_LDFLAGS}" SHLIBGLOBALSFLAGS="${SHLIBGLOBALSFLAGS}" IMAKE_DEFINES="${IMAKE_DEFINES}" || \
    make CONFIGURE="$PWD/my_configure" PREFIX=%{_prefix} LIBDIR=%{_libdir} CDEBUGFLAGS="${CDEBUGFLAGS}" LOCAL_LDFLAGS="${LOCAL_LDFLAGS}" SHLIBGLOBALSFLAGS="${SHLIBGLOBALSFLAGS}" IMAKE_DEFINES="${IMAKE_DEFINES}" || \

%install
make install \
        DESTDIR=%{buildroot} \
        PREFIX=%{_prefix} \
        LIBDIR=%{_libdir} SHLIBDIR=%{_libdir} \
        INSTALL_DIR="install -dm0755" \
        INSTALL_FILE="install -pm0644" \
        INSTALL_PROGRAM="install -pm0755"


# TODO: broken upstream with broken linking and strange shell wrappers
# https://bugs.etersoft.ru/show_bug.cgi?id=14208
#rm -f %buildroot%_libdir/nx/X11/libX11.so*
# lib.req: ERROR: /tmp/.private/lav/nx-libs-buildroot/usr/bin/nxagent: library libNX_X11.so.6 not found
%if "%_vendor" == "alt"
which patchelf 2>/dev/null >/dev/null && patchelf --remove-needed libNX_X11.so.6 %buildroot%_bindir/nxagent
%endif

# Remove static libs (they don't exist on SLES, so using -f here)
rm -f %{buildroot}%{_libdir}/*.a

# Fix permissions on shared libraries
chmod 755  %{buildroot}%{_libdir}/lib*.so*

#Remove extras, GL, and other unneeded headers
rm -r %{buildroot}%{_includedir}/GL
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/XK*.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/*Xv*.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/XRes*.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/XIproto.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/XI.h
rm -r %{buildroot}%{_includedir}/nx-X11/Xtrans

#Remove our shared libraries' .la files before wrapping up the packages
rm -f %{buildroot}%{_libdir}/*.la

#FIXME: leaving nxdialog integration to Ionic
#rm -f %{buildroot}%{_bindir}/nxdialog
#rm -f %{buildroot}%{_datadir}/man/man1/nxdialog.1*
sed -i '1 s/python$/python3/' %{buildroot}%{_bindir}/nxdialog


%if_with system_locale
rm -rf %buildroot%_datadir/X11/locale
%endif

#mkdir -p %buildroot%_datadir/nx/
#install -m644 debian/rgb %buildroot%_datadir/nx/rgb.txt

#cd %buildroot%_libdir
#ln -sf libXcomp.so.3.5.0 libXcomp.so
#ln -sf libXcompext.so.3.5.0 libXcompext.so
#ln -sf libXcompshad.so.3.5.0 libXcompshad.so
#cd -

#mkdir -p %buildroot%_docdir/%name-%version/
#install -m 644 nxcomp/LICENSE %buildroot%_docdir/%name-%version/
#mkdir -p %buildroot%_docdir/%name-%version/nxcomp/
#install -m 644 nxcomp/README %buildroot%_docdir/%name-%version/nxcomp

# Needed for nxagent to find the keymap directory
#mkdir -p %buildroot%_datadir/X11/xkb
#touch %buildroot%_datadir/X11/xkb/keymap.dir

#cp -a nxcomp/VERSION %buildroot%_datadir/nx/VERSION.nxagent
#cp -a nxproxy/VERSION %buildroot%_datadir/nx/VERSION.nxproxy
#cp -a debian/keystrokes.cfg %buildroot%_sysconfdir/nxagent/
#cp -a debian/nxagent.keyboard %buildroot%_sysconfdir/nxagent/
mkdir -p %buildroot%_datadir/pixmaps/
cp -a nx-X11/programs/Xserver/hw/nxagent/nxagent.xpm %buildroot%_datadir/pixmaps/

%files
#%doc README.md LICENSE LICENSE.nxcomp
#doc %_docdir/%name-%version
#%config(noreplace) %_sysconfdir/ld.so.conf.d/%name-%_arch.conf
%_libdir/libXcomp*.so.*
%_libdir/libNX_*.so.*
%dir %_libdir/nx/
%dir %_libdir/nx/X11/
%_libdir/nx/X11/libX11.so.*
%dir %_datadir/nx
%_datadir/nx/*
%exclude %_datadir/nx/VERSION.nxagent
%exclude %_datadir/nx/VERSION.nxproxy
%_man1dir/nxproxy.*

%if_without system_locale
%dir %_libdir/nx/X11/locale
%_libdir/nx/X11/locale/*
%endif

%files devel
%_libdir/libNX_*.so
%_libdir/libXcomp*.so

%_pkgconfigdir/*.pc

%dir %_includedir/nx/
%_includedir/nx/*
%_includedir/nx-X11/

%files -n nxagent
%dir %_sysconfdir/nxagent
%config(noreplace) %_sysconfdir/nxagent/keystrokes.cfg
#config(noreplace) %_sysconfdir/nxagent/nxagent.keyboard
%_bindir/nxagent
%dir %_libdir/nx/bin
%_libdir/nx/bin/nxagent
%_man1dir/nxagent.*
#_datadir/X11/xkb/keymap.dir
%_pixmapsdir/nxagent.xpm
#%_man1dir/nxagent.1*
%_datadir/nx/VERSION.nxagent
#%_datadir/nx/fonts

%files -n nxproxy
%_bindir/nxproxy
#%_man1dir/nxproxy.1*
%_datadir/nx/VERSION.nxproxy

%files -n nxdialog
%doc nxdialog/README.md
%_bindir/nxdialog
%_man1dir/nxdialog.1*


%changelog
* Fri Oct 27 2023 Ivan A. Melnikov <iv@altlinux.org> 3.5.99.26.1-alt3.1
- add patches for loongarch64 and riscv64 support

* Thu Aug 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.5.99.26.1-alt3
- add patches from Debian
- fix bare words in the spec

* Tue Apr 05 2022 Konstantin Kondratyuk <kondratyuk@altlinux.org> 3.5.99.26.1-alt2
- fix build with python3

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.5.99.26.1-alt1
- drop libNX_X11.so.6 needed from nxagent (fix build package)
- packing nxdialog
- add channels patches

* Fri Feb 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.5.99.26-alt4
- add Conflicts/Provides for Fedora based packaging

* Thu Dec 16 2021 Vitaly Lipatov <lav@altlinux.ru> 3.5.99.26-alt3
- disable -Wpedantic and -Werror*
- enable parallel build (use make_build)
- switch to use libXfont2-devel

* Sat Sep 25 2021 Vitaly Lipatov <lav@altlinux.ru> 3.5.99.26-alt2
- fix building with binutils >= 2.36

* Thu Mar 25 2021 Slava Aseev <ptrnine@altlinux.org> 3.5.99.26-alt1
- new version 3.5.99.26 (with rpmrb script)

* Fri Sep 13 2019 Vitaly Lipatov <lav@altlinux.ru> 3.5.99.22-alt1
- new version 3.5.99.22 (with rpmrb script)
- build without channel_usbip, channel_pcscd, channel_extra1

* Fri Mar 01 2019 Pavel Vainerman <pv@altlinux.ru> 3.5.2.31-alt9
- added patches for compilation with gcc8 (altbug #36207)

* Wed Feb 06 2019 Vitaly Lipatov <lav@altlinux.ru> 3.5.2.31-alt8
- use Obsoletes: nx instead Conflicts

* Fri Jun 08 2018 Pavel Vainerman <pv@altlinux.ru> 3.5.2.31-alt7
- fix window title encoding (eterbug #12919)
- fix font path for ALTLinux (eterbug #12807)

* Fri May 18 2018 Pavel Vainerman <pv@altlinux.ru> 3.5.2.31-alt6
- minor fixes in spec 

* Wed May 16 2018 Pavel Vainerman <pv@altlinux.ru> 3.5.2.31-alt5
- fixed segfault in rootless mode (eterbug #12859)

* Fri May 04 2018 Pavel Vainerman <pv@altlinux.ru> 3.5.2.31-alt4
- (gitlab-ci): minor fixes

* Thu Apr 12 2018 Pavel Vainerman <pv@altlinux.ru> 3.5.2.31-alt3
- update URL
- (gitlab-ci): added build for p7

* Mon Apr 09 2018 Pavel Vainerman <pv@altlinux.ru> 3.5.2.31-alt2
- update build require

* Mon Apr 09 2018 Pavel Vainerman <pv@altlinux.ru> 3.5.2.31-alt1
- added (public) etersoft patches 

* Mon Apr 09 2018 Pavel Vainerman <pv@altlinux.ru> 3.5.0.31-alt4
- minor fixes

* Thu Apr 05 2018 Etersoft Builder <builder@etersoft.ru> 3.5.0.31-alt3
- fixed spec file - added require to font 'fixed' 
- added .gitlab-ci.yml
- fixed path for nxagent

* Thu Apr 05 2018 Pavel Vainerman <pv@altlinux.ru> 3.5.0.31-alt2
- fixed path for nxagent 

* Mon Apr 02 2018 Pavel Vainerman <pv@altlinux.ru> 3.5.0.31-alt1
- new version (3.5.0.31) with rpmgs script
- thanks cas@altlinux.org for the base spec file

