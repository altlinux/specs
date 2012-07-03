%define tarname Songbird
%define mozappdir %_libdir/songbird

Name: songbird
Summary: The desktop media player mashed-up with the Web
Version: 1.8.0
Release: alt1.2
# Songbird requires an upstream patched xulrunner and taglib to function
# properly. Bundled vendor sources can be found at:
# http://wiki.songbirdnest.com/Developer/Articles/Builds/Contributed_Builds
Packager: Aeliya Grevnyov <gray_graff@altlinux.org>

Source: %tarname.tar
Source1: %tarname-vendor-reduced.tar
Source2: songbird.desktop
Source3: find-external-requires
Source4: songbird.sh.in
Patch1: system_nspr.patch
Patch2: as-needed.patch
Patch3: fix_ssltunnel_with_system_nss.patch
Patch4: leak_setenv_apprunner.patch
Patch5: move_hunspell_1.2.patch
Patch6: startup-script.patch
#Patch7: disable_ipod_plugin.patch
Patch8: songbird-1.8.0-alt-glib2-2.32.0.patch
Patch9: songbird-1.8.0-alt-no-unused-vars.patch
Group: Sound
License: GPLv2
Url: http://www.getsongbird.com

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: gstreamer-devel
BuildRequires: gst-plugins-devel
BuildRequires: libXt-devel
BuildRequires: libXext-devel
BuildRequires: libIDL-devel
BuildRequires: libcurl-devel
BuildRequires: gtk2-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libhal-devel
BuildRequires: zlib-devel
BuildRequires: unzip zip libzip-devel
BuildRequires: subversion
BuildRequires: libcairo-devel
BuildRequires: libjpeg-devel
BuildRequires: libgtk+2-devel
BuildRequires: pango-devel
BuildRequires: libnspr-devel
BuildRequires: libnss-devel libnss-devel-static
BuildRequires: libhunspell-devel

%description
Songbird is a desktop media player mashed-up with the Web. Songbird is
committed to playing the music you want, from the sites you want, on the
devices you want, challenging the conventions of discovery, purchase,
consumption and organization of music on the Internet.
Songbird is a player and a platform. Like Firefox, Songbird is an open source,
Open Web project built on the Mozilla platform. Songbird provides a public
playground for Web media mash-ups by providing developers with both desktop and
Web APIs, developer resources and fostering Open Web media standards, to wit,
an Open Media Web.

%prep
# Upstream scripts generalize archs. Specify the proper
# paths to match upstream for a sane build.
%ifarch %ix86
%define sb_arch i686
%else
%define sb_arch %_arch
%endif

%setup -q -n %tarname
%patch1 -p3
%patch2 -p2
%patch6 -p2
#%%patch7 -p2
#%%__sed -i 's/SB_MILESTONE=1.2.1/SB_MILESTONE=1.2.0/' build/sbBuildInfo.mk.in

#Unpack vendor packages
tar xf %SOURCE1

pushd %tarname-vendor
%patch3 -p5
%patch4 -p5
%patch5 -p5
popd
%patch8 -p2
%patch9 -p2

mkdir -p build/checkout/linux-%sb_arch
mkdir -p build/linux-%sb_arch
#rm -rf dependencies/vendor
mv %tarname-vendor dependencies/vendor

%build
# Build the included vendor libraries(sqlite3)
pushd dependencies/vendor/sqlite
SB_VENDOR_BUILD_ROOT=%_builddir/%tarname/build make -f Makefile.songbird release
popd

# Move compiled sqlite3 into the dependecies area
pushd build/linux-%sb_arch
mkdir -p %_builddir/%tarname/dependencies/linux-%sb_arch
mv sqlite ../../dependencies/linux-%sb_arch/
popd


# Build XULRunner
%add_optflags %optflags_shared
%add_findreq_skiplist %mozappdir/application.ini
pushd dependencies/vendor/xulrunner/mozilla

# Build with -Os as it helps the browser; also, don't override mozilla's warning
# level; they use -Wall but disable a few warnings that show up _everywhere_
MOZ_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | sed -e 's/-O2/-Os/' -e 's/-Wall//')
export RPM_OPT_FLAGS=$MOZ_OPT_FLAGS
export LDFLAGS="$LDFLAGS -Wl,-rpath,%mozappdir/xulrunner -Wl,-rpath-link,%_builddir/%tarname/dependencies/linux-%sb_arch/mozilla/release"

#Setup XULRunner mozconfig
cat << "EOF" > .mozconfig
MOZILLA_OFFICIAL=1
export MOZILLA_OFFICIAL
BUILD_OFFICIAL=1
export BUILD_OFFICIAL

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/compiled/xulrunner
ac_add_options --prefix=%prefix
ac_add_options --libdir=%_libdir
ac_add_options --mandir=%_mandir
ac_add_options --with-system-jpeg
ac_add_options --with-system-zlib
ac_add_options --with-system-bz2
ac_add_options --with-pthreads
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --enable-system-hunspell
ac_add_options --enable-optimize="$RPM_OPT_FLAGS"
ac_add_options --enable-pango
ac_add_options --enable-system-cairo
ac_add_options --enable-svg
ac_add_options --enable-canvas
ac_add_options --enable-application=xulrunner
ac_add_options --with-xulrunner-stub-name=songbird-bin
ac_add_options --disable-debug
ac_add_options --disable-tests
ac_add_options --disable-auto-deps
ac_add_options --disable-crashreporter
ac_add_options --disable-javaxpcom
ac_add_options --disable-elf-dynstr-gc
ac_add_options --disable-updater
ac_add_options --disable-installer
ac_add_options --enable-extensions=default
ac_add_options --disable-dbus
ac_add_options --enable-jemalloc
ac_add_options --enable-strip
ac_add_options --enable-strip-libs
ac_add_options --enable-install-strip
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options MOZ_DEBUG_SYMBOLS=0
mk_add_options MOZ_MAKE_FLAGS=%_smp_mflags
EOF

mkdir -p compiled/xulrunner

make -f client.mk build_all

popd

mkdir -p dependencies/linux-%sb_arch/mozilla/release
mkdir -p dependencies/linux-%sb_arch/xulrunner/release

# Package XULRunner
pushd dependencies/vendor/xulrunner
./make-mozilla-sdk.sh mozilla mozilla/compiled/xulrunner ../../linux-%sb_arch/mozilla/release
./make-xulrunner-tarball.sh mozilla/compiled/xulrunner/dist/bin ../../linux-%sb_arch/xulrunner/release xulrunner.tar.bz2

# Link the completed package where make expects it
ln -s ../../dependencies/linux-%sb_arch/mozilla ../../../build/linux-%sb_arch/mozilla
popd


# Build the included vendor libraries(taglib)
pushd dependencies/vendor/taglib
SB_VENDOR_BUILD_ROOT=%_builddir/%tarname/build make -f Makefile.songbird release
popd

# Move compiled taglib into the dependecies area
pushd build/linux-%sb_arch
mv taglib ../../dependencies/linux-%sb_arch/
popd


# Build Songbird
export SB_ENABLE_INSTALLER=1
export SONGBIRD_OFFICIAL=1
export SB_ENABLE_JARS=1
export SB_DISABLE_PKG_AUTODEPS=0

# Force system library usage
echo "ac_add_options --with-media-core=gstreamer-system --with-libxul-sdk=%_builddir/%tarname/dependencies/linux-%sb_arch/mozilla/release --disable-tests --disable-breakpad" > songbird.config

# In order for debug packages to be created, -gstabs+ must be
# removed from the compile options under 64 bit or debugedit chokes,
# bug 453506
sed -i s/-gstabs+//g configure.ac
autoreconf -fisv
make -f songbird.mk MOZ_MAKE_FLAGS=%_smp_mflags

%install

cd compiled
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_iconsdir/hicolor/32x32/apps
mkdir -p %buildroot%_iconsdir/hicolor/64x64/apps
mkdir -p %buildroot%_iconsdir/hicolor/128x128/apps
mkdir -p %buildroot%_iconsdir/hicolor/256x256/apps
mkdir -p %buildroot%_iconsdir/hicolor/512x512/apps
mkdir -p %buildroot%_desktopdir
cp -pR dist %buildroot%_libdir/songbird

cp -p ../app/branding/songbird-32.png %buildroot%_iconsdir/hicolor/32x32/apps/songbird.png
cp -p ../app/branding/songbird-64.png %buildroot%_iconsdir/hicolor/64x64/apps/songbird.png
cp -p ../app/branding/songbird-128.png %buildroot%_iconsdir/hicolor/128x128/apps/songbird.png
cp -p ../app/branding/songbird-256.png %buildroot%_iconsdir/hicolor/256x256/apps/songbird.png
cp -p ../app/branding/songbird-512.png %buildroot%_iconsdir/hicolor/512x512/apps/songbird.png

desktop-file-install --vendor="" --dir=%buildroot%_desktopdir %SOURCE2

# set up the songbird start script
cat %SOURCE4 > %buildroot%_bindir/songbird
chmod 755 %buildroot%_bindir/songbird

%files
%_bindir/songbird
%mozappdir
%defattr(0644,root,root,0755)
%_desktopdir/songbird.desktop
%_iconsdir/hicolor/128x128/apps/songbird.png
%_iconsdir/hicolor/256x256/apps/songbird.png
%_iconsdir/hicolor/32x32/apps/songbird.png
%_iconsdir/hicolor/512x512/apps/songbird.png
%_iconsdir/hicolor/64x64/apps/songbird.png

%changelog
* Tue Jun 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.2
- Fixed build

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.1
- Fixed build with new glib2

* Wed Nov 03 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.8.0-alt1
- Update to 1.8.0 version (fix building)
- Build with local(not system) sqlite3 (upstream - suxx)
- Fix repocop info (freedesktop-desktop)
- Remove disable_ipod_plugin.patch (disabled in upstream)

* Sun Mar 14 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.4.3-alt1
- Update to 1.4.3 version

* Sun Sep 13 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.4.0-alt0.1.svn20090913
- Update to svn20090913.

* Tue Aug 04 2009 gray_graff <gray_graff@altlinux.org> 1.3.0-alt0.1.svn20090731
- Disable ipod plugin.
- Update as-needed.patch.
- Remove applied in upstream patch (nsAppRunner.patch).
- Update system_nspr.patch.
- Update to svn20090731.

* Mon Jul 13 2009 gray_graff <gray_graff@altlinux.org> 1.2.0-alt2
- Fix critical bugs:
  + Crash on some sites. move_hunspell_1.2 patch (fta@ubuntu.com)
  + Crash when songbird is started twice. leak_setenv_apprunner
    patch (fta@ubuntu.com)
- Build with system hunspell
- Fix wrong xulrunner-devel requires
- Fix startup script

* Tue Jul 07 2009 gray_graff <gray_graff@altlinux.org> 1.2.0-alt1
- Initial build fot Sisyphus
- Build with system nss
- Build with system nspr
- with-libxul-sdk (thanks legion@)
- Fix build with as-needed

* Fri Jun 19 2009 David Lee Halik <auralvance@gmail.com> - 1.2.0-1
- Bump to 1.2.0
- Songbird bugzilla 15689, and 16022 patches upstreamed, removed
- Populated icon cache with updated pngs
