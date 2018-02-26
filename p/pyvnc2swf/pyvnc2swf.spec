# SPEC-file for pyvnc2swf
#

%define version 0.9.5
%define release alt2

Name: pyvnc2swf
Version: %version
Release: %release.1

Summary: A VNC session recorder to Flash movie
Summary(ru_RU.UTF-8): Утилита для записи сессии VNC в файл Flash

License: %gpl2plus
Group: Graphics
URL: http://www.unixuser.org/~euske/vnc2swf/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name.bin
Source2: %name-play
Source3: %name-edit
Patch0:  %name-0.9.5-alt-recordwin.patch

BuildRequires(pre): rpm-build-licenses

Requires: python >= 2.4, python-module-pygame >= 1.6

%description
pyvnc2swf is a screen recorder for Flash movie. It captures
screen motion through  VNC protocol and converts  it into a
Shockwave Flash (SWF) file.

%description -l ru_RU.UTF-8
pyvnc2swf - утилита для записи экрана в Flash-ролик. Она
захватывает состояние экрана через протокол VNC и форматирует его
в файл в формате Shockwave Flash (SWF).

%package recordwin
Summary: A wrapper program for pyvnc2swf to record a specific window
Summary(ru_RU.UTF-8): Скрипт для записи из pyvnc2swf отдельного окна
Group: Graphics
Requires: %name = %version-%release
Requires: x11vnc, xwininfo
AutoReqProv: yes

%description recordwin
Script recordwin.sh allows you to record a specific window
in the current screen instead of the entire display.  This
is a wrapper program for pyvnc2swf and x11vnc.

%description recordwin -l ru_RU.UTF-8
Скрипт recordwin.sh позволяет записывать отдельное окно на
текущем экране  вместо захвата  целиком всего  экрана.  Он
представляет собой оболочку для вызова pyvnc2swf и x11vnc.

%add_python_req_skip pymedia

%prep
%setup
%patch0

mv -f -- LICENCE.TXT LICENCE.TXT.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENCE) LICENCE

%build

%install
mkdir -p -- %buildroot%_datadir/%name
cp -- pyvnc2swf/*.py %buildroot%_datadir/%name

mkdir -p -- %buildroot%_bindir

install -m 0755 -- %SOURCE1 %buildroot%_bindir/%name
install -m 0755 -- %SOURCE2 %buildroot%_bindir/%name-play
install -m 0755 -- %SOURCE3 %buildroot%_bindir/%name-edit
cp -- bin/recordwin.sh %buildroot%_bindir 


%files
%doc README.txt docs/changes* docs/index* docs/pyvnc2swf*
%doc --no-dereference LICENCE

%_datadir/%name/*.py

%_bindir/%{name}*

%files recordwin
%doc docs/recordwin.html
%_bindir/recordwin.sh

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt2.1
- Rebuild with Python-2.7

* Tue Nov 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt2
- Rebuilt with python 2.6 (build for sisyphus)

* Tue Nov 24 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.5-alt2
- Rebuild with python 2.6

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.5-alt1
- New version 0.9.5

* Mon May 07 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.3-alt2
- Fix paths for x86_64

* Mon May 07 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.3-alt1
- New version 0.9.3
  - Replace crippled_des.py with d3des.py. (License issue)

* Fri Apr 27 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.2-alt1
- New version 0.9.2
  - FLV support added
- Fix paths for x86_64

* Thu Apr 19 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.1-alt1
- New version 0.9.1
  - More intuitive UI
  - Fixed PyMedia related bugs
  - Fixed MP3 related bugs
  - Disable the movie scaling by default
  - A password file must be encrypted
- Fix for #10252 (missed dependency on python-modules-tkinter)
- Skip automatic dependency to pymedia (non-existing in Sisyphus)

* Thu Aug 31 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.2-alt1
- New version 0.8.2
  - Problem with RealVNC is fixed
  - Cursor color bug and vnc conversion bug is fixed
- Fix for #9880

* Mon Nov 21 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.0-alt1
- Updating to the version 0.8.0

* Sun Nov 20 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.2-alt1
- Updating to the version 0.7.2
-- Adding documentation in doc/*.html files
-- Adding recordwin.sh script for
- Movind recordwin.sh to a separate package due to dependencies of x11vnc.

* Mon Sep 05 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.4-alt1
- Initial build for ALTLinux Sisyphus

* Sun Sep 04 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.4-alt0.1
- wrapper scripts cleanup

* Sun Sep 04 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.4-alt0
- New version 0.6.4
- spec cleanup

* Tue Aug 09 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.3-alt0
- Initial build

