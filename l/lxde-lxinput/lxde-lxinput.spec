%define upstreamname lxinput
Name: lxde-%upstreamname
Version: 0.3.2
Release: alt1
Summary: Keyboard and mouse settings dialog for LXDE

Group: System/Configuration/Hardware
License: GPLv2+
Url: http://lxde.sourceforge.net/
Packager: LXDE Development Team <lxde at packages.altlinux.org>

Source: http://downloads.sourceforge.net/sourceforge/lxde/%upstreamname-%version.tar.gz

BuildRequires: docbook-dtds docbook-style-xsl intltool libgtk+2-devel xsltproc
Requires: lxde-lxsession

%description
LXInput is a keyboard and mouse configuration utility for LXDE, the
Lightweight X11 Desktop Environment.

%prep
%setup -n %upstreamname-%version

%build
autoreconf -fisv
%configure --enable-man
%make_build

%install
%makeinstall_std INSTALL='install -p'
cp data/%upstreamname.desktop %buildroot%_desktopdir/%upstreamname.desktop
%find_lang %upstreamname

%files -f %upstreamname.lang
#FIXME: add ChangeLog and NEWS if there is content
%doc AUTHORS COPYING README
%_bindir/%upstreamname
%_datadir/%upstreamname/
%_desktopdir/%upstreamname.desktop
%_man1dir/%upstreamname.1.gz

%changelog
* Wed May 30 2012 Radik Usupov <radik@altlinux.org> 0.3.2-alt1
- new version (0.3.2)

* Fri Aug 26 2011 Radik Usupov <radik@altlinux.org> 0.3.1-alt1
- new version (0.3.1)

* Sun Aug 08 2010 Radik Usupov <radik@altlinux.org> 0.3.0-alt1
- new version
- changed packager

* Sun May 30 2010 Radik Usupov <radik@altlinux.org> 0.1.1-alt4
- buildrequires are corrected
- added autoreconf -fisv parameters
- added --enable-man fot %%configure parameters
- Makefile.am fixed: lxinput.desktop.in -> data/lxinput.desktop.in (thanks snejok@)

* Thu Feb 25 2010 Radik Usupov <radik@altlinux.org> 0.1.1-alt3
- Copy desktop file by 'cp'

* Tue Jan 26 2010 Radik Usupov <radik@altlinux.org> 0.1.1-alt2
- Update spec-files

* Mon Dec 28 2009 Radik Usupov <Radik@altlinux.org> 0.1.1-alt1
- First version of RPM package for Sisyphus
