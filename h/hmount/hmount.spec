Name: hmount
Version: 0.2.2
Release: alt1

Packager: Alexey Borovskoy <alb@altlinux.ru>

Summary: %name - Tool to mount/umount hot-plugged devices via HAL interface.

License: GPL
Group: System/Base

Url: http://freshmeat.net/projects/hmount

Source: %name-%version.tar.bz2

Patch1: %name-%version-%release.patch

BuildPreReq: libhal-devel libdbus-devel

%description
Simple interface to HAL mount/umount actions.
Unlinke gnome-mount, not depend on gconf,  gtk, X, gnome libs.
Intended to mount/umount/list hot-plugged devices without huge amount
of programs and libraries.

%prep
%setup -q
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%_mandir/man?/*
%_bindir/*
%doc AUTHORS COPYING ChangeLog NEWS README TODO

%changelog
* Mon Oct 26 2009 Alexey Borovskoy <alb@altlinux.ru> 0.2.2-alt1
- Build for Sisyphus.

* Sun Jan 20 2008 Alexey Borovskoy <alb@altlinux.ru> 0.2.2-alt0.M40.1
- New version: 0.2.2.

* Mon May 28 2007 Alexey Borovskoy <alb@altlinux.ru> 0.2.1-alt0.M40.1
- Initial release for 4.0 branch.
