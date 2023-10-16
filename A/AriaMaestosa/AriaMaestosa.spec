%define srcname AriaSrc

Name: AriaMaestosa
Version: 1.4.13
Release: alt2

Summary: Aria Maestosa is an opensource (GPL) midi tracker/editor
License: GPLv2 with exceptions (look at license.txt)
Group: Sound
Url: http://ariamaestosa.sourceforge.net

Source: %srcname-%version.tar
# Upstream patches
Patch1: 0001-Use-a-sensible-default-folder-for-opening-saving-fil.patch
Patch2: 0001-Update-to-wxWidgets-3.1.2.patch
Patch3: 0001-Make-the-scons-build-compatible-with-Python-3.patch
# Mageia patches
Patch50: ariamaestosa-wxgtk.patch
Patch51: ariamaestosa-scons.patch
Patch52: ariamaestosa-skip-upstream-version-check.patch

# Automatically added by buildreq on Thu Nov 18 2010
BuildRequires: cvs flex gcc-c++ ghostscript-utils glib2-devel libGLU-devel libalsa-devel libjack-devel libwxGTK3.2-devel python-modules-email rcs scons swig texlive-latex-base
BuildRequires: chrpath

%description
Aria Maestosa is an open-source (GPL) midi tracker/editor. It lets you 
compose, edit and play midi files with a few clicks in a user-friendly 
interface offering keyboard, guitar, drum and controller views.

%prep
%setup -n %srcname-%version
%autopatch -p1

%build
scons config=debug prefix=%prefix destdir=%buildroot

%install
scons install config=debug prefix=%buildroot%prefix

chrpath -d %buildroot%_bindir/Aria

%find_lang aria_maestosa

%files -f aria_maestosa.lang
%doc Changelog.txt TODO.txt license.txt
%_bindir/Aria
%_datadir/Aria

%changelog
* Mon Oct 16 2023 Anton Midyukov <antohami@altlinux.org> 1.4.13-alt2
- NMU: 
  + rebuild with wxGTK3.2
  + add upstream and Mageya patches
  + clean Packager

* Wed Oct 06 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.13-alt1
- Build new version.

* Fri Sep 18 2020 Igor Vlasenko <viy@altlinux.ru> 1.4.6-alt1.qa1
- NMU: do not use /usr/bin/python

* Fri Dec 28 2012 Alex Karpov <karpov@altlinux.ru> 1.4.6-alt1
- new version

* Tue Jul 03 2012 Alex Karpov <karpov@altlinux.ru> 1.4.2-alt1
- new version

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

