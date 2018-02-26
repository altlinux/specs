%define upstreamname obconf
Name: lxde-lxappearance-%upstreamname
Version: 0.2.0
Release: alt1

Summary: %name is tool for configuring openbox within LXDE.
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net

Source: %upstreamname-%version.tar.gz

# Automatically added by buildreq on Tue Aug 10 2010 (-bb)
BuildRequires: intltool libopenbox-devel lxde-lxappearance-devel

%description
LXAppearance is part of LXDE project.

This plugin allows to configure openbox.

%prep
%setup -n %upstreamname-%version
sed -i '/no/ d' po/LINGUAS

%build
autoreconf -fisv
%configure
touch -r po/Makefile po/stamp-it
%make_build

%install
%makeinstall_std
%find_lang %upstreamname

%files -f %upstreamname.lang
%doc CHANGELOG README
%_libdir/lxappearance/plugins/%upstreamname.so
%_datadir/lxappearance/%upstreamname

%changelog
* Tue May 08 2012 Radik Usupov <radik@altlinux.org> 0.2.0-alt1
- new upsreame snapshot

* Mon Feb 13 2012 Radik Usupov <radik@altlinux.org> 0.1.1-alt2
- new upsreame snapshot

* Fri Aug 05 2011 Mykola Grechukh <gns@altlinux.ru> 0.1.1-alt1
- new version
- rebuilt with new openbox

* Tue Aug 10 2010 Mykola Grechukh <gns@altlinux.ru> 0.0.1-alt1
- initial build for Sisyphus
