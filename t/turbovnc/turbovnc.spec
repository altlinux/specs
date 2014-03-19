Name: turbovnc
Version: 1.2.1
Release: alt3

%define vnc_name turbovnc

Summary: Fast remote display system well suited to VirtualGL.
License: GPL
#Group: System/Libraries
Group: Networking/Remote access
Provides: tightvnc
Conflicts: tightvnc

Url: http://virtualgl.org
Packager: Dmitry Derjavin <dd@altlinux.org>

Source: %name-%version.tar
#Source1: turbovnc
#Source2: turbovnc.pamd

Patch1: TurboVNC-1.0.2-alt-conf-class-path.patch
Patch2: TurboVNC-1.2.1-alt-system-libturbojpeg.patch

BuildRequires: cmake libturbojpeg-devel libpam0-devel zlib-devel libXaw-devel libXext-devel libXcursor-devel

%description
TurboVNC is an optimized version of VNC (more specifically, of
TightVNC 1.3.x.) On the surface, TurboVNC behaves similarly to its
parent, but TurboVNC has been tuned to provide interactive performance
for full-screen video and 3D workloads.

TurboVNC, when used with VirtualGL, provides a highly performant and
robust solution for remotely displaying 3D applications over all types
of networks.

This package contains TurboVNC client application.

%package server
Summary: TurboVNC server
Group: Networking/Remote access
Provides: tightvnc-server
Conflicts: tightvnc-server

%description server
TurboVNC is an optimized version of VNC (more specifically, of
TightVNC 1.3.x.) On the surface, TurboVNC behaves similarly to its
parent, but TurboVNC has been tuned to provide interactive performance
for full-screen video and 3D workloads.

TurboVNC, when used with VirtualGL, provides a highly performant and
robust solution for remotely displaying 3D applications over all types
of networks.

This package contains TurboVNC server.

# %package server-data
# Summary: TurboVNC client, Java version
# Group: Networking/Remote access
# Requires: %name-server

# %description server-data
# TurboVNC is an optimized version of VNC (more specifically, of
# TightVNC 1.3.x.) On the surface, TurboVNC behaves similarly to its
# parent, but TurboVNC has been tuned to provide interactive performance
# for full-screen video and 3D workloads.

# TurboVNC, when used with VirtualGL, provides a highly performant and
# robust solution for remotely displaying 3D applications over all types
# of networks.

# This package contains TurboVNC Java client application for HTTP access
# to TurboVNC server.

%prep
%setup

%patch1 -p1
%patch2 -p1

%build

cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=%buildroot%_usr -DTVNC_BINDIR=%buildroot%_bindir -DTVNC_DOCDIR=%buildroot%_datadir/doc/%name-%version ./

make
make xserver

%install
make install
# Temporarily disabled java viewer:
# mkdir -p %buildroot%_usr/libexec/%name
# for file in VncViewer.jar index.vnc; do
#     mv %buildroot/usr/vnc/classes/$file %buildroot%_usr/libexec/%name
# done
#
# Docs don't need to be copied any more
# mkdir -p %buildroot%_datadir/doc/%name-%version
# mv doc/*.png doc/*.html doc/*.css LICENSE.txt ChangeLog.txt \
# %buildroot%_datadir/doc/%name-%version
#
# Java viewer docs to be added back:
# mkdir -p %buildroot%_datadir/doc/%name-server-data-%version
# mv %buildroot/usr/vnc/classes/README %buildroot%_datadir/doc/%name-server-data-%version
pushd %buildroot%_usr/man/man1
mv Xserver.1 %{name}-Xserver.1
popd
mkdir -p %buildroot%_man1dir
mv %buildroot%_usr/man/man1/* %buildroot%_man1dir
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir/sysconfig
pushd %buildroot%_usr/etc
mv *.conf %buildroot%_sysconfdir
mv init.d/tvncserver %buildroot%_initdir
mv sysconfig/tvncservers %buildroot%_sysconfdir/sysconfig
popd

%files
%_bindir/tvncconfig
%_bindir/vncconnect
%_bindir/vncviewer
%_man1dir/vncconnect.*
%_man1dir/vncviewer.*
%doc %_datadir/doc/%name-%version

%files server
%_bindir/Xvnc
%_bindir/vncserver
%_bindir/vncpasswd
%_initdir/tvncserver
%config(noreplace) %_sysconfdir/turbovncserver-auth.conf
%config(noreplace) %_sysconfdir/turbovncserver.conf
%config(noreplace) %_sysconfdir/sysconfig/tvncservers
###%config(noreplace) %_sysconfdir/pam.d/%vnc_name
%_man1dir/%name-Xserver.*
%_man1dir/Xvnc.*
%_man1dir/vncpasswd.*
%_man1dir/vncserver.*

# %files server-data
# %_usr/libexec/%name
# %doc %_datadir/doc/%name-server-data-%version

%post server
%post_service tvncserver

%preun server
%preun_service tvncserver

%changelog
* Wed Mar 19 2014 Dmitry Derjavin <dd@altlinux.org> 1.2.1-alt3
- post and preun were assigned to the wrong package (closes: 29893).

* Fri Mar 07 2014 Dmitry Derjavin <dd@altlinux.org> 1.2.1-alt2
- post and preun service scripts added.

* Thu Mar 06 2014 Dmitry Derjavin <dd@altlinux.org> 1.2.1-alt1
- Fresh up to 1.2.1;
- Java viewer temporarily disabled.

* Wed Feb 13 2013 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Fresh up to v1.1.

* Wed Mar 28 2012 Dmitry Derjavin <dd@altlinux.org> 1.0.90-alt1
- 1.0.90, examine ChangeLog.txt for important changes;
- PAM configuration removed.

* Fri Jan 27 2012 Dmitry Derjavin <dd@altlinux.org> 1.0.2-alt4
- ALT specific default settings added to config file.

* Mon Nov 21 2011 Dmitry Derjavin <dd@altlinux.org> 1.0.2-alt2
- vncpasswd moved to -server package;
- provides and conflicts added.

* Fri Nov 18 2011 Dmitry Derjavin <dd@altlinux.org> 1.0.2-alt1
- Initial ALT Linux build.

