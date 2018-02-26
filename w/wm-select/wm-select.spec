Name: wm-select
Version: 0.8
Release: alt1

Summary: Application for selecting window manager at startup
License: GPL
Group: Graphical desktop/Other
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: %name-%version.tar

BuildRequires: libgtk+2-devel

%description
wm-select is a small Gtk application for selecting a window manager
at X startup.

%prep
%setup -q

%build
%make_build CFLAGS="%optflags"

%install
install -pD -m755 %name %buildroot%_bindir/%name
for f in *.mo; do
	lang="${f%%.mo}"
	install -pD -m644 "$f" "%buildroot%_datadir/locale/$lang/LC_MESSAGES/%name.mo"
done
%find_lang %name

%files -f %name.lang
%_bindir/*

%changelog
* Tue Oct 17 2006 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt1
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Sat Sep 16 2006 Dmitry V. Levin <ldv@altlinux.org> 0.7-alt1
- Handle invalid pixmaps gently.

* Mon May 15 2006 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
- Fixed build with gcc-4.1.0.

* Tue Mar 07 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5-alt1
- Fixed build with --as-needed.

* Thu Jan 12 2006 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Cleaned up build dependencies.
- Relocated binary to %_bindir/.

* Mon Nov 21 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Rewritten FillBox() in more portable way (fixes #8514).

* Sat Oct 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Implemented Gtk2 support.
- Build with Gtk2 by default.

* Wed Jan 09 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
