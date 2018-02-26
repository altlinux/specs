Name: antico
Version: 0.2
Release: alt6.gcbed547

Summary: Antico is a Qt4/X11 Desktop/Window Manager
Group: Graphical desktop/Other
License: GPL
URL: http://www.antico.netsons.org/

Packager: Boris Savelev <boris@altlinux.org>

Source0: %name-%version.tar

# Automatically added by buildreq on Fri May 01 2009
BuildRequires: gcc-c++ libX11-devel libqt4-devel xorg-xextproto-devel

%description
The goal is to create a Desktop/Window manager simple and fast. All parameters must be configured from few files,
avoiding unnecessary complications, following the K.I.S.S. philosophy.
The whole project is based only on Qt4 libraries, without any other external dependencies (e.g. kdelibs ...).

%prep
%setup

%build
qmake-qt4
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot
mkdir -p %buildroot%_sysconfdir/X11/wmsession.d
install -m644 %name-alt.wm %buildroot%_sysconfdir/X11/wmsession.d/50%name

%files
%doc README CHANGELOG
%_sysconfdir/X11/wmsession.d/50%name
%_bindir/%name
%_datadir/%name

%changelog
* Sat Jun 06 2009 Boris Savelev <boris@altlinux.org> 0.2-alt6.gcbed547
- update from upstream

* Tue May 19 2009 Boris Savelev <boris@altlinux.org> 0.2-alt5.g5671eb2
- update from upstream

* Sat May 16 2009 Boris Savelev <boris@altlinux.org> 0.2-alt4.g94854be
- fix alt+tab bug (update from upstream)

* Mon May 11 2009 Boris Savelev <boris@altlinux.org> 0.2-alt3.gddf647c
- fix #20004

* Sun May 03 2009 Boris Savelev <boris@altlinux.org> 0.2-alt2.gd2d3ab2
- update from upstream

* Fri May 01 2009 Boris Savelev <boris@altlinux.org> 0.2-alt1
- intial build for Sisyphus
