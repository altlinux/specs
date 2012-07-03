# norootforbuild

Name: littlewizard
Summary: Development Environment for Children
Version: 1.2.2
Release: alt2
License: GPL
Group: Games/Educational
Source0: %name-%version.tar.bz2
# wget -nH -p -k http://littlewizard.sourceforge.net/tutorial.html
Source1: tutorial.tar
Patch: littlewizard-desktop.alt.patch
Packager: Fr. Br. George <george@altlinux.ru>
Url: http://littlewizard.sourceforge.net/

# Automatically added by buildreq on Mon Jul 21 2008
BuildRequires: gcc-c++ libgtk+2-devel libxml2-devel

%description
Little Wizard is created especially for primary school children. It allows to
learn using main elements of present computer languages, including: variables,
expressions, loops, conditions, logical blocks. Every element of language is
represented by an intuitive icon. It allows program Little Wizard without
using keyboard, only mouse.

%package devel
Summary: Development headers and files for %name
Group: Development/C++
Requires: %name = %version

%description devel
Headers and development files for %name

%prep
%setup -q
%patch

%build
%configure

%make_build

mkdir tutorial
tar -C tutorial -x -f %SOURCE1

%install
%makeinstall
install -D %buildroot%_pixmapsdir/%name/%name-icon.png %buildroot%_niconsdir/%name.png
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO tutorial/*
%_bindir/%name
%_bindir/littlewizardtest
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/icons/gnome/48x48/mimetypes/gnome-mime-application-x-%name.png
%_datadir/icons/gnome/scalable/mimetypes/gnome-mime-application-x-%name.svg
%_datadir/mime/packages/%name.xml
%_datadir/pixmaps/%name
%_niconsdir/%name.png
%_libdir/liblanguage.so.*
%_libdir/liblw.so.*

%files devel
%_includedir/*
%_libdir/liblanguage.so
%_libdir/liblw.so

%changelog
* Thu Oct 08 2009 Fr. Br. George <george@altlinux.ru> 1.2.2-alt2
- Repocop warnings fixed

* Sat Sep 20 2008 Fr. Br. George <george@altlinux.ru> 1.2.2-alt1
- Version up
+ Tutorial added

* Sun Jul 20 2008 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Initial build from OpenSuSE

* Wed Jul  2 2008 kirill.kirillov@gmail.com
- added littlewizard-1.2.0-fix-mime-type.patch
* Tue Jul  1 2008 kirill.kirillov@gmail.com
- Update to the next major release 1.2.0
  + New control flow commands "else", "break", "continue", "step"
  + Command "read" for user interactivity
  + Command "concatenate" for concatenating the strings
  + Command "length" for obtaining the length of the string or size of an array
  + Command "rand" behaves like in Pascal, it now generates values between 0 <= x < v
  + Boolean values (but dynamic "C" like casting still possible)
  + Smart comparation of the values, numerical or lexigraphical depending on the content.
  + Remarks
  + Mostly rewritten parser and interpreter part
  + Possibility to set initial position and direction of the wizard
  + Moving tiles on world board using a "SHIFT" key
  + Mime support (project files have own icon and can be loaded from the browser)
  + Memory leaks fixes and various optimizations, etc
- Dropped gcc 4.3 patch
* Sun Jun 29 2008 Andrea Florio andrea@opensuse.org
- added gcc 4.3 patch
- added -devel package
- added -debuginfo
- made rpmlint happy, now build on openSUSE 11.0
* Sat Jul 28 2007 kirill.kirillov@gmail.com
- Update to the bug fix release 1.1.5
* Fri Jan 12 2007 Piotr Pacholak <obi.gts@gmail.com>
- BR: gcc-c++
* Fri Jan 12 2007 Piotr Pacholak <obi.gts@gmail.com>
- BR: libxml2-devel
* Fri Nov 17 2006 Piotr Pacholak <obi.gts@gmail.com>
- up to 1.1.4
* Wed May 24 2006 Piotr Pacholak <obi.gts@gmail.com>
- Rebuild
* Thu May 18 2006 Piotr Pacholak <obi.gts@gmail.com>
- Rebuild
* Wed May 17 2006 Piotr Pacholak <obi.gts@gmail.com>
- initial release
