Name: icon-naming-utils
Version: 0.8.90
Release: alt1

Summary: Utilities to maintain compatibility between freedesktop.org Icon Naming Spec and GNOME/KDE
Summary(ru_RU.UTF8): Утилиты для поддержки совместимости между freedesktop.org Icon Naming Specification и GNOME/KDE
License: GPL
Group: Graphical desktop/GNOME
Url: http://tango.freedesktop.org/Standard_Icon_Naming_Specification

Source: http://tango.freedesktop.org/releases/%name-%version.tar

BuildArch: noarch

BuildPreReq: perl-XML-Simple

%description
This package provides transitional utilities to assist in creating icon themes for existing desktop environments, such as GNOME and KDE, that are compatible with freedesktop.org Icon Naming Specification.

%description -l ru_RU.UTF8
Этот пакет содержит утилиты, помогающие создавать темы значков, соответствующие спецификации freedesktop.org по именованию значков, для существующих графических сред, таких как GNOME и KDE.

%prep
%setup -q

%build
%configure
%make

%install
%make_install install DESTDIR=%buildroot

%files
%_libexecdir/icon-name-mapping
%dir %_datadir/dtds
%_datadir/dtds/legacy-icon-mapping.dtd
%dir %_datadir/%name
%_datadir/%name/legacy-icon-mapping.xml
%_datadir/pkgconfig/%name.pc

%changelog
* Mon Mar 09 2009 Alexey Rusakov <ktirf@altlinux.org> 0.8.90-alt1
- new version (0.8.90)
- moved to git/git.alt

* Mon Sep 08 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8.7-alt1
- new version (0.8.7)

* Fri Sep 07 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8.6-alt1
- new version (0.8.6)

* Thu Mar 01 2007 Igor Zubkov <icesik@altlinux.org> 0.8.2-alt1
- 0.8.1 -> 0.8.2

* Thu Aug 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Sun Aug 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.8.0-alt1
- initial Sisyphus package.

