Name: motion
Version: 4.3.2
Release: alt2

Summary: %name - Detect motion using a video4linux device
License: GPL
Group: Video

Url: https://motion-project.github.io
Source0: %name-%version.tar
Patch3: motion-4.1.1-alt-mysql8-transition.patch

BuildRequires: libavformat-devel libjpeg-devel postgresql-devel zlib-devel
BuildRequires: libmjpegtools-devel libsqlite3-devel
BuildRequires: libpostproc-devel libswscale-devel libavdevice-devel
BuildRequires: libavfilter-devel libv4l-devel
BuildRequires: libavformat-devel libjpeg-devel libmysqlclient-devel postgresql-devel zlib-devel libwebp-devel
BuildRequires: libmicrohttpd-devel

%description
With motion you can use a video4linux device as a motion detector.
It will make snapshots if motion is detected.

%prep
%setup
%patch3 -p0

sed -i 's|<postgresql[/]libpq-fe.h>|<pgsql/libpq-fe.h>|' src/%name.h
sed -i 's|\(if [\\(]cnt->conf\.mysql_db && sqltype[\)]\)|//\1|' src/event.c
sed -i 's|\(put_mysql[\(]&cnt->conf, cnt->database, filename, tm, sqltype[\)]\)|//\1|' src/event.c
sed -i 's|\(^.*c->quality\).*|//\1|' src/ffmpeg.c

%build
%ifarch %e2k
# asm under that ifdef
%add_optflags -U__MMX__
%endif
%autoreconf
%configure \
	--with-webp \
	--without-optimizecpu

%make_build

%install
%makeinstall_std

mv %buildroot%_defaultdocdir/%name %buildroot%_defaultdocdir/%name-%version
rename -- -dist.conf .conf %buildroot%_sysconfdir/%name/*.conf
install -pDm0644 data/%name.service %buildroot/%_unitdir/%name.service

%find_lang %name

%files -f %name.lang
%doc README.md
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/camera?.conf
%_unitdir/*.service
%_bindir/%name
%_man1dir/*

%changelog
* Tue Sep 28 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.3.2-alt2
- Add noreplace to global config files (closes: 41020)

* Sat Apr 24 2021 Evgeny Sinelnikov <sin@altlinux.org> 4.3.2-alt1
- update to latest release

* Tue Apr 21 2020 Michael Shigorin <mike@altlinux.org> 4.1.1-alt3
- E2K: fix ftbfs (x86 asm under MMX ifdef, SIMD might do better)
- minor spec cleanup

* Sun Jan 13 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.1.1-alt2
- fix FTBFS due to transition to libmysqlclient21

* Mon Oct 15 2018 Anton Farygin <rider@altlinux.ru> 4.1.1-alt1
- 4.1.1
- cleanup specfile
- added systemd unit
- enabled webp support

* Mon Jun 05 2017 Hihin Ruslan <ruslandh@altlinux.ru> 4.0.1-alt1.2
- Rebuild with new ffnpeg

* Thu Feb 23 2017 Hihin Ruslan <ruslandh@altlinux.ru> 4.0.1-alt1.1
- Version 4.0.1 (ALT #33157)

* Thu Feb 23 2017 Hihin Ruslan <ruslandh@altlinux.ru> 3.4.1-alt1.1
- Version 3.4.1

* Fri May 01 2015 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.12-alt3.1
- New version 

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.12-alt2.4
- Fixed build

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.12-alt2.3
- Rebuilt with libav 0.8

* Mon Aug 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.12-alt2.2
- Rebuilt with ffmpeg 0.7.1

* Sat Dec 11 2010 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.12-alt2.1
- correct buildreq
- fix #23880

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 3.2.12-alt1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Tue Jun 15 2010 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.12-alt1
- new version

* Tue Feb 17 2009 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.11-alt1.svn20090216.1
- new version released

* Thu Jan 31 2008 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.10-alt1.svn20080126.1
- add motion-3.2.10-docdir.patch

* Tue Dec 25 2007 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.9-alt2
- add motion-3.2.9-configure.patch

* Sat Dec 22 2007 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.9-alt1
- new version released

* Sat Oct 13 2007 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.8-alt2
- add motion-3.2.8-ffmpeg.patch

* Fri Aug 31 2007 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.8-alt1
- new version released

* Wed Mar 01 2006 Grigory Milev <week@altlinux.ru> 3.2.4-alt1
- new version released

* Thu Nov 24 2005 Kachalov Anton <mouse@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Tue Oct 11 2005 Grigory Milev <week@altlinux.ru> 3.1.19-alt2
- rebuild with new libpg4

* Mon Apr 25 2005 Grigory Milev <week@altlinux.ru> 3.1.19-alt1
- new version released
- return ffmpeg

* Thu Jan 13 2005 Grigory Milev <week@altlinux.ru> 3.1.17-alt2
- temporary off ffmpeg support

* Mon Nov  1 2004 Grigory Milev <week@altlinux.ru> 3.1.17-alt1
- new version released

* Thu Oct 21 2004 ALT QA Team Robot <qa-robot@altlinux.org> 3.1.16-alt1.1
- Rebuilt with libcurl.so.3.

* Thu Sep  9 2004 Grigory Milev <week@altlinux.ru> 3.1.16-alt1
- new version released

* Wed May 12 2004 Grigory Milev <week@altlinux.ru> 3.1.3-alt2
- fix build requires

* Wed Feb 25 2004 Grigory Milev <week@altlinux.ru> 3.1.3-alt1
- new version released

* Tue Nov  4 2003 Grigory Milev <week@altlinux.ru> 3.0.6-alt1
- build new version
- added MySQL support
- added ffmpeg support

* Wed Oct 23 2002 Grigory Milev <week@altlinux.ru> 3.0.4-alt1
- new version released

* Wed May 29 2002 Grigory Milev <week@altlinux.ru>  3.0.0-alt1
- Initial build for ALT Linux distribution.



