%define upstreamname obconf
%define gtkver 2
Name: lxde-lxappearance-%upstreamname
Version: 0.2.3
Release: alt1

Summary: %name is tool for configuring openbox within LXDE.
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net
#Url: git://git.lxde.org/lxde/lxappearance-obconf.git

Source: %upstreamname-%version.tar

BuildPreReq: libgtk+%gtkver-devel intltool libopenbox-devel lxde-lxappearance-devel

%description
LXAppearance is part of LXDE project.

This plugin allows to configure openbox.

%prep
%setup -n %upstreamname-%version

%build
%autoreconf
%if %gtkver==3
    %configure --enable-gtk3
%else
    %configure
%endif
#touch -r po/Makefile po/stamp-it
%make_build

%install
%makeinstall_std
%find_lang lxappearance-%upstreamname

%files -f lxappearance-%upstreamname.lang
%doc CHANGELOG README
%_libdir/lxappearance/plugins/%upstreamname.so
%exclude %_libdir/lxappearance/plugins/%upstreamname.a
%exclude %_libdir/lxappearance/plugins/%upstreamname.la
%_datadir/lxappearance/%upstreamname

%changelog
* Tue May 17 2016 2016 Anton Midyukov <antohami@altlinux.org> 0.2.3-alt1
- New version.

* Mon Sep 14 2015 Aleksey Avdeev <solo@altlinux.org> 0.2.2-alt1
- new version
- rebuilt with new openbox

* Tue May 08 2012 Radik Usupov <radik@altlinux.org> 0.2.0-alt1
- new upsreame snapshot

* Mon Feb 13 2012 Radik Usupov <radik@altlinux.org> 0.1.1-alt2
- new upsreame snapshot

* Fri Aug 05 2011 Mykola Grechukh <gns@altlinux.ru> 0.1.1-alt1
- new version
- rebuilt with new openbox

* Tue Aug 10 2010 Mykola Grechukh <gns@altlinux.ru> 0.0.1-alt1
- initial build for Sisyphus
