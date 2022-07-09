Name: desmume
Version: 0.9.13
Release: alt1
Summary: A Nintendo DS emulator
Group: Emulators
License: GPLv2+
Url: http://desmume.org/
# http://downloads.sourceforge.net/%%name/%%name-%%version.tar.gz
Source: %name-%version.tar.gz
# Fix format strings
Patch0: %{name}-0.9.13-formatstring.patch
# Use system tinyxml instead of the embedded copy
Patch1: %{name}-0.9.13-tinyxml.patch
# Fix building on aarch64
# https://github.com/TASEmulators/desmume/issues/551
Patch2: %{name}-0.9.13-aarch64.patch
#Fix building on ppc64le
# https://github.com/TASEmulators/desmume/issues/550
Patch3: %{name}-0.9.13-ppc64le.patch
Patch4: %{name}-0.9.13-arm.patch

BuildRequires: meson
BuildRequires: libgtkglext-devel
BuildRequires: libglade-devel
BuildRequires: libopenal-devel
BuildRequires: liblua5-devel
BuildRequires: zziplib-devel
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: gcc-c++ libpcap-devel
BuildRequires: desktop-file-utils
BuildRequires: libSDL2-devel
BuildRequires: pkgconfig(tinyxml)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(gtk+-3.0)
Requires: icon-theme-hicolor
BuildPreReq: chrpath



%package cli
Summary: A Nintendo DS emulator (CLI version)
Group: Emulators

%description
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial games.


%description cli
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial games.

This is the CLI version.

%prep
%setup -q -n %name-release_0_9_13
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

pushd desmume

# Remove bundled tinyxml
rm -rf src/utils/tinyxml

# Fix end-of-line encoding
sed -i 's/\r//' AUTHORS

# Fix file encoding
for txtfile in ChangeLog AUTHORS
do
    iconv --from=ISO-8859-1 --to=UTF-8 $txtfile > tmp
    touch -r $txtfile tmp
    mv tmp $txtfile
done

# Fix premissions
find src -name '*.cpp' -exec chmod -v 644 '{}' \;
find src -name '*.h' -exec chmod -v 644 '{}' \;


# Fix premissions
find src -name *.[ch]* -exec chmod 644 {} \;

popd


%build
pushd desmume/src/frontend/posix
%meson
%meson_build
popd

%install
pushd desmume/src/frontend/posix
%meson_install
popd


# Remove installed icon
#rm -f %buildroot%_datadir/pixmaps/DeSmuME.xpm

# Install icons
mkdir -p %buildroot%_datadir/icons/hicolor/32x32/apps
#install -m 644 src/gtk/DeSmuME.xpm %buildroot%_datadir/icons/hicolor/32x32/apps/
#install -m 644 src/gtk/DeSmuME.xpm %buildroot%_datadir/icons/hicolor/32x32/apps/DeSmuME-glade.xpm


%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/icons/hicolor/*/apps/*DeSmuME*
%_datadir/applications/*.desktop
%_datadir/metainfo/*.xml
%_mandir/man1/%name.1*
%doc %name/AUTHORS %name/ChangeLog %name/COPYING %name/README %name/README.LIN

%files cli
%_bindir/%name-cli
%_mandir/man1/%name-cli.1*

%changelog
* Tue Jul 05 2022 Ilya Mashkin <oddity@altlinux.ru> 0.9.13-alt1
- 0.9.13

* Wed Apr 07 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.11-alt4
- Fixed FTBFS (corrected build requires).

* Tue Feb 12 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.11-alt3
- NMU: fixed build with gcc-8.

* Fri Jun 22 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.11-alt2
- Fixed FTBFS (corrected build requires).

* Tue Feb 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.11-alt1
- Updated to version 0.9.11

* Tue Jun 05 2012 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt1
- Build for Sisyphus

* Thu Apr 26 2012 Andrea Musuruane <musuruan@gmail.com> 0.9.8-1
- Updated to upstream version 0.9.8

* Sun Apr 15 2012 Andrea Musuruane <musuruan@gmail.com> 0.9.7-5
- Fixed microphone support (BZ #2231)
- Enabled LUA engine

* Sat Mar 17 2012 Andrea Musuruane <musuruan@gmail.com> 0.9.7-4
- Fixed FTBFS for F17+

* Sat Mar 17 2012 Andrea Musuruane <musuruan@gmail.com> 0.9.7-3
- Fixed an error in desmume-glade.desktop (BZ #2229)

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.9.7-2
- Rebuilt for c++ ABI breakage

* Sun Feb 06 2011 Andrea Musuruane <musuruan@gmail.com> 0.9.7-1
- Updated to upstream version 0.9.7

* Sun Jun 06 2010 Andrea Musuruane <musuruan@gmail.com> 0.9.6-1
- Updated to upstream version 0.9.6-1
- Fixed Source0 URL

* Sun Dec 06 2009 Andrea Musuruane <musuruan@gmail.com> 0.9.5-2
- Added a patch from upstream to compile on big endian systems (SF #2909694)

* Sun Dec 06 2009 Andrea Musuruane <musuruan@gmail.com> 0.9.5-1
- Updated to upstream version 0.9.5
- Updated icon cache scriptlets

* Fri Jul 24 2009 Andrea Musuruane <musuruan@gmail.com> 0.9.4-1
- Updated to upstream version 0.9.4
- Added a fix to compile under gcc 4.4 (SF #2819176)
- Removed no longer needed patches
- Removed no longer needed Debian man pages
- Cosmetic changes

* Thu Apr 30 2009 Andrea Musuruane <musuruan@gmail.com> 0.9.2-2
- Added a patch from upstream to fix IO Regs menu crash (SF #2781065)

* Sun Apr 19 2009 Andrea Musuruane <musuruan@gmail.com> 0.9.2-1
- Updated to upstream version 0.9.2
- Removed no longer needed patch to compile with gcc 4.4
- Added a patch from upstream to compile on 64 bit systems (SF #2755952)

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.1-3
- rebuild for new F11 features

* Sat Feb 14 2009 Andrea Musuruane <musuruan@gmail.com> 0.9.1-2
- Made a patch to compile with gcc 4.4 (SF #2599049)

* Fri Feb 13 2009 Andrea Musuruane <musuruan@gmail.com> 0.9.1-1
- Updated to upstream version 0.9.1

* Sun Jan 04 2009 Andrea Musuruane <musuruan@gmail.com> 0.9-1
- Updated to upstream version 0.9

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.8-2
- rebuild for buildsys cflags issue

* Wed Apr 23 2008 Andrea Musuruane <musuruan@gmail.com> 0.8-1
- Updated to upstream version 0.8

* Sun Sep 08 2007 Andrea Musuruane <musuruan@gmail.com> 0.7.3-4
- Using debian sources because many things were missing from upstream
- Removed no longer needed automake and autoconf from BR
- Updated icon cache scriptlets to be compliant to new guidelines

* Tue Aug 21 2007 Andrea Musuruane <musuruan@gmail.com> 0.7.3-3
- Added missing automake libtool to BR

* Mon Aug 20 2007 Andrea Musuruane <musuruan@gmail.com> 0.7.3-2
- Added missing autoconf to BR

* Sat Aug 18 2007 Andrea Musuruane <musuruan@gmail.com> 0.7.3-1
- Updated to upstream version 0.7.3
- Added man pages from Debian
- Updated License tag from GPL to GPLv2+
- Removed %%{?dist} tag from changelog

* Sun Jun 24 2007 Andrea Musuruane <musuruan@gmail.com> 0.7.1-1
- Updated to upstream version 0.7.1
- Updated icon cache scriptlets to be compliant to new guidelines

* Thu Jun 07 2007 Andrea Musuruane <musuruan@gmail.com> 0.7.0-2
- Added a patch from Ian Chapman to remove the buggy tools menu which
  only contains IO regs which frequently crashes desmume on x86_64
- Added a patch from Ian Chapman to make desmume-glade ONLY look in the
  installed location for it's .glade files and not to use the "uninstalled"
  location
- Shortened description
- Better use of %%{name} macro

* Fri May 25 2007 Andrea Musuruane <musuruan@gmail.com> 0.7.0-1
- Updated to upstrem version 0.7.0

* Sun Mar 25 2007 Andrea Musuruane <musuruan@gmail.com> 0.6.0-1
- Initial release for Dribble

