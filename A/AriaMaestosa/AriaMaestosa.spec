%define srcname AriaSrc

Name: AriaMaestosa
Version: 1.4.1
Release: alt1

Summary: Aria Maestosa is an opensource (GPL) midi tracker/editor
License: GPLv2 with exceptions (look at license.txt)
Group: Sound
Url: http://ariamaestosa.sourceforge.net

Packager: Alex Karpov <karpov@altlinux.org>

Source: %srcname-%version.tar

# Automatically added by buildreq on Thu Nov 18 2010
BuildRequires: cvs flex gcc-c++ ghostscript-utils glib2-devel libGLU-devel libalsa-devel libjack-devel libwxGTK-devel python-modules-email rcs scons swig texlive-latex-base

%description
Aria Maestosa is an open-source (GPL) midi tracker/editor. It lets you 
compose, edit and play midi files with a few clicks in a user-friendly 
interface offering keyboard, guitar, drum and controller views.

%prep
%setup -n %srcname-%version

%build
python scons/scons.py prefix=/usr destdir=%buildroot

%install
python scons/scons.py install prefix=%buildroot/usr
%find_lang aria_maestosa

%files -f aria_maestosa.lang
%doc Changelog.txt TODO.txt license.txt
%_bindir/Aria
%_datadir/Aria

%changelog
* Mon May 21 2012 Alex Karpov <karpov@altlinux.ru> 1.4.1-alt1
- new version

* Wed Feb 08 2012 Alex Karpov <karpov@altlinux.ru> 1.3b4-alt1.2
- build with internal scons (new scons issue workaround)

* Thu Dec 15 2011 Alex Karpov <karpov@altlinux.ru> 1.3b4-alt1.1
- illegal rpath entries removed

* Wed Nov 30 2011 Alex Karpov <karpov@altlinux.ru> 1.3b4-alt1
- new beta

* Thu Aug 25 2011 Alex Karpov <karpov@altlinux.ru> 1.3b2-alt1
- new beta

* Tue Mar 08 2011 Alex Karpov <karpov@altlinux.ru> 1.2.4.1-alt1
- new version

* Sat Dec 04 2010 Alex Karpov <karpov@altlinux.ru> 1.2.4-alt1
- new version

* Thu Nov 18 2010 Alex Karpov <karpov@altlinux.ru> 1.2.3-alt1.1
- updated build requirements (fix build)

* Sat Sep 25 2010 Alex Karpov <karpov@altlinux.ru> 1.2.3-alt1
- new version

* Mon Jul 19 2010 Alex Karpov <karpov@altlinux.ru> 1.2.2-alt1
- new version

* Mon Jun 14 2010 Alex Karpov <karpov@altlinux.ru> 1.2.1-alt1
- initial build for Sisyphus

