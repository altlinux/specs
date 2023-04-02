Name: geany-plugins
Version: 1.38
Release: alt2
%define geany_ver 1.38

Summary: Plugins for Geany

License: GPLv2
Group: Development/Tools
Url: http://plugins.geany.org/

Source: %name-%version.tar.bz2

BuildRequires(pre): geany geany-devel intltool
# Hack out self-providing symbols
%add_python_req_skip app
%add_python_req_skip dialogs
%add_python_req_skip document
%add_python_req_skip encoding
%add_python_req_skip filetypes
%add_python_req_skip glog
%add_python_req_skip highlighting
%add_python_req_skip keybindings
%add_python_req_skip main
%add_python_req_skip msgwindow
%add_python_req_skip navqueue
%add_python_req_skip prefs
%add_python_req_skip project
%add_python_req_skip scintilla
%add_python_req_skip search
%add_python_req_skip ui_utils
%add_python_req_skip templates

Requires: geany-plugins-vc

# Automatically added by buildreq on Mon Nov 09 2020
# optimized out: at-spi2-atk fontconfig geany glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libenchant2-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgpg-error-devel libgtk+3-devel libharfbuzz-devel libjavascriptcoregtk4-devel liblua5.1-devel libpango-devel libsoup-devel libwayland-client libwayland-cursor libwayland-egl perl perl-XML-Parser pkg-config python-modules python2-base python3 python3-base sh4 shared-mime-info vala xorg-proto-devel
BuildRequires: cppcheck geany-devel intltool libcheck-devel libctpl-devel libgit2-devel libgpgme-devel libgtkspell3-devel libvte3-devel libwebkit2gtk-devel libxml2-devel python3-dev

BuildRequires: liblua5.1-devel

%description
This is Geany plugin collection

%package common
Group: Development/Tools
Requires: geany = %geany_ver
Summary: Localization and other platform independent stuff of geany-plugins
BuildArch: noarch

%description common
Common files of geany-plugins, including localization

%package vc
Group: Development/Tools
Requires: geany-plugins-common = %version-%release
Summary: Geany VC integration plugin

%description vc
Various VCS integration (Git, SVN, ...) for Geany

%prep
%setup
sed -i '/^geanyluadir/s@.*@geanyluadir = %_libdir/geany@' geanylua/Makefile.am

%build
export PYTHON_VERSION=2
%autoreconf
%configure
%make_build

%install
%makeinstall_std --silent --no-print-directory
%find_lang %name

%files
%doc %_defaultdocdir/%name
%_libdir/geany/*
%_libdir/lib*
%_datadir/geany-plugins/*
#dir #_libexecdir/geany-plugins
#_libexecdir/geany-plugins/*
#_iconsdir/hicolor/*/apps/*
%exclude %_libdir/geany/geanyvc*
%exclude %_libdir/geany/*.la
#exclude %_libdir/geany-plugins/*/*.la

%files common -f %name.lang
%files vc
%_libdir/geany/geanyvc*
%exclude %_libdir/geany/*.la

%changelog
* Sun Apr 02 2023 Yuri N. Sedunov <aris@altlinux.org> 1.38-alt2
- cherry-picked "Simplify libgit2 version checks" (668f5d0) and
  "Add support for libgit2 1.4" (5d9f1bc),
  rebuilt with libgit2-1.6.3

* Mon May 23 2022 Fr. Br. George <george@altlinux.ru> 1.38-alt1
- Autobuild version bump to 1.38

* Fri May 07 2021 Fr. Br. George <george@altlinux.ru> 1.37-alt2
- Build with geany-1.37.1

* Sat Nov 07 2020 Fr. Br. George <george@altlinux.ru> 1.37-alt1
- Autobuild version bump to 1.37
- Switch to GTK3

* Wed Jun 24 2020 Michael Shigorin <mike@altlinux.org> 1.36-alt2
- Fix ftbfs (specify python version explicitly)

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 1.36-alt1
- Autobuild version bump to 1.36

* Wed May 22 2019 Fr. Br. George <george@altlinux.ru> 1.35-alt1
- Autobuild version bump to 1.35

* Wed Feb 27 2019 Fr. Br. George <george@altlinux.ru> 1.34.1-alt0.1
- Autobuild version bump to 1.34
- Build with Geany 1.34.1

* Mon Mar 19 2018 Fr. Br. George <george@altlinux.ru> 1.33-alt1
- Autobuild version bump to 1.33

* Tue Sep 26 2017 Fr. Br. George <george@altlinux.ru> 1.31-alt2
- Rebuild with new libgit2

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 1.31-alt1
- Autobuild version bump to 1.31

* Fri Mar 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.30-alt1.1
- rebuilt against libgit2.so.25

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 1.30-alt1
- Autobuild version bump to 1.30

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1.1
- NMU: rebuild with new lua

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 1.28-alt1
- Autobuild version bump to 1.28

* Tue Jul 05 2016 Fr. Br. George <george@altlinux.ru> 1.27-alt1
- Autobuild version bump to 1.27
- Build additional modules

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 1.24-alt1
- Autobuild version bump to 1.24

* Thu May 23 2013 Fr. Br. George <george@altlinux.ru> 1.23-alt2
- Rebuild with geany 1.23.1

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 1.23-alt1
- Autobuild version bump to 1.23
- GDB and noarch plugins vanished

* Thu Jul 26 2012 Fr. Br. George <george@altlinux.ru> 1.22-alt1
- Autobuild version bump to 1.22
- Update BuildRequires for more plugins to build

* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 0.21.1-alt2
- Remove release dependency

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 0.21.1-alt1
- Autobuild version bump to 0.21.1

* Fri Jan 14 2011 Fr. Br. George <george@altlinux.ru> 0.20-alt1
- Autobuild version bump to 0.20
- Add unpackaged files

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt4
- trying to fix build

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt3
- split by plugins

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt2
- first build for ALT Linux
