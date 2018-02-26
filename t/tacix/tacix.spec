Summary: TaciX
Name: tacix
Version: 0.1.1
Release: alt2.gf1da751.1
License: GPL
Group: Networking/Remote access
Packager: Boris Savelev <boris@altlinux.org>
Url: https://code.launchpad.net/~freenx-team/freenx-server/tacix
Source: %name-%version.tar

# Automatically added by buildreq on Mon Apr 13 2009
BuildRequires: python-devel rpm-build-intro

%description
This package contains the TaciX server.

%package manager
Summary: TaciX manager
Group: Networking/Remote access
Requires: %name = %version-%release

%description manager
This package contains the TaciX session manager.

%package client
Summary: TaciX client
Group: Networking/Remote access
Requires: %name = %version-%release

%description client
This package contains the FreeNX Client.

%package freenx
Summary: TaciX FreeNX compatibility layer
Group: Networking/Remote access
Conflicts: freenx-server
Requires: %name-manager = %version-%release

%description freenx
This package contains the FreeNX compatibility layer.

%package applet-gtk
Summary: TaciX applet
Group: Networking/Remote access

%description applet-gtk
This package contains the GNOME applet.

%package -n python-module-%name
Summary: Python module for %name
Group: Development/Python

%description -n python-module-%name
Library to create remote desktop clients and remote desktop session managers.

%prep
%setup

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir
mkdir -p %buildroot%_initdir
install -m755 %name-alt-init %buildroot%_initdir/%name
mkdir -p %buildroot%_var/lib/nxserver/home/{.ssh,.nx}

%pre
%groupadd nx 2> /dev/null ||:
%useradd -g nx -G utmp -d /var/lib/nxserver/home/ -s %_libdir/%name/tacix-freenx-server \
        -c "Tacix Freenx User" nx 2> /dev/null ||:

%files
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/%name.conf
%dir %_libexecdir/%name
%dir %_datadir/%name

%files manager
%_initdir/%name
%config %_sysconfdir/dbus-1/system.d/*.conf
%config %_sysconfdir/%name/Xsession
%_sysconfdir/%name/cups.conf.template
%_bindir/tacix-manager
%_libexecdir/%name/tacix-session
%_datadir/dbus-1/system-services/%name.service
%_man1dir/tacix-manager*


%files client
%_bindir/tacix-client
%_libexecdir/%name/tacix-dialog
%_pixmapsdir/%name-*.png
%_man1dir/tacix-client*

%files freenx
%dir %_sysconfdir/%name/freenx-keys
%attr(700,nx,root) %config %_sysconfdir/%name/freenx-keys/authorized_keys2
%attr(700,nx,root) %config %_sysconfdir/%name/freenx-keys/client.id_dsa.key
%_libexecdir/%name/tacix-freenx-node
%_libexecdir/%name/tacix-freenx-server
%attr(700,nx,root) %_var/lib/nxserver/home
%attr(700,nx,root) %_var/lib/nxserver/home/.ssh
%attr(700,nx,root) %_var/lib/nxserver/home/.nx

%files applet-gtk
%_sysconfdir/xdg/autostart/%name-*.desktop
%_libexecdir/%name/tacix-applet-gtk
%_datadir/%name/*.ui

%files -n python-module-%name
%python_sitelibdir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.gf1da751.1
- Rebuild with Python-2.7

* Wed Dec 29 2010 Boris Savelev <boris@altlinux.org> 0.1.1-alt2.gf1da751
- fix build (update buildreq)

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.gf1da751.1
- Rebuilt with python 2.6

* Fri Nov 20 2009 Boris Savelev <boris@altlinux.org> 0.1.1-alt1.gf1da751
- new version

* Sat Jun 06 2009 Boris Savelev <boris@altlinux.org> 0.1-alt4.gaa09db5
- update from upstream

* Fri May 22 2009 Boris Savelev <boris@altlinux.org> 0.1-alt3.ge36afdc
- add forgotten python submodule

* Fri May 15 2009 Boris Savelev <boris@altlinux.org> 0.1-alt2.g7f299eb
- fix init-script
- update from upstream

* Wed May 13 2009 Boris Savelev <boris@altlinux.org> 0.1-alt1.gd8ba068
- update from upstream

* Mon Apr 13 2009 Boris Savelev <boris@altlinux.org> 0.0.1-alt1
- initial build

