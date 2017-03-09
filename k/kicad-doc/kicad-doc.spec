Summary: Documentation and tutorials for kicad
Name: kicad-doc
Version: 4.0.6
Epoch: 1
Release: alt1
Group: Documentation
License: GPLv3
Url: https://github.com/KiCad/kicad-doc
Source:	%name-%version.tar
BuildArch: noarch
BuildRequires(pre): cmake rpm-macros-cmake
BuildRequires: dblatex po4a asciidoc-a2x source-highlight git
Requires: kicad-data

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
Requires: %name = %version-%release

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
Requires: %name = %version-%release

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
Requires: %name = %version-%release

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
Requires: %name = %version-%release

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
Requires: %name = %version-%release

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
Requires: %name = %version-%release

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
Requires: %name = %version-%release

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
Requires: %name = %version-%release

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
Requires: %name = %version-%release

%description pl
KiCad is a open source (GPL) integrated package for schematic circuit capture
and PCB layout.
This is the documentation package for kicad. It contains documentation,
tutorials and files localization.
Polish translation.

%prep
%setup

%build
%cmake_insource \
		-DCMAKE_BUILD_TYPE=Release \
		-DBUILD_FORMATS=html
%make_build

%install
%makeinstall_std

%files
%dir %_datadir/doc/kicad/help
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

%files nl
%_datadir/doc/kicad/help/nl

%files pl
%_datadir/doc/kicad/help/pl

%changelog
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

