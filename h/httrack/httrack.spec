%def_enable shared
%def_enable static

%define Name HTTrack
%define lname lib%name
%define origver 3.45-3

Name: httrack
Version: 3.45.3
Release: alt1

Summary: An easy-to-use offline browser utility
License: %gpl2plus
Group: Networking/File transfer

Url: http://www.httrack.com
Source0: %name-%version.tar.gz
Source1: %name.conf
Patch: httrack-3.47.3-alt-makefile.patch
Packager: Led <led@altlinux.ru>

%{?_enable_shared:Requires: %lname = %version-%release}
BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Tue Mar 04 2008
BuildRequires: gcc-c++ zlib-devel ImageMagick

%set_automake_version 1.10
BuildRequires: desktop-file-utils

%description
%Name is an easy-to-use offline browser utility. It allows you to
download a World Wide website from the Internet to a local directory,
building recursively all directories, getting html, images, and other
files from the server to your computer. %Name arranges the original
site's relative link-structure. Simply open a page of the "mirrored"
website in your browser, and you can browse the site from link to link,
as if you were viewing it online. %Name can also update an existing
mirrored site, and resume interrupted downloads. %Name is fully
configurable, and has an integrated help system.


%if_enabled shared
%package -n %lname
Summary: Shared library for %Name
Group: System/Libraries

%description -n %lname
This package contains shared library for %Name.
%endif


%package -n %lname-devel
Summary: Development files for %Name
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
This package contains development files required for packaging
%Name-based software.


%if_enabled static
%package -n %lname-devel-static
Summary: Static libraries for %Name
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
This package contains development libraries required for packaging
statically linked %Name-based software.
%endif


%package -n web%name
Summary: Offline browser - %name and htsserver frontend
Group: Networking/File transfer
Requires: %name = %version-%release

%description -n web%name
Offline browser: copy websites to a local directory.


%prep
%setup
%patch -p1


%build
ACLOCAL="aclocal -I m4" %autoreconf
%configure %{subst_enable shared} %{subst_enable static}
%make_build
convert -depth 8 html/server/div/web%name.xpm web%{name}_48.png
for s in 32 24 16; do
    convert -resize ${s}x$s -depth 8 html/server/div/web%name.xpm web%{name}_$s.png
done


%install
%make_install DESTDIR=%buildroot install
mv %buildroot%_docdir/%name{,-%version}
install -m 0644 AUTHORS README %buildroot%_docdir/%name-%version/
install -D -m644 %SOURCE1 %buildroot/%_sysconfdir/%name.conf
for s in 48 32 24 16; do
    install -D -m 0644 {web%{name}_$s,%buildroot%_iconsdir/hicolor/${s}x$s/apps/web%name}.png
done
rm %buildroot%_libdir/%name/*.la
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=FileTransfer \
	%buildroot%_desktopdir/WebHTTrack.desktop


%files
%_docdir/%name-%version
%_bindir/%name
%_datadir/%name
%exclude %_datadir/%name/libtest
%exclude %_datadir/%name/icons
%_man1dir/%name.1*
%config(noreplace) %_sysconfdir/%name.conf


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%_libdir/%name/*.so.*
%endif


%files -n %lname-devel
%_includedir/%name
%if_enabled shared
%_libdir/*.so
%_libdir/%name/*.so
%endif


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%_libdir/%name/*.a
%endif


%files -n web%name
%_bindir/*
%exclude %_bindir/%name
%_man1dir/*
%exclude %_man1dir/%name.1*
%_datadir/%name/icons
%_pixmapsdir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*


%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 3.45.3-alt1
- 3.45.3 (moved back to srpm)

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.43.9-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for webhttrack
  * postclean-03-private-rpm-macros for the spec file

* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 3.43.9-alt1
- 3.43-9C (maybe closes #9356)
- patch teardown

* Wed Dec 09 2009 Michael Shigorin <mike@altlinux.org> 3.43.7-alt1.1
- built for Sisyphus (again), thanks led@

* Fri Aug 28 2009 Led <led@altlinux.ru> 3.43.7-alt1
- 3.43.7

* Sun May 24 2009 Led <led@altlinux.ru> 3.43.5-alt1
- 3.43.5

* Sat Feb 28 2009 Led <led@altlinux.ru> 3.43.3-alt1
- 3.43.3

* Sun Feb 15 2009 Led <led@altlinux.ru> 3.43.2-alt1
- 3.43.2
- cleaned up spec

* Sat Nov 08 2008 Led <led@altlinux.ru> 3.43.1-alt1
- 3.43.1

* Sun Aug 10 2008 Led <led@altlinux.ru> 3.42.3-alt3
- fixed *.desktop

* Sat Aug 09 2008 Led <led@altlinux.ru> 3.42.3-alt2
- fixed *.desktop

* Thu Jul 31 2008 Led <led@altlinux.ru> 3.42.3-alt1
- 3.42.3

* Fri Apr 04 2008 Led <led@altlinux.ru> 3.42-alt3
- added post scripts for update menus

* Fri Mar 21 2008 Led <led@altlinux.ru> 3.42-alt2
- 3.42-2

* Tue Mar 04 2008 Led <led@altlinux.ru> 3.42-alt1
- 3.42
- fixed %%changelog
- cleaned up spec
- fixed License

* Wed Apr 19 2006 Andrey Semenov <mitrofan@altlinux.ru> 3.40.2-alt1
- 3.40.2

* Sat Jan 28 2006 Andrey Semenov <mitrofan@altlinux.ru> 3.40-alt1
- new version

* Mon Feb 14 2005 Andrey Semenov <mitrofan@altlinux.ru> 3.33-alt1
- 3.33

* Tue May 11 2004 Andrey Semenov <mitrofan@altlinux.ru> 3.32.2-alt1
- new version
- Broken engine on 64-bit archs

* Mon Apr 12 2004 Andrey Semenov <mitrofan@altlinux.ru> 3.32-alt1
- new version
- Fixed: css and js files were not parsed!
- Fixed: again broken file:// (infinite loops with local crawls)
- Fixed: Bandwidth limiter more gentle with low transfer rate
- Fixed: external wrappers were not called during updates/continue
- New: additional callback examples
- Fixed: overflow in unzip.c fixed
- New: tests are now cached for better performances!
- New: %%r (protocol) option for user-defined structure

* Mon Mar 15 2004 Andrey Semenov <mitrofan@altlinux.ru> 3.31-alt1
- new version
- bugs fixed
- experimental categories implemented
- new cache format (ZIP file)
- .m3u files now crawled
- .aam files now crawled
- full HTTP headers are now stored in cache

* Wed Dec 10 2003 Andrey Semenov <mitrofan@altlinux.ru> 3.30-alt2
- removed *.la files

* Sun Oct 12 2003 Andrey Semenov <mitrofan@altlinux.ru> 3.30-alt1
- New: Webhttrack, a linux/unix/bsd Web GUI for httrack
- New: "URL hack" feature
- New: HTTP-headers charset is now propagated in the html file
- New: loadable external engine callbacks
- New: Experimental ".mht" archives format

* Wed Apr 02 2003 Andrey Semenov <mitrofan@altlinux.ru> 3.23-alt1
- First version of RPM package.
