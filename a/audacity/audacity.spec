Name: audacity
Version: 2.0.0
Release: alt1

Summary: Cross-platform audio editor
Summary(ru_RU.CP1251): Кроссплатформенный звуковой редактор
License: GPL
Group: Sound
Url: http://audacity.sourceforge.net/

Packager: Alex Karpov <karpov@altlinux.ru>

# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/audacity co -r audacity-1_3_0-branch audacity
Source0: %name-fullsrc-%version.tar
Source2: %name-48x48.xpm
Source3: %name-32x32.xpm
Source4: %name-16x16.xpm
Source6: %name-%version-help-en.tar

Patch0: %name-installmo.patch

# Automatically added by buildreq on Fri Aug 14 2009
BuildRequires: gcc-c++ gcc-fortran glibc-devel-static jackit-devel libalsa-devel libavformat-devel libexpat-devel libflac++-devel libgtk+2-devel libid3tag-devel libmad-devel libsndfile-devel libsoundtouch-devel libtag-devel libtwolame-devel libvorbis-devel wxGTK-devel

BuildRequires: libportaudio2-devel
BuildRequires: desktop-file-utils shared-mime-info

%description
Audacity is a program that lets you manipulate digital audio waveforms.
It imports many sound file formats, including WAV, AIFF, AU, IRCAM,
MP3, and Ogg Vorbis. It supports all common editing operations such
as Cut, Copy, and Paste, plus it will mix tracks and let you apply
plug-in effects to any part of a sound.

%prep
%setup -q -n %name-src-%version
%patch0
%__grep -Irl "libmp3lame.so" . | xargs %__subst "s/libmp3lame.so/libmp3lame.so.0.0/"


%build
rm -f src/.depend
rm -f src/.gchdepend
cd lib-src/libmad
autoreconf -fisv
cd ../..
%configure --disable-dynamic-loading
#--enable-unicode=yes --with-portmixer=no
%make

%install
%makeinstall DESTDIR=%buildroot
%__install -pD -m644 %SOURCE2 %buildroot%_liconsdir/%name.xpm
%__install -pD -m644 %SOURCE3 %buildroot%_iconsdir/%name.xpm
%__install -pD -m644 %SOURCE4 %buildroot%_miconsdir/%name.xpm
mkdir %buildroot%_datadir/%name/help
tar -xf %SOURCE6 -C %buildroot%_datadir/%name/help/

%find_lang %name

%files -f %name.lang
%doc *.txt 
%exclude %_docdir/%name
%_bindir/*
%_mandir/man?/*
%_iconsdir/*.xpm
%_liconsdir/*
%_miconsdir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/mime/packages/%name.xml

%changelog
* Thu Mar 15 2012 Alex Karpov <karpov@altlinux.ru> 2.0.0-alt1
- new version. At last - not beta anymore!

* Tue Jan 31 2012 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1.3
- russian translation updated

* Sun Jan 22 2012 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1.2
- added new russian translation (bug #26841)

* Wed Jan 18 2012 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1.1
- export with libav* now works

* Tue Dec 13 2011 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1
- new version

* Wed Nov 09 2011 Alex Karpov <karpov@altlinux.ru> 1.3.13-alt2.1
- rebuild with new libav*

* Thu Aug 25 2011 Alex Karpov <karpov@altlinux.ru> 1.3.13-alt2
- fixed build (patch from Debian by Reinhard Tartler)

* Wed Apr 13 2011 Alex Karpov <karpov@altlinux.ru> 1.3.13-alt1
- new version

* Tue Nov 23 2010 Alex Karpov <karpov@altlinux.ru> 1.3.12-alt1.1
- disable portmixer for a while (build workaround)

* Fri Apr 02 2010 Alex Karpov <karpov@altlinux.ru> 1.3.12-alt1
- new version

* Tue Mar 23 2010 Alex Karpov <karpov@altlinux.ru> 1.3.11-alt1
- new version

* Thu Dec 10 2009 Alex Karpov <karpov@altlinux.ru> 1.3.10-alt1
- new version

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.9-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for audacity
  * postclean-05-filetriggers for spec file

* Mon Nov 02 2009 Alex Karpov <karpov@altlinux.ru> 1.3.9-alt1.1
- GSocket declaration conflict fixed

* Wed Sep 02 2009 Alex Karpov <karpov@altlinux.ru> 1.3.9-alt1
- new version
    + build from fullsrc tarball

* Mon Aug 24 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt2.1
- minor spec cleanup

* Mon Aug 24 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt2
- added actual help files

* Fri Aug 14 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt1.1
- updated build requirements
    + spec cleanup

* Thu Aug 13 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt1
- new version

* Tue Aug 11 2009 Alex Karpov <karpov@altlinux.ru> 1.3.7-alt1.1
- rebuild with new libs

* Fri Feb 27 2009 Alex Karpov <karpov@altlinux.ru> 1.3.7-alt1
- now it's stable enough for alt1 release

* Thu Jan 29 2009 Alex Karpov <karpov@altlinux.ru> 1.3.7-alt0.1
- 1.3.7

* Wed Jan 28 2009 Alex Karpov <karpov@altlinux.ru> 1.3.6-alt0.1
- 1.3.6
    + removed obsoleted %post and %postun stuff

* Thu Sep 25 2008 Alex Karpov <karpov@altlinux.ru> 1.3.5-alt0.1
- 1.3.5
    + updated build requirements

* Mon Apr 07 2008 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.9.2
- added update_menus

* Thu Mar 27 2008 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.9.1
- added desktopdb macros with new build requirements

* Mon Mar 24 2008 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.9
- added mimedb macros

* Sat Dec 15 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.M40.7
- build for branch 4.0 with libtwolame

* Fri Dec 14 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.6.1
- build for branch 4.0 (#13689 fix)

* Wed Nov 14 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.6.1
- Vamp disabled for x86_64 build

* Wed Nov 14 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.6
- 1.3.4 release

* Tue Oct 30 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.1
- new 1.3.4 unofficial beta
  + required wxGTK2u-2.6.4 (#13068 and probably #11880 fix)
  + removed desktop-file patch.

* Thu Sep 20 2007 Alex Karpov <karpov@altlinux.ru> 1.3.3-alt0.3
- audacity.desktop categories fixed (#12843)

* Tue Jun 05 2007 Alex Karpov <karpov@altlinux.ru> 1.3.3-alt0.2
- updated build requirements (now we can find a sound device)

* Wed May 30 2007 Alex Karpov <karpov@altlinux.ru> 1.3.3-alt0.1
- 1.3.3

* Tue Feb 20 2007 Alex Karpov <karpov@altlinux.ru> 1.3.2-alt0.4
- patch for flac-1.1.3 support by Led <led@> (bug #10868) 

* Thu Dec 14 2006 Alex Karpov <karpov@altlinux.ru> 1.3.2-alt0.3
- fixed bug 10420

* Sat Nov 11 2006 Alex Karpov <karpov@altlinux.ru> 1.3.2-alt0.2
- initial build of 1.3.x branch for Sisyphus

* Thu Dec 01 2005 Vladimir Lettiev <crux@altlinux.ru> 1.3.0-alt0.1
- 1.3.0 beta ( audacity-1_3_0-branch from cvs )

* Tue Feb 22 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.3-alt1.1.1
- Rebuilt with libflac-1.1.2-alt1

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.3-alt1.1
- Rebuilt with libstdc++.so.6.

* Sun Nov 21 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Thu Sep 02 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Fri Jun 25 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.1-alt2
- Updated patch from help file location.

* Wed May 12 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Apr 13 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt2
- Updated russian translation.
- Added russian help.
- Fixed build with SoundTouch for gcc 3.3.3.

* Wed Mar 10 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Feb 14 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.9
- 1.2.0-pre4

* Fri Nov 14 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.8
- 1.2.0-pre3
- Fixed build on SMP systems.

* Tue Oct 07 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.7
- 1.2.0-pre2

* Sun Sep 28 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.6
- 1.2.0-pre2 testing tarball.

* Sun Sep 14 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.3
- 1.2.0-pre1

* Wed Jun 25 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt3
- Fixed unmet: now requires wxGTK >= 2.4.1.

* Fri Jun 20 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt2
- Rebuilt with new wxGTK.

* Fri Mar 21 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Sun Mar 16 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt0.4
- Rebuilt with libid3tag package.

* Fri Mar 07 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt0.2
- Developers branch snapshot (CVS 20030306).
- Temprorary without libsamplerate.

* Wed Mar 05 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0.0-alt6
- Rebuild with wxGTK-2.4.0

* Fri Feb 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt5
- Rebuild with new id3lib (3.8.2)

* Fri Nov 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt4
- Rebuild with new id3lib (3.8.1)

* Wed Nov 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt3
- Rebuild, system id3lib used.

* Wed Jul 31 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt2.1
- rebuild with new vorbis

* Mon Jun 24 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0.0-alt2
- Fixed intersection with basesystem.

* Fri Jun 7 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Mon May 27 2002 Andrey Astafiev <andrei@altlinux.ru> 1.1-alt0.1.cvs
- cvs snapshot 20020527 of 1.1.x unstable branch especially for Daedalus.

* Wed Feb 13 2002 Andrey Astafiev <andrei@altlinux.ru> 0.99-alt0.1.pre1
- cvs snapshot 20020213 with several bugfixes.
- relocated help.

* Tue Feb 12 2002 Andrey Astafiev <andrei@altlinux.ru> 0.98-alt2
- rebuild with wxGTK 2.2.x branch.

* Fri Feb 01 2002 Andrey Astafiev <andrei@altlinux.ru> 0.98-alt1
- 0.98.

* Tue Jan 08 2002 Andrey Astafiev <andrei@altlinux.ru> 0.97-alt2
- Fixed group tag.

* Thu Oct 11 2001 Andrey Astafiev <andrei@altlinux.ru> 0.97-alt1
- First version of RPM package.
