# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: mpdscribble
Version: 0.18.1
Release: alt2

Summary: Audioscrobbler client for mpd
License: GPLv2+
Group: Sound
Url: http://mpd.wikia.com/wiki/Client:Mpdscribble
Packager: Slava Semushin <php-coder@altlinux.ru>

Source: http://downloads.sourceforge.net/musicpd/%name-%version.tar.bz2
Patch0: mpdscribble-alt-src-no_id3_tags.patch

BuildRequires: glib2-devel libsoup-devel pkg-config

%description
mpdscribble is a music player daemon client which submits information about
tracks being played to audioscrobbler (http://last.fm/).

%prep
%setup

# don't build with -pedantic-errors flag because it lead to errors in
# system headers
sed -i 's| -pedantic-errors||' configure.ac

# don't build with -Wcast-qual due to warnings from libsoup
# (https://bugzilla.gnome.org/show_bug.cgi?id=600315)
sed -i '/-Wcast-qual/d' configure.ac

# don't try to install documenation to non-versioned directory under
# /usr/share/doc
sed -i '/^doc_DATA/d' Makefile.am

# don't try to install config to /etc. We will pack it as example
# manually.
sed -i '/^dist_sysconf_DATA/d' Makefile.am

%patch0 -p2

%build
%autoreconf
%configure --enable-werror
%make_build --silent --no-print-directory

%install
%makeinstall --silent --no-print-directory

%files
%_bindir/%name
%_man1dir/%name.1.*
%doc AUTHORS NEWS README doc/%name.conf

%changelog
* Sun Nov 15 2009 Slava Semushin <php-coder@altlinux.ru> 0.18.1-alt2
- Fixed build (compile without -Wcast-qual)

* Sat Sep 05 2009 Slava Semushin <php-coder@altlinux.ru> 0.18.1-alt1
- Updated to 0.18.1

* Thu Jul 09 2009 Slava Semushin <php-coder@altlinux.ru> 0.18-alt1
- Updated to 0.18

* Tue May 26 2009 Slava Semushin <php-coder@altlinux.ru> 0.17-alt3
- Fixed build with automake 1.11

* Fri May 08 2009 Slava Semushin <php-coder@altlinux.ru> 0.17-alt2
- Fixed build with gcc4.4

* Sun Mar 08 2009 Slava Semushin <php-coder@altlinux.ru> 0.17-alt1
- Updated to 0.17

* Sat Jan 24 2009 Slava Semushin <php-coder@altlinux.ru> 0.16-alt1
- Updated to 0.16

* Thu Jan 08 2009 Slava Semushin <php-coder@altlinux.ru> 0.15-alt1
- Updated to 0.15
- Build with internal libmpd for a while
- Updated Source, Url and License tags

* Wed Oct 15 2008 Slava Semushin <php-coder@altlinux.ru> 0.2.12-alt4.1
- Rebuild with libmpd 0.16.1

* Sat Aug 09 2008 Slava Semushin <php-coder@altlinux.ru> 0.2.12-alt4
- Rebuild with libsoup2.4 (#21)
- Build with system libmpd (#10)

* Sat Aug 02 2008 Slava Semushin <php-coder@altlinux.ru> 0.2.12-alt3
- Using -Werror flag for compiler by default (#24)
- Fixed typo in --help output (#25)
- Fixed crash when we hit Ctrl+C (#26)
- Added support for files without tags (#27)
- Optimize BuildRequires

* Mon Jul 28 2008 Slava Semushin <php-coder@altlinux.ru> 0.2.12-alt2
- Fixed memory corruption during parse config/cache files (#4, #14, #23)
- Fixed paths to configuration files in man page (#7, deb #482485)
- Fixed time in log file (#17)

* Mon Jul 28 2008 Slava Semushin <php-coder@altlinux.ru> 0.2.12-alt1
- New maintainer
- Updated to 0.2.12 (Closes: #10582)
- Fixed typo in man page about default value of sleep parameter (#3)
- Enabled _unpackaged_files_terminate_build
- More proper License tag
- Spec cleanup

* Fri Aug 25 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.10-alt1.2
- fix summary (thanks to mike@)

* Wed Aug 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.10-alt1.1
- package setup.sh

* Sun May 28 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.10-alt1
- 0.2.10

* Sun May 28 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.8-alt1
- 0.2.8

* Mon May 01 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.7-alt2
- fix buildrequires
- fix building with --as-needed
- fix crash when running without mpd

* Thu Feb 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.7-alt1
- initial build
