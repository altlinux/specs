# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Summary: Documentation and tutorials for kicad
Name: kicad-doc
Version: 7.0.0
Epoch: 1
Release: alt1
Group: Documentation
License: GPLv3
Url: https://gitlab.com/kicad/services/kicad-doc
Source: %name-%version.tar
# Source-url: https://gitlab.com/kicad/services/kicad-doc/-/archive/%version/kicad-doc-%version.tar.bz2
BuildArch: noarch
BuildRequires(pre): cmake rpm-macros-cmake
BuildRequires: asciidoctor
BuildRequires: po4a

Requires: kicad-common >= %version

%description 
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
Enlish and Russian translation.

%package ca
Summary: Documentation and tutorials for kicad
Group: Documentation
BuildArch: noarch
Requires: kicad-common >= %version

%description ca
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
Canadian translation.

%package de
Summary: Documentation and tutorials for kicad
Group: Documentation
BuildArch: noarch
Requires: kicad-common >= %version

%description de
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
German translation.

%package es
Summary: Documentation and tutorials for kicad
Group: Documentation
BuildArch: noarch
Requires: kicad-common >= %version

%description es
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
Spanish translation.

%package fr
Summary: Documentation and tutorials for kicad
Group: Documentation
BuildArch: noarch
Requires: kicad-common >= %version

%description fr
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
French translation.

%package id
Summary: Documentation and tutorials for kicad
Group: Documentation
BuildArch: noarch
Requires: kicad-common >= %version

%description id
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
Indonesian translation.

%package it
Summary: Documentation and tutorials for kicad
Group: Documentation
BuildArch: noarch
Requires: kicad-common >= %version

%description it
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
Italian translation.

%package ja
Summary: Documentation and tutorials for kicad
Group: Documentation
BuildArch: noarch
Requires: kicad-common >= %version

%description ja
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
Japan translation.

%package nl
Summary: Documentation and tutorials for kicad
Group: Documentation
BuildArch: noarch
Requires: kicad-common >= %version

%description nl
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
Netherlandish translation.

%package pl
Summary: Documentation and tutorials for kicad
Group: Documentation
BuildArch: noarch
Requires: kicad-common >= %version

%description pl
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
Polish translation.

%package zh
Summary: Documentation and tutorials for kicad
Group: Documentation
BuildArch: noarch
Requires: kicad-common >= %version

%description zh
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
Chinese translation.

%prep
%setup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_FORMATS=html
%cmake_build

%install
%cmakeinstall_std

%files
%_datadir/doc/kicad/help/en
%_datadir/doc/kicad/help/ru

%files ca
%_datadir/doc/kicad/help/ca

%files de
%_datadir/doc/kicad/help/de

%files es
%_datadir/doc/kicad/help/es

%files fr
%_datadir/doc/kicad/help/fr

%files id
%_datadir/doc/kicad/help/id

%files it
%_datadir/doc/kicad/help/it

%files ja
%_datadir/doc/kicad/help/ja

#files nl
#_datadir/doc/kicad/help/nl

%files pl
%_datadir/doc/kicad/help/pl

%files zh
%_datadir/doc/kicad/help/zh

%changelog
* Sun Feb 12 2023 Anton Midyukov <antohami@altlinux.org> 1:7.0.0-alt1
- new version (7.0.0) with rpmgs script

* Sat Sep 10 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.7-alt1
- new version (6.0.7) with rpmgs script

* Wed Jun 22 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.6-alt1
- new version (6.0.6) with rpmgs script

* Sun May 08 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.5-alt1
- new version (6.0.5) with rpmgs script

* Wed Feb 23 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.2-alt1
- new version (6.0.2) with rpmgs script

* Tue Jan 04 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.0-alt1
- new version (6.0.0) with rpmgs script

* Tue Oct 12 2021 Anton Midyukov <antohami@altlinux.org> 1:5.1.4-alt2
- do not require kicad-data

* Mon Aug 19 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.4-alt1
- new version 5.1.4

* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.2-alt1
- new version 5.1.2

* Fri Mar 15 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.0-alt1
- new version 5.1.0

* Thu Jan 03 2019 Anton Midyukov <antohami@altlinux.org> 1:5.0.2-alt1
- new version 5.0.2

* Sun Nov 18 2018 Anton Midyukov <antohami@altlinux.org> 1:5.0.1-alt1
- new version 5.0.1

* Tue Jul 17 2018 Anton Midyukov <antohami@altlinux.org> 1:5.0.0-alt1.rc3
- Release candidate 5.0.0-rc3

* Wed Aug 30 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.7-alt1
- new version 4.0.7

* Thu Mar 09 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.6-alt1
- new version 4.0.6

* Thu Feb 23 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.5-alt1
- new version 4.0.5

* Wed Aug 31 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.4-alt1
- New version 4.0.4

* Sat Nov 29 2014 barssc <barssc@altlinux.ru> r647-alt1
- new version

* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 1.1-alt0.2
- fix Group

* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 1.1-alt0.1
- first build for ALT Linux

