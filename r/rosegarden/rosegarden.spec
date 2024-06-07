Name: rosegarden
Version: 24.06
Release: alt1

Summary: MIDI sequencer and musical notation editor
License: GPLv2
Group: Sound
Url: http://www.rosegardenmusic.com

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++ ladspa_sdk
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6Linguist)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(dssi)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lrdf)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)

%description
Rosegarden is a music composition and editing environment based around
a MIDI sequencer that features a rich understanding of music notation
and includes basic support for digital audio.
Rosegarden is an easy-to-learn, attractive application that runs on Linux,
ideal for composers, musicians, music students, and small studio or home
recording environments.

%prep
%setup
# a must for every project btw
sed -i "s/UNSTABLE/STABLE/" CMakeLists.txt

%build
%cmake -DUSE_QT6=ON
%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS CONTRIBUTING README.md
%_bindir/rosegarden
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png
%_datadir/metainfo/rosegarden.*
%_datadir/mime/packages/rosegarden.*

%changelog
* Fri Jun 07 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 24.06-alt1
- 24.06

* Thu Dec 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 23.12-alt1
- 23.12 released

* Mon Oct 09 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 23.06-alt1
- 23.06 released

* Sun Jul 25 2021 Vitaly Lipatov <lav@altlinux.ru> 21.06-alt1
- new version 21.06 (ALT bug 40573)

* Mon Sep 07 2020 Vitaly Lipatov <lav@altlinux.ru> 20.06-alt1
- new version 20.06

* Sun Mar 08 2020 Vitaly Lipatov <lav@altlinux.ru> 19.12-alt1
- NMU: new version 19.12 (ALT bug 38088)

* Sat Oct 05 2019 Michael Shigorin <mike@altlinux.org> 17.12-alt2
- E2K: explicit -std=c++11; strip UTF-8 BOM for lcc < 1.24

* Fri Feb 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.12-alt1
- Updated to upstream version 17.12.

* Mon Jul 31 2017 Ildar Mulyukov <ildar@altlinux.ru> 17.04-alt1
- new version 17.04

* Thu Jun 20 2013 Andrey Cherepanov <cas@altlinux.org> 13.02-alt1.1
- Rebuild with new version liblo

* Mon Feb 25 2013 Alex Karpov <karpov@altlinux.ru> 13.02-alt1
- new version

* Wed Jan 09 2013 Alex Karpov <karpov@altlinux.ru> 12.12.25-alt1
- new version

* Thu May 17 2012 Alex Karpov <karpov@altlinux.ru> 12.04-alt1
- new version

* Tue Dec 13 2011 Alex Karpov <karpov@altlinux.ru> 11.11.42-alt1
- new version

* Thu Nov 10 2011 Alex Karpov <karpov@altlinux.ru> 11.11.1-alt1
- new version

* Thu Aug 25 2011 Alex Karpov <karpov@altlinux.ru> 11.06-alt1
- new version

* Mon Feb 07 2011 Alex Karpov <karpov@altlinux.ru> 11.02-alt1
- new version

* Fri Nov 05 2010 Alex Karpov <karpov@altlinux.ru> 10.10-alt1
- new version

* Wed May 05 2010 Alex Karpov <karpov@altlinux.ru> 10.04.2-alt1
- quick bugfix release

* Mon Apr 26 2010 Alex Karpov <karpov@altlinux.ru> 10.04.1-alt1
- new version

* Wed Mar 10 2010 Alex Karpov <karpov@altlinux.ru> 10.02.1-alt1.1
- fixed configure parameters and filelist

* Thu Mar 04 2010 Alex Karpov <karpov@altlinux.ru> 10.02.1-alt1
- new version
    + minor spec cleanup
    + removed obsoleted patches

* Wed Feb 04 2009 Alex Karpov <karpov@altlinux.ru> 1.7.3-alt1
- 1.7.3
    + removed obsoleted stuff

* Wed Sep 24 2008 Alex Karpov <karpov@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Mon Aug 18 2008 Alex Karpov <karpov@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Sun May 11 2008 Alex Karpov <karpov@altlinux.ru> 1.7.0-alt1
- 1.7.0 release

* Thu Mar 27 2008 Alex Karpov <karpov@altlinux.ru> 1.6.1-alt1.1
- added desktopdb and mimedb macros with new build requirements

* Fri Dec 21 2007 Alex Karpov <karpov@altlinux.ru> 1.6.1-alt1
- 1.6.1 bugfix release

* Fri Dec 07 2007 Alex Karpov <karpov@altlinux.ru> 1.6.0-alt1
- 1.6.0 release

* Fri Nov 30 2007 Alex Karpov <karpov@altlinux.ru> 1.6.0-alt0.pre2
- 1.6.0 prerelease 2

* Fri Oct 19 2007 Alex Karpov <karpov@altlinux.ru> 1.5.1-alt1.1
- rebuild with filesystem-2.3.3-alt1

* Tue Apr 10 2007 Alex Karpov <karpov@altlinux.ru> 1.5.1-alt1
- 1.5.1 upstream bugfix release

* Sun Feb 11 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt4
- updated patch

* Fri Feb 09 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt3
- added libsndfile-utils to requirements

* Wed Feb 07 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt2
- rebuild

* Tue Feb 06 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt1
- 1.5.0 release

* Wed Jan 10 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt0.2svn
- rebuild

* Tue Jan 09 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt0.1svn
- added patch for working --as-needed flag

* Sun Jan 07 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt0.svn
- new version from SVN


* Wed Oct 04 2006 Alex Karpov <karpov@altlinux.ru> 1.4.0-alt0.1
- new version

* Mon Sep 25 2006 Michael Shigorin <mike@altlinux.org> 1.4.0-alt0
- add_changelog
- test build in hasher on behalf of Alex Karpov <karpov@>
  + spec based on old rosegarden-1.0-alt1 spec by Yuri N. Sedunov <aris@>
    and klear-0.5.4-alt2 spec by Igor Zubkov <icesik@>

