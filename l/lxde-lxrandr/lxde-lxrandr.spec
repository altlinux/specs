%set_automake_version 1.11

%define upstreamname lxrandr
%define gtkver 2
Name: lxde-%upstreamname
Version: 0.3.1
Release: alt1

Summary: Easy-to-use XRandR GUI frontend for LXDE project
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net
#Url: git://git.lxde.org/lxde/lxrandr.git
Packager: Radik Usupov <radik@altlinux.org>

Source: %upstreamname-%version.tar

BuildRequires: docbook-dtds docbook-style-xsl intltool libgtk+%gtkver-devel xsltproc

%description
%summary

%prep
%setup -n %upstreamname-%version

%build
%autoreconf
%if %gtkver==3
    %configure --enable-man --enable-gtk3
%else
    %configure --enable-man
%endif

%make_build

%install
%makeinstall_std
%find_lang %upstreamname

%files -f %upstreamname.lang
%doc ChangeLog NEWS README
%_bindir/*
%_desktopdir/*.desktop
%_man1dir/*

%changelog
* Tue May 17 2016 Anton Midyukov <antohami@altlinux.org> 0.3.1-alt1
- New version.

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.1
- Fixed build

* Mon Jun 11 2012 Radik Usupov <radik@altlinux.org> 0.1.2-alt2
- New upstream snapshot

* Mon Aug 29 2011 Radik Usupov <radik@altlinux.org> 0.1.2-alt1
- New version (0.1.2)
- Moved files to folder

* Tue Jun 01 2010 Radik Usupov <radik@altlinux.org> 0.1.1-alt3
- added Packager
- packaging scheme changed to follow upstream git
- added --enable-man fot %%configure parameters
- added autoreconf -fisv parameters
- buildrequires are corrected

* Sat Dec 12 2009 Mykola Grechukh <gns@altlinux.ru> 0.1.1-alt2
- new version

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for lxde-lxrandr

* Fri Jul 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
