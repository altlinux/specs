# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*-
# $Id: sisyphus_list.spec,v 0.0.1 2005/04/12 20:02:51 legion Exp $

Name: sisyphus_list
Version: 1.4.1.4
Release: alt1

Summary: Tools for management of Sisyphus lists.
License: GPL
Group: Development/Other

BuildArch: noarch
Source: %name-%version.tar.bz2

Requires: sisyphus

%description
This package contain utility for managemant of Sisyphus lists.

%prep
%setup -q

%install
%__mkdir_p %buildroot/%_bindir
%__cp -f sisyphus_link_* %buildroot/%_bindir/

%files
%_bindir/*

%changelog
* Sun Feb 26 2006 Alexey Gladkov <legion@altlinux.ru> 1.4.1.4-alt1
- sisyphus_link_move - removed

* Tue Jun 21 2005 Alexey Gladkov <legion@altlinux.ru> 1.4.1.3-alt1
- sisyphus_link_owner - bugfixes;

* Tue May 24 2005 Alexey Gladkov <legion@altlinux.ru> 1.4.1.2-alt1
- Build new version;
  * sisyphus_link_groups added;
- Strings quoting bugfixes;
- Requires added;

* Tue Apr 12 2005 Alexey Gladkov <legion@altlinux.ru> 1.4.1.1-alt1
- Initial revision.
