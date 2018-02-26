Name: xres
Version: 1.3
Release: alt1

Summary: Tool for changing the X screen resolution
License: GPL
Group: System/X11

Source: %name-%version.tar

BuildPreReq: libX11-devel libXext-devel libXxf86vm-devel
%{?!_without_check:%{?!_disable_check:BuildPreReq: xvfb-run}}

%description
This tool make it possible to see which resolutions are available
and to choose one.

%prep
%setup

%build
%__cc %optflags -W -Werror xres.c -lX11 -lXext -lXxf86vm -o xres

%install
install -pD -m755 xres %buildroot%_bindir/xres

%check
xvfb-run -a %buildroot%_bindir/xres

%files
%_bindir/*

%changelog
* Sun Apr 11 2010 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Fixed build with fresh xorg.
- Updated build requirements.

* Tue Mar 07 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt2
- Fixed build with --as-needed.

* Thu Oct 07 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Fixed program behaviour then "XFree86-VidModeExtension"
  is missing on display.
- Added test case.

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt2
- rebuild with gcc3

* Fri Mar 15 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt1
- Repackaged

* Wed Dec 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl1
- RE adaptions.

* Wed Aug 18 1999 Dmitry V. Levin <ldv@fandra.org>
- Initial revision.
