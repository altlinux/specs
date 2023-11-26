Name: vym
Version: 2.9.26
Release: alt1

Summary: QT based MindMap editor
Url: http://www.insilmaril.de/vym/
#Url; https://github.com/insilmaril/vym
Packager: Alex Karpov <karpov@altlinux.ru>

License: %gpl2only
Group: Office

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-2.8.7-alt-pdf_path.patch
Patch2: %name-2.9.22-alt-VYMBASEDIR.patch

Source1: %name.desktop

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-xdg

# Automatically added by buildreq on Sun Oct 29 2023
# optimized out: cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libglvnd-devel libgpg-error libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-svg libqt5-widgets libqt5-xml libsasl2-3 libssl-devel libstdc++-devel pkg-config python-modules python2-base python3 python3-base python3-dev qt5-base-devel qt5-tools sh5
BuildRequires: cmake libdbus-devel qt5-script-devel qt5-svg-devel qt5-tools-devel
%ifnarch %e2k ppc64le
BuildRequires: qt5-webengine-devel
%endif

# For PDF docs generation
BuildRequires: makeinfo texi2dvi texlive-dist

%description
VYM (View Your Mind) is a tool to generate and manipulate maps which show your
thoughts. Such maps can help you to improve your creativity and effectivity.
You can use them for time management, to organize tasks, to get an overview
over complex contexts.

%prep
%setup -q
%patch0 -p1

%patch1
%patch2

%build
%cmake -DCMAKE_INSTALL_DATAROOTDIR:PATH=%_datadir/vym
%cmake_build

#pushd lang
#for i in *.ts; do
#    lconvert-qt5 $i -o `basename $i .ts`.qm
#done
#popd

#pushd tex
#texi2dvi -p vym.tex    > /dev/null
#texi2dvi -p vym_es.tex > /dev/null
#texi2dvi -p vym_fr.tex > /dev/null
#popd

%install
%cmake_install

install -D -m0644 doc/%name.1.gz %buildroot%_man1dir/%name.1.gz
install -D -m0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
sed -e 's#ICONDIR#%_datadir/%name/icons#' -i %buildroot%_desktopdir/%name.desktop

#mkdir %buildroot%_datadir/%name/lang/
#pushd lang
#for i in *.qm; do
#    install -D -m0664 $i %buildroot%_datadir/%name/lang/$i
#done
#popd

#mkdir -p %buildroot%_datadir/%name/doc/
#pushd tex
#for i in *.pdf; do
#    install -D -m0644 $i %buildroot%_datadir/%name/doc/$i
#done
#popd


%files
%doc README.md LICENSE.txt

%_bindir/%name
%_man1dir/%{name}*

%_datadir/%name/*
%exclude %_datadir/%name/scripts
%exclude %_datadir/%name/man

%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_xdgmimedir/packages/*


%changelog
* Sun Nov 26 2023 Nikolay A. Fetisov <naf@altlinux.org> 2.9.26-alt1
- New version

* Thu Jun 17 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.8.8-alt1
- New version

* Wed Jun 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.8.7-alt1
- New version

* Sat Aug 17 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.7.1-alt1
- New version

* Thu May 09 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.7.0-alt1
- New version

* Sat Nov 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.6.11-alt1
- New version

* Sun May 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.6.8-alt1
- New version

* Mon May 08 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.6.0-alt1
- New version
- Build with Qt5

* Wed Jan 09 2013 Alex Karpov <karpov@altlinux.ru> 2.2.4-alt1
- new version

* Tue Jul 03 2012 Alex Karpov <karpov@altlinux.ru> 2.2.2-alt1
- new version

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

