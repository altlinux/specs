Name: normalize
Version: 0.7.7
Release: alt2

Summary: A tool for adjusting the volume of WAV files to a standard level
License: GPL
Group: Sound
Url: http://normalize.nongnu.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://savannah.nongnu.org/download/normalize/%name-%version.tar

Patch0: compressed-wav-files.dpatch
Patch1: fix-flac.dpatch
Patch2: alt-configure-fix.patch

Requires: lame mp3info mpg123 vorbis-tools

# manually removed: gcc-fortran 
# Automatically added by buildreq on Tue Sep 20 2011
# optimized out: glib-devel gtk+ libgfortran-devel libstdc++-devel
BuildRequires: flac gcc-c++ gtk+-devel lame libaudiofile-devel libmad-devel madplay vorbis-tools

%description
normalize is a tool for adjusting the volume of wave files to a
standard level.  This is useful for things like creating mixed CD's
and mp3 collections, where different recording levels on different
albums can cause the volume to vary greatly from song to song.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p2
touch AUTHORS ChangeLog

%build
%autoreconf
%configure --with-mad --with-audiofile
%make_build

%install
%makeinstall_std
ln -s normalize-mp3.1 %buildroot%_man1dir/normalize-ogg.1

%find_lang %name

%files -f %name.lang
%doc NEWS README TODO THANKS
%_bindir/normalize
%_bindir/normalize-ogg
%_bindir/normalize-mp3
%_man1dir/*

%changelog
* Tue Sep 20 2011 Vitaly Lipatov <lav@altlinux.ru> 0.7.7-alt2
- update buildreqs
- add compressed wav fix, flac write support fix (thanks, Mandriva!)
- fix build with new libaudiofile without audiofile-config

* Sat Dec 27 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.7-alt1
- cleanup spec
- add normalize-ogg man as link to normalize-mp3 (fix #8152)

* Tue Jan 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.7-alt0.1
- new bugfix version 0.7.7, change packager
- update buildreq, fix URL, Source URL
- disable xmms plugin build (due gtk1)

* Mon Sep 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Sat May 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Tue Apr 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.3-alt1
- 0.7.3
- xmms-normalize2 package

* Mon Feb 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.2-alt1
- 0.7.2
- xmms-normalize package. Replace or not libnormvol.so???

* Thu Feb 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Sun Feb 3 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt1
- 0.7

* Thu Jan 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.1-alt1
- First build for Sisyphus
