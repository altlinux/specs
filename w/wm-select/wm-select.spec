%def_without runwm
%def_without xdg
%def_without gtk3
Name: wm-select
Version: 0.9.9
Release: alt1

Summary: Application for selecting window manager at startup
License: GPLv2+
Group: Graphical desktop/Other

Url: http://altlinux.org
Source: %name-%version.tar

%if_with gtk3
BuildRequires: libgtk+3-devel
%else
BuildRequires: libgtk+2-devel
%endif

%description
wm-select is a small Gtk application for selecting a window manager
at X startup.

%if_with runwm
%package -n runwm
Group: System/X11
Summary: Executes window manager using wm.d or xsessions database
Conflicts: xinitrc < 2.4.47-alt3

%description -n runwm
runwm is a tool for non-XDG compliant Display Managers that launches
window manager using wm.d or xsessions database.
%endif


%prep
%setup

%build
%make_build CFLAGS="%optflags" \
%if_without xdg
	    WITH_WM_SESSION=yes \
%endif
%if_with gtk3
	    WITH_GTK2= \
%else
	    WITH_GTK2=yes \
%endif
	    all

%install
install -pD -m755 %name %buildroot%_bindir/%name

%if_with runwm
install -pD -m755 runwm %buildroot%_bindir/runwm
%else
install -pD -m755 runwm %buildroot%_bindir/runwm.test
%endif

for f in *.mo; do
	lang="${f%%.mo}"
	install -pD -m644 "$f" "%buildroot%_datadir/locale/$lang/LC_MESSAGES/%name.mo"
done
%find_lang %name

%files -f %name.lang
%_bindir/%name

%if_with runwm
%files -n runwm
%_bindir/runwm
%else
%_bindir/runwm.test
%endif

%changelog
* Tue Dec 07 2021 Igor Vlasenko <viy@altlinux.org> 0.9.9-alt1
- new version

* Tue Nov 16 2021 Igor Vlasenko <viy@altlinux.org> 0.9.8-alt2
- runwm package enabled for xinitrc migration

* Tue Nov 16 2021 Igor Vlasenko <viy@altlinux.org> 0.9.8-alt1
- new version

* Mon Nov 15 2021 Igor Vlasenko <viy@altlinux.org> 0.9.7-alt1
- new version

* Sat Nov 13 2021 Igor Vlasenko <viy@altlinux.org> 0.9.6-alt2
- runwm package enabled

* Sat Nov 13 2021 Igor Vlasenko <viy@altlinux.org> 0.9.6-alt1
- new version

* Wed Nov 10 2021 Igor Vlasenko <viy@altlinux.org> 0.9.5-alt1
- new version:
- set XDG_CURRENT_SESSION from DesktopNames= in XDG mode
- misc improvements

* Tue Nov 09 2021 Igor Vlasenko <viy@altlinux.org> 0.9.4-alt1
- new version:
- added future runwm replacement as runwm.test for now

* Sun Oct 31 2021 Igor Vlasenko <viy@altlinux.org> 0.9.3-alt1
- new version:
- command line options, sessions (ALT/XDG) selection

* Sat Oct 30 2021 Igor Vlasenko <viy@altlinux.org> 0.9.2-alt1
- new version:
- optional XDG sessions support (/usr/share/xsessions)
- icon themes support

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1
- new version (-Werror compatible)

* Sat Mar 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt2
- to Sisyphus

* Sat Mar 28 2020 Michael Shigorin <mike@altlinux.org> 0.8.1-alt1.1
- Fixed FTBFS in face of GTypeDebugFlags/GTimeVal deprecation
  and missing upstream attention through dropping -Werror.

* Wed Sep 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1
- ported for gtk3 and modern gtk2;
- removed gtk1 support;
- support for .png, .svg pixmaps; re-scaling pixmaps to 64x64.

* Thu Jul 12 2012 Dmitry V. Levin <ldv@altlinux.org> 0.8.1-alt1
- Fixed build with new gcc.

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
