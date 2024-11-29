Name: grun
Version: 0.9.3
Release: alt2

Summary: GTK based Run dialog

License: GPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/lrgc/grun.git
Packager: Dmitriy Khanzhin <jinn@altlinux.org>

Source: %name-%version.tar
Patch1: %name-%version-%release.patch

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
%setup
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS BUGS COPYING ChangeLog NEWS README
%_sysconfdir/*
%_bindir/%name
%_man1dir/%name.*

%changelog
* Fri Nov 29 2024 Dmitriy Khanzhin <jinn@altlinux.org> 0.9.3-alt2
- Last git snapshot ade6bae
- Fixed build with gcc-14
- Added russian translation
- Fixed tags: License, Url, Packager

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Mar 25 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.3-alt1
- Initial


