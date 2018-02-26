#define status beta
Name: rosegarden
Version: 12.04
Release: alt1

Summary: MIDI and audio seqencer and musical notation editor
License: GPL
Group: Sound

Url: http://www.rosegardenmusic.com
Source: %name-%version.tar.bz2
Packager: Alex Karpov <karpov@altlinux.ru>

# Automatically added by buildreq on Thu Mar 04 2010
BuildRequires: dssi-devel gcc-c++ imake jackit-devel ladspa_sdk libSM-devel libX11-devel libalsa-devel libfftw3-devel liblirc-devel liblo-devel liblrdf-devel libqt4-devel libsamplerate-devel libsndfile-devel makedepend xorg-cf-files

BuildRequires: perl-XML-Twig desktop-file-utils shared-mime-info

Requires: libsndfile-utils

Provides: rosegarden = %version
Obsoletes: rosegarden-alsa rosegarden-arts rosegarden-common librosegarden-alsa librosegarden-arts

%description
Rosegarden is a professional audio and MIDI seqencer, score editor, and 
general-purpose music composition and editing environement.

Rosegarden is an easy-to-learn, attractive application that runs on 
Linux, ideal for composers, musicians, music students, and small studio
or home recording environments.

%prep
%setup -n %name-%version

%build
%configure --with-qtdir=%_libdir/qt4
%make

%install
%make DESTDIR="%buildroot" install
%find_lang --with-kde %name

%files -f %name.lang
%doc README AUTHORS COPYING
%_bindir/*
%_datadir/applications/*
%_datadir/icons/hicolor/16x16/mimetypes/*
%_datadir/icons/hicolor/32x32/apps/*
%_datadir/icons/hicolor/32x32/mimetypes/*
%_datadir/icons/hicolor/64x64/apps/*
%_datadir/icons/hicolor/64x64/mimetypes/*
%_datadir/icons/hicolor/128x128/apps/*
%_datadir/mime/packages/*

%changelog
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

