Name: herrie
Version: 2.2
Release: alt3

Summary: A command line music player

License: BSD
Group: Sound
Url: http://herrie.info/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://herrie.info/distfiles/%name-%version.tar.bz2

# Automatically added by buildreq on Sat Feb 28 2009
BuildRequires: glib2-devel libalsa-devel libcurl-devel libid3tag-devel libmad-devel libmodplug-devel libncursesw-devel libsndfile-devel libspiff-devel libstdc++-devel libvorbis-devel

%description
Herrie is a command line music player. It has a split-screen file
manager and playlist interface and supports a number of file formats
(MP3, Ogg Vorbis, wave, FLAC, etc).

%prep
%setup -q

%build
# unusual configure
./configure no_xspf
%make_build

%install
%makeinstall_std

:> %buildroot%_sysconfdir/%name.conf
%find_lang %name

%files -f %name.lang
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/*
%doc COPYING ChangeLog README *.sample
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sat Mar 07 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt3
- build without XSPF (wait for new herrie with libxspf support)

* Sat Feb 28 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt2
- update buildreqs

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- new version 2.2 (with rpmrb script)

* Mon Sep 22 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- new version 2.1 (with rpmrb script)

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script)
- update buildreq

* Fri Dec 21 2007 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version 1.9.1 (with rpmrb script)

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- new version 1.8.4 (with rpmrb script)

* Tue Sep 18 2007 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

