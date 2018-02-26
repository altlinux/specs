Name: nx
Version: 3.5.0
Release: alt1

Summary: Next Generation Remote Display

Packager: Boris Savelev <boris@altlinux.org>

Group: Networking/Remote access
License: GPL, MIT/X11 for X11 bits
Url: http://www.nomachine.com

Source: nxagent-%version-2.tar
Source1: nxauth-%version-1.tar
Source3: nxcomp-%version-1.tar
Source4: nxcompext-%version-1.tar
Source5: nxcompsh-%version-1.tar
Source6: nxcompshad-%version-2.tar
Source7: nxesd-%version-2.tar
Source9: nxproxy-%version-1.tar
Source10: nxscripts-%version-1.tar
Source12: nxservice-%version-1.tar
Source13: nxssh-%version-1.tar
Source15: nxwin-%version-1.tar
Source16: nx-X11-%version-1.tar
Source18: docs.tar
Source19: nxfind-provides.sh
Source50: nxagent.1
Source51: nxagent.keyboard
Source60: Makefile.alt

# alt
Patch: nx-X11-alt-SecurityPolicy-path.patch
Patch2: nxcomp-3.2.0-gcc43.patch
Patch3: nxcompsh-3.2.0-gcc43.patch
Patch4: nxcompshad-3.2.0-gcc43.patch
Patch5: nxcompshad-3.3.0-Xext.patch
Patch6: nx-X11-utf8_copy_clipboard.patch
Patch7: nxesd-3.3.0-esd.patch
Patch9: nxcomp-mdv.patch
Patch10: nxservice-3.5.0-cygwin_ifdef.patch

# linuxforum.ru
Patch40: nx-X11-dimbor.patch
Patch41: nxagent.MotifWMHints_Utf8Names.dimbor.patch
Patch42: nxa_wine_close_delay.patch
Patch43: nx-X11-dimbor_x64.patch

# gentoo
Patch50: nx-3.3.0-cflags.patch

# list
Patch60: createpixmap_bounds_check.patch
Patch61: nx-X11-fix_format.patch

# debian
Patch85: 85_nx-X11_debian-ld.patch
Patch90: 90_set_X0-config_path.patch
Patch91: 91_enable_debug.patch
Patch93: 93_export_remote_keyboard_config.patch

#other
Patch100: wmclass.patch
Patch101: byerace.patch
Patch102: sa_restorer.patch


Obsoletes: NX
Provides: NX = %version

Obsoletes: libXcomp
Provides: libXcomp = %version

Obsoletes: libXcompext
Provides: libXcompext = %version

Obsoletes: libXcompshad
Provides: libXcompshad = %version

%define _use_internal_dependency_generator 0
%define __find_provides %SOURCE19

BuildRequires: docbook-utils gcc-c++ groff-base
BuildRequires: libXdamage-devel libXrandr-devel libXt-devel libXtst-devel
BuildRequires: libalsa-devel libpng-devel zlib-devel libpam-devel
BuildRequires: libssl-devel libstdc++-devel makedepend
BuildRequires: libfreetype libXmu-devel libXcomposite libXpm
BuildRequires: libjpeg-devel
BuildRequires: libaudiofile-devel


%description
NX is an exciting new technology for remote display. It provides near local
speed application responsiveness over high latency, low bandwidth links. The
core libraries for NX are provided by NoMachine under the GPL.

%prep
%setup -c -a1 -a3 -a4 -a5 -a6 -a7 -a9 -a10 -a12 -a13 -a15 -a16

%patch0 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch9 -p1
%patch10 -p1

%patch40 -p0
%patch41 -p0
%patch42 -p0
%patch43 -p0

%patch50 -p0

%patch60 -p0

cd nx-X11
%patch61 -p2
%patch85 -p1
%patch90 -p1
# disable debug?
# %patch91 -p2
%patch93 -p1
cd ..

cd nxproxy
%patch100 -p1
cd ..

cd nxcomp
%patch101 -p1
%patch102 -p1
cd ..

cat >> nx-X11/config/cf/host.def << EOF
#ifdef  i386Architecture
#undef  DefaultGcc2i386Opt
#define DefaultGcc2i386Opt      $RPM_OPT_FLAGS -fno-strict-aliasing
#endif
#ifdef  MipsArchitecture
#undef  DefaultGcc2MipsOpt
#define DefaultGcc2MipsOpt      $RPM_OPT_FLAGS -fno-strict-aliasing
#endif
#ifdef s390xArchitecture
#undef OptimizedCDebugFlags
#define OptimizedCDebugFlags $RPM_OPT_FLAGS -fno-strict-aliasing
#endif
#ifdef  AMD64Architecture
#undef  DefaultGcc2AMD64Opt
#define DefaultGcc2AMD64Opt $RPM_OPT_FLAGS -fno-strict-aliasing
#endif
#define ProjectRoot %_libdir/nxserver
#define MotifDir %_libdir/nxserver
#define XPrintDir %_libdir/nxserver/server
EOF

%__subst "s:/usr/lib/xserver/SecurityPolicy:%_libdir/nxserver/xserver/SecurityPolicy:" nx-X11/programs/Xserver/Xext/security.c
%__subst "s:\$(NLSSUBDIR):nls:" nx-X11/Imakefile

cp %SOURCE60 nx-X11

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
%__subst "s|CXXFLAGS=.-O.*|CXXFLAGS=\"$CXXFLAGS\"|" */configure.in

# prepare X11 includes
pushd nx-X11
%make_build -f Makefile.alt Includes
popd

# build Compression Library and Proxy and Extended Compression Library
for i in nxcomp nxproxy nxcompshad nxcompext nxcompsh; do
pushd $i
%autoreconf
%configure \
    LDFLAGS="-Wl,-R%_libdir/nxserver"
%__subst "s,/usr/X11R6/lib ,/usr/X11R6/%_lib ,g" Makefile
%make_build
popd
done

# build nxssh
pushd nxssh
%configure --without-zlib-version-check
%make
popd

# build nxesd
pushd nxesd
%__subst "s|\.\./audiofile-0.2.3/libaudiofile/\.libs/libaudiofile\.a|-laudiofile|" configure
%configure \
    --disable-shared
# multi proc build is broken on many systems
%make nxesd
popd

# build nxservice
pushd nxservice
%configure
%make_build
popd

# build X11 Support Libraries and Agents
pushd nx-X11
%make_build World
popd

%install
pushd nx-X11
%makeinstall_std -C lib
%makeinstall_std -C nls
%makeinstall_std -C programs/Xserver/Xext
popd

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_sysconfdir/nxagent
mkdir -p %buildroot%_man1dir

# install X11 Support Libraries and Agents
cp -a nx-X11/lib/X11/libX11-nx.so.* \
     nx-X11/lib/Xext/libXext-nx.so.* \
     nx-X11/lib/Xrender/libXrender-nx.so.* \
%buildroot%_libdir/

install -m 755 nx-X11/programs/Xserver/nxagent \
%buildroot%_bindir/

# install Compression Libraries and Proxy
cp -a nxcomp/libXcomp.so.* %buildroot%_libdir/
cp -a nxcompext/libXcompext.so.* %buildroot%_libdir/
cp -a nxcompshad/libXcompshad.so.* %buildroot%_libdir/
cp -a nxcompsh/libXcompsh.so.* %buildroot%_libdir/
install -m 755 nxproxy/nxproxy %buildroot%_bindir/
# install nxssh
pushd nxssh
install -m755 nxssh %buildroot%_bindir/
popd
# install nxesd
pushd nxesd
install -m755 nxesd %buildroot%_bindir/
popd

pushd nxservice
install -m755 nxservice %buildroot%_bindir/
popd

# install scripts
mkdir -p %buildroot%_docdir/%name-%version/
cp -r nxscripts %buildroot%_docdir/%name-%version/
# documentation and license
tar xf %SOURCE18 -C %buildroot%_docdir/%name-%version/
install -m 644 nxcomp/LICENSE %buildroot%_docdir/%name-%version/

mkdir -p %buildroot%_docdir/%name-%version/nxcomp/
install -m 644 nxcomp/README %buildroot%_docdir/%name-%version/nxcomp

install %SOURCE50 %buildroot%_man1dir/
gzip -3 %buildroot%_man1dir/*
install %SOURCE51 %buildroot%_sysconfdir/nxagent/

# for backcompat
ln -s ../bin/nxagent %buildroot%_libdir

# lost secpol file
mkdir -p %buildroot%_libdir/nxserver/xserver
mv %buildroot%_sysconfdir/X11/xserver/SecurityPolicy %buildroot%_libdir/nxserver/xserver/SecurityPolicy

# fix keyboard layout switch (need fix)
mkdir -p %buildroot%_sysconfdir/nxagent/xkb
ln -fs ../../../var/lib/xkb %buildroot%_sysconfdir/nxagent/xkb/compiled
ln -fs ../../../../../etc/nxagent/xkb %buildroot%_libdir/nxserver/lib/X11/

rm -rf %buildroot%_sysconfdir/X11
rm -rf %buildroot%_sysconfdir/fonts
rm -rf %buildroot%_includedir
rm -rf %buildroot%_libdir/nxserver/bin
rm -rf %buildroot%_libdir/nxserver/include
rm -rf %buildroot%_libdir/nxserver/lib*/X11/*.so*
rm -rf %buildroot%_libdir/nxserver/lib*/X11/config
rm -rf %buildroot%_libdir/nxserver/lib*/X11/config
rm -rf %buildroot%_libdir/nxserver/lib*/X11/xserver
rm -rf %buildroot%_libdir/nxserver/lib*/pkgconfig
rm -rf %buildroot%_libdir/nxserver/lib*/*.so*
rm -rf %buildroot%_libdir/nxserver/lib*/*.a

ln -fs ../libX11-nx.so.6 %buildroot%_libdir/nxserver/libX11.so.6
ln -fs ../libXext-nx.so.6 %buildroot%_libdir/nxserver/libXext.so.6
ln -fs ../libXrender-nx.so.1 %buildroot%_libdir/nxserver/libXrender.so.1

%files
%doc %_docdir/%name-%version
%dir %_sysconfdir/nxagent
%config %_sysconfdir/nxagent/nxagent.keyboard
%_sysconfdir/nxagent/xkb
%_bindir/nxagent
%_bindir/nxesd
%_bindir/nxproxy
%_bindir/nxssh
%_bindir/nxservice
%_libdir/lib*.so.*
%_libdir/nxagent
%dir %_libdir/nxserver
%dir %_libdir/nxserver/lib
%dir %_libdir/nxserver/lib/X11
%dir %_libdir/nxserver/xserver
%_libdir/nxserver/*.so.*
%_libdir/nxserver/lib/X11/locale
%_libdir/nxserver/lib/X11/Xcms.txt
%_libdir/nxserver/lib/X11/XKeysymDB
%_libdir/nxserver/lib/X11/XErrorDB
%_libdir/nxserver/lib/X11/xkb
%_libdir/nxserver/xserver/SecurityPolicy
%_man1dir/*

%changelog
* Thu Jun 16 2011 Boris Savelev <boris@altlinux.org> 3.5.0-alt1
- remove turbo-jpeg completly
- remove vendor check
- up to 3.5.0
- add symlinks for X11 libs to %%_libdir/nxserver
- build nxesd staticly with libesd
- build nxcomp* with rpath

* Fri Apr 08 2011 Lenar Shakirov <snejok@altlinux.ru> 3.4.0-alt15
- fixed build:
  + libarts-devel removed from Sisyphus
  + libalsa-devel libpng-devel zlib-devel was added to spec

* Mon Feb 07 2011 Boris Savelev <boris@altlinux.org> 3.4.0-alt14
- build for Sisyphus

* Tue Jan 11 2011 Denis Baranov <baraka@etersoft.ru> 3.4.0-alt13.2
- Fix eterbug #6284

* Thu Dec 16 2010 Boris Savelev <boris@altlinux.org> 3.4.0-alt13
- disable turbo-jpeg
- rebuild with new openssl

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 3.4.0-alt12
- cleanup spec, disable tarball archiving
- drop out build and linking with libjpeg-turbo (eterbug #6284)

* Thu Sep 09 2010 Boris Savelev <boris@altlinux.org> 3.4.0-alt11
- update nx sources:
    nxagent 9->11
    nxauth 2->3
    nxcomp 6->7
    nxcompsh 1->2
    nx-X11 3->4
- libturbo-jpeg 0.0.93 -> 1.0.0

* Mon Jul 26 2010 Boris Savelev <boris@altlinux.org> 3.4.0-alt10
- nxagent updated to 3.4.0-9

* Thu Jun 17 2010 Boris Savelev <boris@altlinux.org> 3.4.0-alt9
- nxagent updated to 3.4.0-8
- libjpeg-turbo updated to 0.0.93

* Tue Jun 15 2010 Alexander Morozov <amorozov@etersoft.ru> 3.4.0-alt8
- fix nxagent crash (eterbug #5121) (closes: #23365)

* Thu May 20 2010 Devaev Maxim <mdevaev@etersoft.ru> 3.4.0-alt7
- disabled libjpeg-turbo by default

* Wed Apr 21 2010 Boris Savelev <boris@altlinux.org> 3.4.0-alt6.1
- remove '%%set_verify_elf_method unresolved=relaxed'

* Sun Apr 11 2010 Michael Shigorin <mike@altlinux.org> 3.4.0-alt6
- fixed build (added BR)

* Fri Mar 19 2010 Boris Savelev <boris@altlinux.org> 3.4.0-alt5
- fix "warning: format not a string literal and no format arguments"

* Wed Mar 10 2010 Boris Savelev <boris@altlinux.org> 3.4.0-alt4
- update: nxauth, nxssh, nxservice, nxcomp
- build with turbo-jpeg

* Wed Feb 10 2010 Boris Savelev <boris@altlinux.org> 3.4.0-alt3
- update: nxagent, nx-X11, nxcompshad

* Mon Jan 04 2010 Boris Savelev <boris@altlinux.org> 3.4.0-alt2
- add another patch from dimbor to fixes rootless mode on x86_64

* Tue Oct 06 2009 Boris Savelev <boris@altlinux.org> 3.4.0-alt1
- new version

* Sun Sep 27 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt19
- add patches from nx-mobile (Fabian Franz) (nxcomp and nxproxy)

* Fri Sep 18 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt18
- update nx-X11-3.3.0-7

* Sun Sep 13 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt17
- update nxagent-3.3.0-18

* Thu Jul 09 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt16.2
- delete unpacked files

* Wed Jul 08 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt16.1
- fix fprintf using (merge with lav@)

* Wed Jul 08 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt15.2
- delete unpacked files

* Tue Jun 23 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt15.1
- rebuild with new libpng

* Mon May 25 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt15
- fix build with new toolchain

* Sat Apr 11 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt14
- add nxa_wine_close_delay.patch for remove delay in rootless mode
- remove devel *.so
- remove ldconfig

* Sun Apr 05 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt13
- fix nxagent.MotifWMHints_Utf8Names.dimbor.patch

* Sun Mar 29 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt12
- add fix for non-ascii character in window titles for Windows client

* Wed Mar 25 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt11
- new nxagent-3.3.0-13.tar.gz
- new nxcomp-3.3.0-4.tar.gz
- new nxcompext-3.3.0-4.tar.gz
- new nx-X11-3.3.0-6.tar.gz
- remove nxcompext-mem-leak.patch (apply in upstream)

* Sat Mar 14 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt10
- fix memory leak in nxcompext with png compress

* Mon Mar 09 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt9
- move all libs to %%_libdir
- move all binaries to %%_bindir
- add nxagent man
- add fix for non-ascii character in window titles for Windows client
- add nxagent keyboard settings patch (new directory %_sysconfdir/nxagent)

* Fri Jan 23 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt8
- fix build nxesd (bug #18620)

* Fri Jan 23 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt7
- new verison:
    nxagent
    nx-X11
    nxcompshad

* Wed Jan 19 2009 Boris Savelev <boris@altlinux.org> 3.3.0-alt6
- back devel *.so (for proprietary soft)
- new verison:
    nxagent
    nx-X11
    nxcompext
- fix buildreq

* Tue Dec 30 2008 Boris Savelev <boris@altlinux.org> 3.3.0-alt5
- add Clipboard patch from dimbor
- remove devel *.so

* Fri Dec 05 2008 Yuri Fil <yurifil@altlinux.org> 3.3.0-alt4
- fix linking in nxesd

* Fri Dec 05 2008 Yuri Fil <yurifil@altlinux.org> 3.3.0-alt3
- don't build nxesd docs (due problem with jade)

* Fri Dec 05 2008 Yuri Fil <yurifil@altlinux.org> 3.3.0-alt2
- fix build on Mandriva/2009.0

* Sat Nov 22 2008 Boris Savelev <boris@altlinux.org> 3.3.0-alt1
- 3.3.0 release

* Tue Jul 15 2008 Boris Savelev <boris@altlinux.org> 3.2.0-alt3
- Fixed TR07F02082. The agent server could be unable to init core
  keyboard on 64 bit systems.

* Thu Jul 03 2008 Boris Savelev <boris@altlinux.org> 3.2.0-alt2
- Imported patch fixing issues from  X.Org security advisory, June
  11th, 2008: Multiple vulnerabilities in X server extensions. CVE
  IDs: CVE-2008-1377, CVE-2008-1379, CVE-2008-2360, CVE-2008-2361,
  CVE-2008-2362.
- new nx-X11 and nxagent

* Sat Jun 14 2008 Boris Savelev <boris@altlinux.org> 3.2.0-alt1
- new version

