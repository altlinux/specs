Name:    nx-libs
Version: 3.5.0.31
Release: alt4
Summary: NX X11 protocol compression libraries

Group:   System/Libraries
License: GPLv2+
URL:     http://x2go.org/

# Source0-url: https://github.com/ArcticaProject/nx-libs/archive/redist-server/%version.tar.gz
Source0: %name-%version.tar
Source1: Makefile.alt

BuildRequires: gcc-c++
BuildRequires: fontconfig-devel
BuildRequires: gccmakedep
BuildRequires: imake
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXext-devel
BuildRequires: libXfont-devel
BuildRequires: libXfixes-devel
BuildRequires: libXinerama-devel
BuildRequires: libXpm-devel
BuildRequires: libXrandr-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
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

Conflicts: nx
Provides:  nx = %EVR

%description
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network  especially a slow one.

This package provides the core nx-X11 libraries customized for
nxagent/x2goagent.

%package devel
Summary: Header files for development with nx
Group: Development/C
Requires: %name = %version-%release

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

%prep
%setup -q

# Apply all patches from debian/patches
cat debian/patches/series | while read patchfile;do 
	test -e debian/patches/$patchfile && patch -p1 < debian/patches/$patchfile
done

# Install into /usr
sed -i -e 's,/usr/local,/usr,' nx-X11/config/cf/site.def
# Use rpm optflags
sed -i -e 's#-O3#%{optflags}#' nx-X11/config/cf/host.def
sed -i -e 's#-O3#%{optflags}#' nx-X11/config/cf/linux.cf
echo "#define DefaultGcc2Ppc64Opt %optflags" >> nx-X11/config/cf/host.def
# Use multilib dirs
# We're installing binaries into %%_libdir/nx/bin rather than %%_libexedir/nx
# becuase upstream expects libraries and binaries in the same directory

#sed -i -e 's,/lib/nx,/%_lib/nx,' Makefile nx-X11/config/cf/X11.tmpl
#sed -i -e 's,/lib/x2go,/%_lib/x2go,' Makefile

# Fix FSF address
find -name LICENSE | xargs sed -i \
  -e 's/59 Temple Place/51 Franklin Street/' -e 's/Suite 330/Fifth Floor/' \
  -e 's/MA  02111-1307/MA  02110-1301/'
# Fix source permissions
find -type f -name '*.[hc]' | xargs chmod -x

# Bundled nx-X11/extras
# Xpm - Is needed and needs to get linked to libXcomp
# Mesa - Used by the X server

# Xcursor - Other code still references files in it
# Xfont - Statically linked to nxarget  others?
# Xpm

%__subst "s:\$(NLSSUBDIR):nls:" nx-X11/Imakefile

cp %SOURCE1 nx-X11

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
# allow use rpm optflags
%__subst "s|^C.*FLAGS=.*-O.*||" */configure*

# prepare X11 includes
pushd nx-X11
%make_build USRLIBDIR=%_libdir SHLIBDIR=%_libdir -f Makefile.alt Includes
popd

for i in nxcomp nxproxy nxcompshad nxcompext; do
pushd $i
%autoreconf
%configure USRLIBDIR=%_libdir SHLIBDIR=%_libdir
%__subst "s,/usr/X11R6/lib ,/usr/X11R6/%_lib ,g" Makefile
popd
done

# build X11 Support Libraries and Agents
pushd nx-X11
%__subst 's|NX_REQUIREDLIBS   = |NX_REQUIREDLIBS   = -ldl |g' lib/X11/Imakefile
%make_build USRLIBDIR=%_libdir SHLIBDIR=%_libdir World
popd

# build Compression Library and Proxy and Extended Compression Library
for i in nxcomp nxproxy nxcompshad nxcompext; do
pushd $i
export LDFLAGS="${LDFLAGS} -L../nx-X11/exports/lib -lNX_X11"
%make_build USRLIBDIR=%_libdir SHLIBDIR=%_libdir
popd
done

pushd nx-X11
%make_build USRLIBDIR=%_libdir SHLIBDIR=%_libdir
popd

pushd nx-X11/lib

# rebuild libraries with new links
for i in X11 Xfixes Xdamage Xcomposite; do
pushd $i
%__subst 's|-lc|-lc -lX11|g' Makefile
rm -rf *.so*
%make_build
popd
done
popd


%install
pushd nx-X11
%makeinstall_std PREFIX=%_prefix USRLIBDIR=%_libdir SHLIBDIR=%_libdir NXLIBDIR=%_libdir -C lib
%makeinstall_std PREFIX=%_prefix USRLIBDIR=%_libdir SHLIBDIR=%_libdir NXLIBDIR=%_libdir -C nls
%makeinstall_std PREFIX=%_prefix USRLIBDIR=%_libdir SHLIBDIR=%_libdir NXLIBDIR=%_libdir -C programs/Xserver/Xext
popd

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_sysconfdir/nxagent
mkdir -p %buildroot%_man1dir

# install NX libraries to system libdir
cp -a nx-X11/lib/X11/libNX_*.so.* %buildroot%_libdir/

# Remove static libs
rm %buildroot%_libdir/*.a

# install Compression Libraries and Proxy
cp -a nxcomp/libXcomp.so.* %buildroot%_libdir/
cp -a nxcompext/libXcompext.so.* %buildroot%_libdir/
cp -a nxcompshad/libXcompshad.so.* %buildroot%_libdir/
install -m 755 nxproxy/nxproxy %buildroot%_bindir/

mkdir -p -m0755 %buildroot%_includedir/nx
cp -afLr nx-X11/exports/include/X11 %buildroot%_includedir/nx/

# install files for development
mkdir -p %buildroot%_includedir/nx
cp -a nxcomp/*.h %buildroot%_includedir/nx/
cp -a nxcomp/libXcomp.so %buildroot%_libdir/
cp -a nxcompshad/Shadow.h %buildroot%_includedir/nx/

mkdir -p %buildroot%_libdir/nx/bin
install -D -m 755 nx-X11/programs/Xserver/nxagent %buildroot%_libdir/nx/bin
install -D -m 755 debian/wrappers/nxagent %buildroot%_bindir
subst 's|/usr/lib|%_libdir|g' %buildroot%_bindir/nxagent

mkdir -p %buildroot%_datadir/nx/X11
mv %buildroot%_sysconfdir/X11/xserver/SecurityPolicy %buildroot%_datadir/nx/SecurityPolicy
mv %buildroot/usr/lib/nx/X11/*DB %buildroot%_datadir/nx/X11/
mv %buildroot/usr/lib/nx/X11/Xcms.txt %buildroot%_datadir/nx/X11/

# fix keyboard layout switch
#mkdir -p %buildroot%_sysconfdir/nxagent/xkb/compiled/
#ln -fs ../../../var/lib/xkb %buildroot%_sysconfdir/nxagent/xkb/compiled
#ln -fs ../../../../../%_sysconfdir/nxagent/xkb %buildroot%_libdir/nxserver/lib/X11/

# delete unused files
rm -rf %buildroot%_sysconfdir/X11
rm -rf %buildroot%_sysconfdir/fonts
rm -rf %buildroot%_libdir/nxserver/bin
rm -rf %buildroot%_libdir/nxserver/include
rm -rf %buildroot%_libdir/nxserver/lib*/X11/*.so*
rm -rf %buildroot%_libdir/nxserver/lib*/X11/config
rm -rf %buildroot%_libdir/nxserver/lib*/X11/config
rm -rf %buildroot%_libdir/nxserver/lib*/X11/xserver
rm -rf %buildroot/usr/lib/nx/X11/locale
rm -rf %buildroot/usr/lib/nx/X11/xserver
rm -rf %buildroot%_libdir/nxserver/lib*/pkgconfig
rm -rf %buildroot%_libdir/nxserver/lib*/*.so*
rm -rf %buildroot%_libdir/nxserver/lib*/*.a
rm -rf %buildroot%_libdir/pkgconfig/*.pc

mkdir -p %buildroot%_datadir/nx/
install -m644 debian/rgb %buildroot%_datadir/nx/rgb.txt

cd %buildroot%_libdir
ln -sf libXcomp.so.3.5.0 libXcomp.so
ln -sf libXcompext.so.3.5.0 libXcompext.so
ln -sf libXcompshad.so.3.5.0 libXcompshad.so
cd -

mkdir -p %buildroot%_docdir/%name-%version/
install -m 644 nxcomp/LICENSE %buildroot%_docdir/%name-%version/
mkdir -p %buildroot%_docdir/%name-%version/nxcomp/
install -m 644 nxcomp/README %buildroot%_docdir/%name-%version/nxcomp

# Needed for nxagent to find the keymap directory
mkdir -p %buildroot%_datadir/X11/xkb
touch %buildroot%_datadir/X11/xkb/keymap.dir

cp -a nxcomp/VERSION %buildroot%_datadir/nx/VERSION.nxagent
cp -a nxproxy/VERSION %buildroot%_datadir/nx/VERSION.nxproxy
cp -a debian/keystrokes.cfg %buildroot%_sysconfdir/nxagent/
cp -a debian/nxagent.keyboard %buildroot%_sysconfdir/nxagent/
mkdir -p %buildroot%_datadir/pixmaps/
cp -a nx-X11/programs/Xserver/hw/nxagent/nxagent.xpm %buildroot%_datadir/pixmaps/

%post -n nxagent
# fix font path
[ -r %_datadir/X11/fonts/misc ] || ln -s %_datadir/fonts/bitmap/misc %_datadir/X11/fonts/misc


%files
#%doc README.md LICENSE LICENSE.nxcomp
%doc %_docdir/%name-%version
#%config(noreplace) %_sysconfdir/ld.so.conf.d/%name-%_arch.conf
%_libdir/libXcomp*.so.*
%_libdir/libNX_*.so.*
%dir %_libdir/nx
%dir %_datadir/nx
%_datadir/nx/*
%exclude %_datadir/nx/VERSION.nxagent
%exclude %_datadir/nx/VERSION.nxproxy

%files devel
%_libdir/libNX_*.so
%_libdir/libXcomp*.so

# conflict with X11-devel
# %_libdir/pkgconfig/*.pc

%dir %_includedir/nx
%dir %_includedir/nx/X11
%_includedir/nx/*

%files -n nxagent
%dir %_sysconfdir/nxagent
%config(noreplace) %_sysconfdir/nxagent/keystrokes.cfg
%config(noreplace) %_sysconfdir/nxagent/nxagent.keyboard
%_bindir/nxagent
%dir %_libdir/nx/bin
%_libdir/nx/bin/nxagent
%_datadir/X11/xkb/keymap.dir
%_pixmapsdir/nxagent.xpm
#%_man1dir/nxagent.1*
%_datadir/nx/VERSION.nxagent
#%_datadir/nx/fonts

%files -n nxproxy
%_bindir/nxproxy
#%_man1dir/nxproxy.1*
%_datadir/nx/VERSION.nxproxy

%changelog
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

