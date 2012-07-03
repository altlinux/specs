%define origname jimmac

Name: x-cursor-theme-%origname
Version: 20030906
Release: alt2

Summary: Jimmac is a nice X11 mouse cursor theme
License: GPL
Group: System/XFree86

Url: http://kde-look.org/content/show.php?content=6550
Source: 6550-Jimmac.tar.gz
Packager: Michael Shigorin <mike@altlinux.ru>

BuildArch: noarch

Summary(ru_RU.KOI8-R): Jimmac -- симпатичная тема курсоров X11
Summary(uk_UA.KOI8-U): Jimmac -- симпатична тема курсор╕в X11

%description
X11 mouse theme based on Jimmac's cursors - see
http://jimmac.musichall.cz/i.php3?ikony=71

%description -l ru_RU.KOI8-R
Тема графических курсоров для X11, основанная на Jimmac
(см. http://jimmac.musichall.cz/i.php3?ikony=71)

%description -l uk_UA.KOI8-U
Тема граф╕чних курсор╕в для X11, зроблена на баз╕ Jimmac
(див. http://jimmac.musichall.cz/i.php3?ikony=71)

%prep
%setup -q -n Jimmac

%build
%__cat > README.ALT << __EOF__
mkdir -p ~/.icons/default
cat >> ~/.icons/default/index.theme << EOF
[Icon Theme]
Inherits=jimmac
EOF
__EOF__

%install
%__install -d %buildroot%_iconsdir/
%__cp -a %origname/ %buildroot%_iconsdir/

%files
%_iconsdir/%origname
%doc README* default/index.theme

%changelog
* Mon Jan 31 2005 Michael Shigorin <mike@altlinux.ru> 20030906-alt2
- fixed package architecture

* Tue Aug 03 2004 Michael Shigorin <mike@altlinux.ru> 20030906-alt1
- built for ALT Linux

