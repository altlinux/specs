%define upstreamname lxsession-edit
Name: lxde-%upstreamname
Version: 0.2
Release: alt2

Summary: LXDE Desktop Session Settings
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net
Packager: Radik Usupov <radik@altlinux.org>

Source: %upstreamname-%version.tar.gz

# Automatically added by buildreq on Fri Jan 09 2009
BuildRequires: intltool libgtk+2-devel python-modules-encodings time xml-utils

%description
lxsession-edit is a tool used to manage desktop session autostarts, especially for lxsession lite.

%prep
%setup -n %upstreamname-%version

%build
%autoreconf
%configure
touch -r po/Makefile po/stamp-it
%make_build

%install
%makeinstall_std
%find_lang %upstreamname

%files -f %upstreamname.lang
%doc ChangeLog INSTALL README
%_bindir/*
%_desktopdir/*.desktop
%_datadir/%upstreamname

%changelog
* Thu Jun 14 2012 Radik Usupov <radik@altlinux.org> 0.2-alt2
- new upstream snapshot

* Tue Aug 30 2011 Radik Usupov <radik@altlinux.org> 0.2-alt1
- new version

* Mon Jun 14 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.1-alt7
- russian title improved

* Sun Jun 13 2010 Radik Usupov <radik@altlinux.org> 0.1.1-alt6
- Added name[ru] in desktop-file

* Sun Jun 06 2010 Radik Usupov <radik@altlinux.org> 0.1.1-alt5
- optimized buildrequires

* Sun Jun 06 2010 Radik Usupov <radik@altlinux.org> 0.1.1-alt4
- updated from upstreame
- added localization
- added packager
- added autoreconf -fisv parameters
- added new builrequires

* Fri Jul 17 2009 Nick S. Grechukh <gns@altlinux.org> 0.1.1-alt3
- build fixed (infinite loop in po/)

* Thu Jul 16 2009 Nick S. Grechukh <gns@altlinux.org> 0.1.1-alt2
- packager fixed

* Thu Jul 16 2009 Nick S. Grechukh <gns@altlinux.org> 0.1.1-alt1
- new version

* Fri Jan 09 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
