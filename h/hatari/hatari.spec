Group: Emulators
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)


Summary: An Atari ST emulator suitable for playing games
Name: hatari
Version: 2.1.0
Release: alt1
License: GPLv2+
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://hatari.tuxfamily.org/
Source0: http://download.tuxfamily.org/%name/%version/%name-%version.tar.bz2
Source1: hatari.desktop
# Take DESTDIR into consideration when installing symlinks
# https://hg.tuxfamily.org/mercurialroot/hatari/hatari/rev/35281f58daab
Patch0: %{name}-2.0.0-symlinks.patch
# Compile on aarch64
# https://listengine.tuxfamily.org/lists.tuxfamily.org/hatari-devel/2016/12/msg00013.html
Patch1: %{name}-2.0.0-aarch64.patch
# Compile on s390(x)
Patch2: %{name}-2.0.0-s390.patch
# PythonUI: Support both Hatari config file locations
# https://hg.tuxfamily.org/mercurialroot/hatari/hatari/raw-rev/7b3bcc42bc81
Patch3: %{name}-2.0.0-hatariui_conf.patch
# PythonUI: Support for Hatari v2.0 option changes
# https://hg.tuxfamily.org/mercurialroot/hatari/hatari/raw-rev/d1668fda4200
Patch4: %{name}-2.0.0-hatariui_options.patch
# Fix X11 window embedding with SDL2
# https://hg.tuxfamily.org/mercurialroot/hatari/hatari/raw-rev/2b82cd9e99d1
Patch5: %{name}-2.0.0-window_embedding.patch


BuildRequires: ctest cmake rpm-macros-cmake
BuildRequires: libSDL2-devel libSDL2_image-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: readline-devel
BuildRequires: libportaudio2-devel
BuildRequires: python-devel
BuildRequires: libicns-utils
BuildRequires: desktop-file-utils
Requires: icon-theme-hicolor
# Required by zip2st and atari-hd-image
Requires: unzip
Requires: mtools
Requires: dosfstools
Source44: import.info

%package ui
Summary: External user interface for Hatari
Group: Emulators
Requires: %name = %version-%release
Requires: pygtk2
Requires: icon-theme-hicolor

%description
Hatari is an emulator for the Atari ST, STE, TT and Falcon computers.
More precisely, it is an adaption of the WinSTon source code to
Linux, using the UAE CPU core instead of the original, non-portable
assembler CPU core.

The Atari ST was a 16/32 bit computer system which was first released
by Atari in 1985. Using the Motorola 68000 CPU, it was a very popular
computer having quite a lot of CPU power at that time.

Unlike many other Atari ST emulators which try to give you a good
environment for running GEM applications, Hatari tries to emulate the
hardware of a ST as close as possible so that it is able to run most
of the old ST games and demos.

%description ui
Hatari UI is an out-of-process user interface for the Hatari emulator and its
built-in debugger which can (optionally) embed the Hatari emulator window.

%prep
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%setup
#patch0 -p1
#patch1 -p1
#patch2 -p1
#patch3 -p1
#patch4 -p1
#patch5 -p1

# Remove shebang from non executable scripts
for pyfile in dialogs.py hatari.py uihelpers.py config.py
do
  sed -i -e '/^#!\//, 1d' python-ui/$pyfile
done

# Fix hataiui to get doc files
sed -i 's/"hatari" + sep/"%name%{!?_docdir_fmt:-%version}" + sep/' \
  python-ui/uihelpers.py

%build
%{fedora_cmake} \
  -DCMAKE_VERBOSE_MAKEFILE=TRUE \
  -DCMAKE_BUILD_TYPE:STRING=None \
  -DDOCDIR:PATH=%_pkgdocdir \
  -DBUILD_SHARED_LIBS:BOOL=OFF .
# It does not compile with smp_mflags
make

%install
make install DESTDIR=%buildroot

# Fix file permissions
chmod 644 %buildroot%_datadir/%name/hatariui/conftypes.py

# Install French man page
install -d -m 755 %buildroot%_mandir/fr/man1
install -p -m 644 doc/fr/hatari.1 %buildroot%_mandir/fr/man1

# Install desktop file
install -d -m 755 %buildroot%_datadir/applications
desktop-file-install \
  --dir %buildroot%_datadir/applications \
  %SOURCE1

# Extract Mac OS X icons
icns2png -x src/gui-osx/Hatari.icns

# Install icons
#for i in 16 32 48 128; do
#for i in 32 48 128; do
#  install -d -m 755 %buildroot%_datadir/icons/hicolor/${i}x${i}/apps
#  install -m 644 Hatari_${i}x${i}x32.png \
#    %buildroot%_datadir/icons/hicolor/${i}x${i}/apps/hatari.png
#done


install -m 644 python-ui/hatari-icon.png \
    %buildroot%_datadir/icons/hicolor/32x32/apps/hatari-icon.png


# Install hatari-ui desktop file
desktop-file-install \
  --delete-original \
  --remove-key Encoding \
  --add-category Game \
  --add-category Emulator \
  --dir %buildroot%_datadir/applications \
  %buildroot%_datadir/applications/hatariui.desktop

# Install license among docs
install -p -m 644 gpl.txt %buildroot%_pkgdocdir

%files
%_bindir/*
%_datadir/%name
%_mandir/man1/*
%_mandir/fr/man1/*
%if %{with desktop_vendor_tag}
%_datadir/applications/fedora-%name.desktop
%else
%_datadir/applications/%name.desktop
%endif
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/hicolor/*/apps/%name.svg
%_datadir/icons/hicolor/*/mimetypes/*
%_datadir/mime/packages/hatari.xml
%doc %_pkgdocdir
%exclude %_bindir/hatariui
%exclude %_datadir/%name/hatariui
%exclude %_datadir/%name/hconsole
%exclude %_mandir/man1/hatariui.1*
%exclude %_mandir/man1/hconsole.1*

%files ui
%_bindir/hatariui
%_datadir/%name/hatariui
%_datadir/%name/hconsole
%_mandir/man1/hatariui.1*
%_mandir/man1/hconsole.1*
%_datadir/applications/hatariui.desktop
%_datadir/icons/hicolor/32x32/apps/hatari-icon.png
%doc python-ui/{README,release-notes.txt,TODO}
%exclude %_datadir/%name/hatariui/README
%exclude %_datadir/%name/hatariui/release-notes.txt
%exclude %_datadir/%name/hatariui/TODO
%exclude %_datadir/%name/hconsole/release-notes.txt

%changelog
* Mon May 07 2018 Ilya Mashkin <oddity@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Tue Jul 25 2017 Ilya Mashkin <oddity@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Fri Aug 15 2014 Ilya Mashkin <oddity@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Wed Aug 06 2014 Ilya Mashkin <oddity@altlinux.ru> 1.7.0-alt2
- build for Sisyphus

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_3
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_2
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_1
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_4
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_3
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_2
- initial fc import

