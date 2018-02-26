Name: wmMoonClock
Version: 1.27
Release: alt4

Packager: Sir Raorn <raorn@altlinux.ru>

Summary: Dockable Moon Phase Clock
Group: Graphical desktop/Window Maker
License: GPL
URL: http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml

Source: http://nis-www.lanl.gov/~mgh/WindowMaker/%name-%version.tar.gz

Patch: %name-1.27-alt-link.patch
Patch1: 01_all_previous_diff.diff
Patch2: 02_update_time.diff
Patch3: 03_add_southern_hemisphere_support.diff
Patch4: 04_fix_hyphen_used_as_minus_sign.diff

# Automatically added by buildreq on Thu Aug 27 2009
BuildRequires: libXext-devel libXpm-devel

%description
wmMoonClock displays the current phase of the moon. Clicking on
the icon brings up different displays -- there are 5 in all.

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cd Src
%make_build CFLAGS="%optflags"

%install
cd Src
install -p -D -pm755 %name $RPM_BUILD_ROOT%_bindir/%name
install -p -D -pm644 %name.1 $RPM_BUILD_ROOT%_man1dir/%name.1

%files
%doc BUGS COPYING
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Thu Aug 27 2009 Alexey I. Froloff <raorn@altlinux.org> 1.27-alt4
- Applied Debian patches (closes: #18547)
  + Add southern hemisphere support
  + Enhanced display refresh rate
- Dropped menu entry

* Sun Mar 19 2006 Sir Raorn <raorn@altlinux.ru> 1.27-alt3
- Fixed wrong libm linking
- Rebuilt with Xorg7, buildreqs updated

* Mon Oct 07 2002 Stanislav Ievlev <inger@altlinux.ru> 1.27-alt2
- rebuild with gcc3
- added Packager Tag
- added URL

* Mon Dec 03 2001 Sir Raorn <raorn@altlinux.ru> 1.27-alt1
- Built for Sisyphus

