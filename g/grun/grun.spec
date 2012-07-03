Name: grun
Version: 0.9.3
Release: alt1

Summary: GTK based Run dialog

License: GPL
Group: Graphical desktop/Other
Url: http://code.google.com/p/grun/

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar
BuildRequires: libgtk+2-devel

%description
gRun is a GTK based Run dialog that closely resembles the Windows Run dialog, just like xexec. 
It has a intelligent history mechanism and a dual level fork() mechanism for launching the application 
in its own process. gRun also has support for launching console mode application in an XTerm as well as 
associations for file types.
gRun is much more powerful than xexec, looks a lot better, and has the big advantage that you can start 
typing a command without having to mouse-click into the text field.

gRun is especially useful if you do not use the GNOME desktop which has a built-in run command, and if
you use a window-manager (e.g. IceWM) where you can define a keyboard shortcut (e.g. Alt-F2) for staring gRun. 

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%doc AUTHORS BUGS COPYING ChangeLog NEWS README
%_bindir/%name
%_man1dir/%name.*

%changelog
* Wed Mar 25 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.3-alt1
- Initial


