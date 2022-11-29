Summary: An Atari ST emulator suitable for playing games
Name: hatari
Version: 2.4.1
Release: alt2
License: GPLv2+
Group: Emulators
Url: http://hatari.tuxfamily.org/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %name-%version.tar.bz2
Source1: hatari.desktop

%add_python3_path %_datadir/%name
BuildRequires(pre): rpm-macros-cmake rpm-build-python3 rpm-build-gir
BuildRequires: ctest cmake
BuildRequires: libSDL2-devel libSDL2_image-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: readline-devel
BuildRequires: libportaudio2-devel
BuildRequires: python3-dev
BuildRequires: desktop-file-utils
Requires: icon-theme-hicolor
# Required by zip2st and atari-hd-image
Requires: unzip
Requires: mtools
Requires: dosfstools

%package ui
Summary: External user interface for Hatari
Group: Emulators
Requires: %name = %version
#BuildArch:      noarch
Requires: libgtk+3
Requires: typelib(Gtk) = 3.0

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
%setup
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Fix interpreter

for pyfile in tools/atari-convert-dir.py tools/debugger/hatari_profile.py tools/hconsole/example.py tools/hconsole/hconsole.py python-ui/hatariui.py python-ui/gentypes.py python-ui/debugui.py
do
  sed -i '1s|/usr/bin/env python3|%{__python3}|' $pyfile
done

%build
%cmake_insource \
  -DCMAKE_BUILD_TYPE:STRING=None \
  -DDOCDIR:PATH=%_pkgdocdir \
  -DBUILD_SHARED_LIBS:BOOL=OFF .
%cmake_build

%install
%cmake_install

# Install French man page
install -d -m 755 %buildroot%_mandir/fr/man1
install -p -m 644 doc/fr/hatari.1 %buildroot%_mandir/fr/man1

# Install desktop file
install -d -m 755 %buildroot%_datadir/applications
desktop-file-install \
  --dir %buildroot%_datadir/applications \
  %SOURCE1

#Add translation of description in desktop file
sed -i '4 a Comment\[ru\]=Эмулятор компьютеров Atari ST'  %buildroot%_datadir/applications/hatari.desktop

install -m 644 python-ui/hatari-icon.png \
    %buildroot%_datadir/icons/hicolor/32x32/apps/hatari-icon.png


# Install hatari-ui desktop file
desktop-file-install \
  --delete-original \
  --remove-key Encoding \
  --add-category Game \
  --add-category Emulator \
  --dir %buildroot%_datadir/applications \
  %buildroot%_datadir/applications/hatari.desktop

# Install license among docs
install -p -m 644 gpl.txt %buildroot%_pkgdocdir

%check
ctest -V

%files
%_bindir/*
%_datadir/%name
%_mandir/man1/*
%_mandir/fr/man1/*
#_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/hicolor/*/apps/%name.svg
%_datadir/icons/hicolor/*/mimetypes/*
%_datadir/mime/packages/hatari.xml
%doc %_pkgdocdir
%exclude %_bindir/hatari
%exclude %_datadir/%name/*
%exclude %_datadir/%name/hconsole
%exclude %_mandir/man1/hatari.1*
%exclude %_mandir/man1/hconsole.1*

%files ui
%_bindir/hatari
%_datadir/%name/*
%_datadir/%name/hconsole
%_mandir/man1/hatari.1*
%_mandir/man1/hconsole.1*
%_datadir/applications/hatari.desktop
%_datadir/icons/hicolor/32x32/apps/hatari-icon.png
%doc python-ui/{README,release-notes.txt,TODO}
#exclude %_datadir/%name/hatariui/README
#exclude %_datadir/%name/hatariui/release-notes.txt
#exclude %_datadir/%name/hatariui/TODO
#exclude %_datadir/%name/hconsole/release-notes.txt

%changelog
* Tue Nov 29 2022 Artyom Bystrov <arbars@altlinux.org> 2.4.1-alt2
- Add translation of description in desktop file

* Sat Aug 20 2022 Ilya Mashkin <oddity@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Sun Jul 24 2022 Ilya Mashkin <oddity@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Sat Aug 28 2021 Artyom Bystrov <arbars@altlinux.org> 2.3.1-alt1
- moving from srpms to Gear
- Update sources to version 2.3.1

* Wed Feb 06 2019 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1.1
- Rebuild with libreadline7.

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

