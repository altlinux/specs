Name: vym
Version: 2.2.0
Release: alt1

Summary: QT based MindMap editor
Url: http://sourceforge.net/projects/vym
Packager: Alex Karpov <karpov@altlinux.ru>

License: GPL
Group: Office

Source: %name-%version.tar

Provides: vym

# Automatically added by buildreq on Thu Aug 25 2011
# optimized out: fontconfig libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libstdc++-devel
BuildRequires: gcc-c++ glibc-devel-static phonon-devel

%description
VYM (View Your Mind) is a tool to generate and manipulate maps which show your
thoughts. Such maps can help you to improve your creativity and effectivity.
You can use them for time management, to organize tasks, to get an overview
over complex contexts.

%prep
%setup -q
subst 's,/doc/packages/vym,/doc/%name,g' %name.pro
subst 's,= tex/vym.pdf,= doc/vym.pdf,g' %name.pro


%build
export QTDIR=%_qt4dir
export PATH=$PATH:$QTDIR/bin
qmake PREFIX=%prefix vym.pro -after DESTDIR=%buildroot
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
# remove unneeded scripts
#rm %buildroot%_datadir/%name/scripts/update-bookmarks
#rm %buildroot%_datadir/%name/scripts/release-mac

# menu
mkdir -p %buildroot%_desktopdir
cat << EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Name=VYM
GenericName=MindMap Editor
Comment=View Your Mind
Exec=vym
Terminal=false
Categories=Application;Office;
Type=Application
Icon=%_datadir/%name/icons/%name.png
EOF


%files
%_defaultdocdir/%name 
%_bindir/%name
%_datadir/%name/*
%exclude %_datadir/%name/scripts
%_desktopdir/%name.desktop

%changelog
* Thu Jun 21 2012 Alex Karpov <karpov@altlinux.ru> 2.2.0-alt1
- new version

* Mon Jan 30 2012 Alex Karpov <karpov@altlinux.ru> 2.0.6-alt1
- new version

* Tue Dec 13 2011 Alex Karpov <karpov@altlinux.ru> 2.0.3-alt1
- new version

* Mon Sep 26 2011 Alex Karpov <karpov@altlinux.ru> 1.99.00-alt1
- new version

* Thu Aug 25 2011 Alex Karpov <karpov@altlinux.ru> 1.13.39-alt1
- new version

* Tue Mar 01 2011 Alex Karpov <karpov@altlinux.ru> 1.12.8-alt1
- new version

* Mon May 17 2010 Alex Karpov <karpov@altlinux.ru> 1.12.7-alt1.1
- closing #23484
    + updated build requirements
    + removed unneeded scrips

* Wed Mar 31 2010 Alex Karpov <karpov@altlinux.ru> 1.12.7-alt1
-new version 

* Tue Dec 29 2009 Alex Karpov <karpov@altlinux.ru> 1.12.6-alt1
- new version
    + removed obsoleted stuff

* Mon Dec 01 2008 Alex Karpov <karpov@altlinux.ru> 1.12.2-alt1
- new version

* Mon Aug 18 2008 Alex Karpov <karpov@altlinux.ru> 1.12.0-alt1
- 1.12.0
    + spec cleanup

* Mon Oct 01 2007 Alex Karpov <karpov@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Tue Sep 25 2007 Alex Karpov <karpov@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri Jun 15 2007 Alex Karpov <karpov@altlinux.ru> 1.8.1-alt5.1
- initial real (not local) build for Sisyphus

* Mon Apr 17 2007 Andrii Dobrovol`s`kii <dobr@altlinux.org> 1.8.1-alt5
- Change doc path

* Thu Apr 12 2007 Andrii Dobrovol`s`kii <dobr@iop.kiev.ua> 1.8.1-alt4
- Other Requires and Provides, and doc files (Thanks to I.Zubkov and
  Glodin S.V.)

* Thu Apr 12 2007 Andrii Dobrovol`s`kii <dobr@iop.kiev.ua> 1.8.1-alt3
- Requires zip for saving

* Thu Apr 5 2007 Andrii Dobrovol`s`kii <dobr@iop.kiev.ua> 1.8.1-alt2
- with menu

* Thu Apr 5 2007 Andrii Dobrovol`s`kii <dobr@iop.kiev.ua> 1.8.1-alt1
- with the spec corrections from Yuriy Kashirin

* Fri Mar 30 2007 Andrii Dobrovol`s`kii <dobr@iop.kiev.ua> 1.8.1-alt0
- initial build for ALT Linux (Sisyphus)

