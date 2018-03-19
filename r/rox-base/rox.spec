%define base_name rox-filer
Name: rox-base
Version: 2.11
Release: alt1

Summary: ROX desktop enviroment
License: GNU GPL
Group: Graphical desktop/Other

Url: http://rox.sourceforge.net/
Source: http://prdownloads.sourceforge.net/%base_name/%base_name-%version.tar.bz2
Source1: rox-startup.sh
Source2: rox.desktop
Source3: rox.svg
Packager: Eugene Ostapets <eostapets@altlinux.ru>

Patch0: rox-i18n-standard-path.patch
Patch1: rox-images-standard-path.patch
Patch2: rox-user-config.patch
Patch3: rox-fix-help-path.patch

Patch50: rox-2.3-rootmenu.patch
Patch51: rox-2.3-workplace.patch
Patch52: rox-2.5-alt-DSO.patch
Patch53: rox-alt-set-system-locale-path.patch

# Automatically added by buildreq on Thu Oct 05 2006
BuildRequires: fontconfig imake libXt-devel libgtk+2-devel libxml2-devel xorg-cf-files pkgconfig 
BuildRequires: librsvg-utils

%description
ROX is a desktop environment, like GNOME, KDE and XFCE.  It is an attempt to bring some of the good features from RISC OS to Unix and Linux.
%prep
%setup -q -n %base_name-%version
#%%patch0 -p1
%patch1 -p1
#%%patch2 -p1
%patch3 -p1

#%%patch50 -p1
#%%patch51 -p1
%patch52 -p2
%patch53 -p2

rsvg-convert -w 48 -h 38 -f png -o rox.png %SOURCE3

%build
%__mkdir ROX-Filer/build
cd ROX-Filer/build
../src/configure \
	--enable-rox 
%make

%install
%__mkdir -p %buildroot%_libdir/rox/ROX-Filer
%__mkdir -p %buildroot/usr/{bin,share/{mime/packages,Choices,man/man1,rox/{images,help,ROX/MIME}}}
%__install -m 755 ROX-Filer/ROX-Filer %buildroot%_libdir/rox/ROX-Filer
%__install -m 755 ROX-Filer/AppRun %buildroot%_libdir/rox/ROX-Filer
%__install -m 644 rox.xml %buildroot%_datadir/mime/packages
%__install -m 644 rox.1 %buildroot%_mandir/man1
ln -s %buildroot%_mandir/man1/rox.1 %buildroot%_mandir/man1/ROX-Filer.1
%__install -m 755 Choices/MIME-types/application_postscript %buildroot%_datadir/Choices
%__install -m 755 Choices/MIME-types/text %buildroot%_datadir/Choices
%__install -m 755 Choices/MIME-types/text_html %buildroot%_datadir/Choices

#install languages
mkdir -p %buildroot%_datadir/locale
# Remove README from locale directory
rm -f ROX-Filer/Messages/README
cp -a ROX-Filer/Messages/* %buildroot%_datadir/locale

#install default theme
%__install -m 644 ROX-Filer/ROX/index.theme %buildroot%_datadir/rox/ROX
%__cp ROX-Filer/ROX/MIME/* %buildroot%_datadir/rox/ROX/MIME/
%__cp ROX-Filer/images/* %buildroot%_datadir/rox/images/


%__cp ROX-Filer/Help/*.html %buildroot%_datadir/rox/help
%__install -m 644 ROX-Filer/.DirIcon %buildroot%_libdir/rox/ROX-Filer
%__install -m 644 ROX-Filer/AppInfo.xml %buildroot%_libdir/rox/ROX-Filer
%__install -m 644 ROX-Filer/Options.xml %buildroot%_libdir/rox/ROX-Filer
%__install -m 644 ROX-Filer/style.css %buildroot%_libdir/rox/ROX-Filer
%__install -m 755 %SOURCE1 %buildroot%_bindir/rox
%__subst "s|@LIBDIR@|%_libdir|g" %buildroot%_bindir/rox

# Install icon and desktop file
install -Dm 0644 %SOURCE2 %buildroot%_desktopdir/rox.desktop
install -Dm 0644 %SOURCE3 %buildroot%_pixmapsdir/rox.svg
install -Dm 0644 rox.png %buildroot%_pixmapsdir/rox.png

%find_lang ROX-Filer

%files -f ROX-Filer.lang
%doc ROX-Filer/Help/README ROX-Filer/Help/TODO ROX-Filer/Help/Changes
%_bindir/*
%_libdir/rox/*
%_datadir/rox/*
%_datadir/mime/packages/*
%_datadir/Choices
%_mandir/man*/*
%_desktopdir/rox.desktop
%_pixmapsdir/rox.*

%changelog
* Mon Mar 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.11-alt1
- New version.
- Install desktop file and icon.
- Fix use locale.

* Fri Feb 28 2014 Andrey Cherepanov <cas@altlinux.org> 2.5-alt1.1.qa2
- Fixed build

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.5-alt1.1.qa1
- NMU: rebuilt for updated dependencies.

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Fixed build

* Thu Oct 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.5-alt1
- new version

* Fri Aug 12 2005 Eugene Ostapets <eostapets@altlinux.ru> 2.3-alt1
- new version

* Wed Aug 10 2005 Eugene Ostapets <eostapets@altlinux.ru> 2.2.0-alt1
- initial build 
