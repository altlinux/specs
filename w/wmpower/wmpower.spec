# vim: set ft=spec: -*- rpm-spec -*-

Name: wmpower
Version: 0.4.3
Release: alt1

Summary: ACPI power status monitor for Window Maker
Group: Graphical desktop/Window Maker
License: GPL
Url: http://wmpower.sourceforge.net/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Fri Jul 08 2005
BuildRequires: libXext-devel libXpm-devel

%description
wmpower is a Window Maker dock application allowing the user to
graphically see (and set) the power management status of his laptop.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure MY_CFLAGS="%optflags"
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README THANKS
%_bindir/*

%changelog
* Sun Mar 28 2010 Alexey I. Froloff <raorn@altlinux.org> 0.4.3-alt1
- [0.4.3]
- Dropped menu entry and unneeded docs

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt4.1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmpower

* Fri Apr 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.4.2-alt4
- Fixed build on x86-64.
- Real fix for --as-needed.

* Tue Mar 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.4.2-alt3
- Fixed build with --as-needed.

* Mon Feb 06 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.4.2-alt2
- Fix building with XOrg7.0.

* Thu Oct 06 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.4.2-alt1
- 0.4.2 release.

* Tue Jul 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.4.1-alt1
- Initial build for Sisyphus.

