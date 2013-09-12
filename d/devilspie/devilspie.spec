Name: devilspie
Version: 0.22
Release: alt2

Summary: A window matching tool inspired by the Matched Window options in Sawfish
License: GPLv2+
Group: Graphical desktop/Other
URL: http://www.burtonini.com/blog/computers/devilspie

Source0: http://www.burtonini.com/computing/%name-%version.tar.gz

Patch0: fix_gdk_display_ftbfs.patch
Patch1: fix_ftbfs_libx11_underlinkage.patch
Patch2: fix_ftbfs_with_binutils_gold.patch

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: intltool glib2-devel gnome-common libwnck-devel

%description
A window-matching utility, inspired by Sawfish's "Matched Windows" option and
the lack of the functionality in Metacity. Metacity lacking window matching is
not a bad thing -- Metacity is a lean window manager, and window matching does
not have to be a window manager task.

Devil's Pie can be configured to detect windows as they are created, and match
the window to a set of rules. If the window matches the rules, it can perform a
series of actions on that window. For example, I make all windows created by
X-Chat appear on all workspaces, and the main Gkrellm1 window does not appear
in the pager or task list.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure
%make_build

%check
make check || exit 1

%install
mkdir -p %buildroot%_sysconfdir/devilspie/
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README NEWS TODO
%dir %_sysconfdir/devilspie/
%_bindir/devilspie
%_man1dir/*

%changelog
* Thu Sep 12 2013 Igor Zubkov <icesik@altlinux.org> 0.22-alt2
- Sync patches with devilspie_0.22-2ubuntu1.debian

* Sat Nov 24 2007 Igor Zubkov <icesik@altlinux.org> 0.22-alt1
- 0.21 -> 0.22

* Tue Sep 25 2007 Igor Zubkov <icesik@altlinux.org> 0.21-alt1
- 0.20.2 -> 0.21

* Sun Feb 18 2007 Igor Zubkov <icesik@altlinux.org> 0.20.2-alt1
- 0.20.1 -> 0.20.2
- clean up build requires

* Sat Jan 13 2007 Igor Zubkov <icesik@altlinux.org> 0.20.1-alt1
- 0.19 -> 0.20.1
- enable check

* Tue Dec 12 2006 Igor Zubkov <icesik@altlinux.org> 0.19-alt1
- 0.18 -> 0.19
- buildreq

* Mon Oct 23 2006 Igor Zubkov <icesik@altlinux.org> 0.18-alt1
- 0.17.1 -> 0.18

* Sat Mar 25 2006 Igor Zubkov <icesik@altlinux.ru> 0.17.1-alt1
- 0.17.1

* Sun Jan 22 2006 Igor Zubkov <icesik@altlinux.ru> 0.16-alt1
- Initial build for Sisyphus

* Mon Sep 26 2005 Lars R. Damerow <lars@pixar.com> 0.13
- update to 0.13

* Fri Sep 16 2005 Lars R. Damerow <lars@pixar.com> 0.11
- update to 0.11
- removed setwintype patch

* Fri Sep 16 2005 Lars R. Damerow <lars@pixar.com> 0.10-2
- patch to fix setwintype crash

* Tue Aug 16 2005 Lars R. Damerow <lars@pixar.com> 0.10-1
- update to 0.10

* Mon Feb 07 2005 Lars R. Damerow <lars@pixar.com> 0.8-2
- update to 0.8
- add devilspie-reference.html

* Fri May  2 2003 Frederic Crozat <fcrozat@mandrakesoft.com>
- Package locale files

* Thu May 01 2003 Ross Burton <ross@burtonini.com>
- Initial spec file based on spec files by Michael Raab
  <mraab@macbyte.info> and Lars R. Damerow <lars@oddment.org>
