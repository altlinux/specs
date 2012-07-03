Packager: Repocop Q. A. Robot <repocop@altlinux.org>
Name: wmsystray
Version: 0.1.1
Release: alt1.1.qa2

Summary: System tray "notification area" dockapp
License: GPL
Group: Graphical desktop/Other
Url: http://kai.vm.bytemark.co.uk/~arashi/wmsystray/
Source0: http://kai.vm.bytemark.co.uk/~arashi/wmsystray/release/%name-%version.tar.bz2
Source1: %name.desktop
Patch0: %name-cflags.patch
Patch1: %name-gcc-3.4.patch
Patch2: %name-xembed-fix.patch

# Automatically added by buildreq on Wed Oct 05 2005
BuildRequires: libXt-devel libXext-devel libXpm-devel
BuildRequires: desktop-file-utils

%description
wmsystray is meant to be used as a Window Maker dock applet. wmsystray
provides a notification area, or "system tray", in a manner compliant with
freedesktop.org's System Tray Protocol Specification. This allows wmsystray
to serve as a system tray area for recent GNOME and KDE applications, and
should work for applications from GNOME 2.x and later or KDE 3.x and later.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
EXTRAFLAGS="%optflags" %make_build

%install
%makeinstall
mkdir -p %buildroot%_datadir/applications
install -pm644 %SOURCE1 %buildroot%_datadir/applications

mkdir -p $RPM_BUILD_ROOT%_menudir
cat << EOF > $RPM_BUILD_ROOT%_menudir/%name
?package(%name):\
needs="x11"\
section="Applications/Accessibility"\
title="wmsystray"\
longtitle="System tray \"notification area\" dockapp"\
command="wmsystray"
EOF
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=X-Desktop \
	%buildroot%_desktopdir/wmsystray.desktop

%files 
%doc AUTHORS README HACKING
%_bindir/%name
%_menudir/%name
%_datadir/applications/*.desktop
%_man1dir/*

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.1-alt1.1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for wmsystray
  * postclean-03-private-rpm-macros for the spec file

* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1.1.qa1
- Disclosure xorg-devel build requirement

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmsystray

* Thu Oct 05 2005 LAKostis <lakostis at altlinux.ru> 0.1.1-alt1
- First build for Sisyphus.

