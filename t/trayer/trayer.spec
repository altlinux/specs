Name: trayer
Version: 1.0.5
Release: alt2
License: BSD

Group: Graphical desktop/Other

Summary: lightweight GTK2-based systray for UNIX desktop

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Sun Aug 15 2010
BuildRequires: libXext-devel libXmu-devel libgtk+2-devel

%description
trayer is a small program designed to provide systray functionality
present in GNOME/KDE desktop environments for window managers which
do not support that function. System tray is a place, where various
applications put their icons, so they are always visible presenting
status of applications and allowing user to control programs.

trayer code was extracted from fbpanel application, you can find more
about it on its homepage: http://fbpanel.sourceforge.net/

%prep
%setup
%build
%make_build -C systray
%make_build
%install
%make_install PREFIX=%buildroot/usr install
%files
%_bindir/trayer
%_man1dir/*.1.*
%doc COPYING README

%changelog
* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.5-alt2
- fix build

* Sun Aug 15 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.5-alt1
- first build for Sisyphus

