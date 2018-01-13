%define rname mozplugger
%define name mozilla-plugin-%rname
%define version 2.1.6
%define release alt1

Name: %name
Version: %version
Release: %release

Summary: A generic mozilla plug-in
License: GPL
Group: Networking/WWW

Url: http://mozplugger.mozdev.org
Source: %rname-%version.tar
Patch: %rname-alt-install.patch
Packager: L.A. Kostis <lakostis@altlinux.org>

Requires: browser-plugins-npapi, m4
Obsoletes: %rname

BuildRequires: libX11-devel libXt-devel 

# Added by hand
BuildRequires(pre): browser-plugins-npapi-devel

Summary(ru_RU.UTF-8): Универсальный плагин к mozilla

%description
MozPlugger is a generic Mozilla plug-in that allows the use of standard Linux
programs as plug-ins for media types on the Internet.

%description -l ru_RU.UTF-8
MozPlugger - это универсальный плагин для браузеров семейства Mozilla,
позволяющий использовать стандартные программы Linux (и не только) как
плагины для различных мультимедиа файлов из сети Internet.

%prep
%setup -n %rname-%version
%patch -p2

%build
%configure
%make_build

%install
%makeinstall_std PLUGINDIRS=%browser_plugins_path

%files
%_sysconfdir/mozpluggerrc
%_bindir/%rname-*
%_man7dir/%rname.*
%browser_plugins_path/%rname.so
%doc README ChangeLog COPYING

%changelog
* Sun Jan 14 2018 Michael Shigorin <mike@altlinux.org> 2.1.6-alt1
- 2.1.6
- spec cleanup

* Thu Mar 28 2013 L.A. Kostis <lakostis@altlinux.ru> 2.1.3-alt1
- 2.1.3.

* Tue Sep 29 2009 Alexey Gladkov <legion@altlinux.ru> 1.13.0-alt1.1
- NMU: Rebuilt with browser-plugins-npapi.

* Sat Sep 26 2009 L.A. Kostis <lakostis@altlinux.ru> 1.13.0-alt1
- 1.13.0.

* Sun Apr 12 2009 L.A. Kostis <lakostis@altlinux.ru> 1.12.0-alt1
- 1.12.0.

* Tue Sep 23 2008 L.A. Kostis <lakostis@altlinux.ru> 1.11.0-alt1
- 1.11.0.

* Mon Jul 07 2008 L.A. Kostis <lakostis@altlinux.ru> 1.10.2-alt1
- 1.10.2.

* Sat Nov 18 2006 L.A. Kostis <lakostis@altlinux.ru> 1.7.3-alt1.2
- remove oo subst hack.

* Wed Oct 04 2006 L.A. Kostis <lakostis@altlinux.ru> 1.7.3-alt1.1
- fix #9754 (s/oofice/oofice2).
- cleanup buildrequies.

* Thu Oct 27 2005 LAKostis <lakostis at altlinux dot ru> 1.7.3-alt1
- new version.

* Sun Aug 07 2005 LAKostis <lakostis at altlinux dot ru> 1.7.2-alt1.1
- update rc from cvs fixing bugs with new gv and mpg123.

* Fri Apr 22 2005 LAKostis <lakostis at altlinux dot ru> 1.7.2-alt1
- new version.

* Wed Apr 20 2005 LAKostis <lakostis at altlinux dot ru> 1.7.1-alt1.1
- update Requires/BuildRequires.

* Sun Mar 06 2005 LAKostis <lakostis at altlinux dot ru> 1.7.1-alt1
- new version
- update to new plugin policy.
- add documentation section.

* Mon Nov 29 2004 LAKostis <lakostis at altlinux dot ru> 1.6.2-alt1
- new version

* Sun Aug 29 2004 LAKostis <lakostis at altlinux dot ru> 1.6.1-alt1
- new version
- update mozpluggerrc from cvs.

* Fri Aug 13 2004 LAKostis <lakostis at altlinux dot ru> 1.6.0-alt1
- new version

* Mon Apr 05 2004 LAKostis <lakostis at altlinux dot ru> 1.5.2-alt1
- new version

* Sat Feb 21 2004 LAKostis <lakostis at altlinux dot ru> 1.5.0-alt1
- new version
- add russian traslation of description

* Tue Oct 07 2003 LKS <lakostis at altlinux dot ru> 1.3.2-alt1.2
- fixed typo in changelog.

* Mon Sep 22 2003 LAKostis <lakostis at altlinux dot ru> 1.3.2-alt1.1
- fixed buildreq.

* Thu Sep 18 2003 LAKostis <lakostis@altlinux.ru> 1.3.2-alt1
- 1.3.2 release.
- spec cleanups.

* Thu Jun 12 2003 LAKostis <lakostis@altlinux.ru> 1.2.0-alt1
- rebuild for Sisyphus.
