Name: shared-desktop-ontologies
Version: 0.9.0
Release: alt1
Serial: 1

Group: System/Base
Summary: Semantic web to the desktop in terms of vocabulary
Url: http://sourceforge.net/projects/oscaf/
License: BSD

BuildArch: noarch

Source0: %name-%version.tar.bz2
Patch0: shared-desktop-ontologies-0.2-define-Version.patch

# Automatically added by buildreq on Mon Jan 18 2010 (-bi)
BuildRequires: cmake gcc-c++ kde-common-devel

%description
Open Semantic Collaboration Architecture Foundation (OSCAF) ontologies
and reference code development. This project is used maintainers from
open source projects to maintain standards for the interoperability
of desktop and web applications.

The shared-desktop-ontologies package brings the semantic web to the desktop
in terms of vocabulary. It contains the well known core ontologies such as RDF
and RDFS as well as the Nepomuk ontologies which are used by projects like KDE
or Strigi.


%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: %name

%description devel
This package contains header files needed if you wish to build applications
based on %name.

%prep
%setup -q
#%patch0 -p1

%build
%Kbuild

%install
%Kinstall

%files
%doc AUTHORS ChangeLog README LICENSE.*
%_datadir/ontology

%files devel
%_datadir/pkgconfig/shared-desktop-ontologies.pc
%_datadir/cmake/SharedDesktopOntologies

%changelog
* Wed Apr 18 2012 Sergey V Turchin <zerg@altlinux.org> 1:0.9.0-alt1
- new version

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.8.1-alt0.M60P.1
- built for M60P

* Tue Dec 13 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.8.1-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.8.0-alt1.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.8.0-alt1.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.8.0-alt2
- new version

* Wed Sep 07 2011 Sergey V Turchin <zerg@altlinux.org> 1:0.5-alt2
- temporary revert to 0.5

* Wed Aug 31 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 0.5-alt0.M51.1
- build for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 0.5-alt1
- new version

* Fri Apr 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.3-alt0.M51.1
- built for M51

* Fri Apr 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- new version

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 0.2-alt0.M51.1
- built for M51

* Mon Jan 18 2010 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- built for ALT

