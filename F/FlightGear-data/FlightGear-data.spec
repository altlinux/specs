Name: FlightGear-data
Version: 2.6.0
Release: alt1

Summary: Data pack for FlightGear open-source flight simulator
License: GPL
Group: Games/Arcade

Url: http://www.flightgear.org
Packager: Michael Shigorin <mike@altlinux.org>
Source: %name-%version.tar.bz2

AutoReqProv: no
Provides: fgfs-data = %version-%release

BuildArch: noarch

# it's 450+ Mb of data
%brp_strip_none
%set_fixup_method skip
#set_strip_method none
%set_cleanup_method skip
%set_compress_method none
%set_verify_elf_method skip

%description
FlightGear is a free, open-source, multi-platform, and sophisticated
flight simulator framework for the development and pursuit of
interesting flight simulator ideas.

This package contains base FlightGear data files; feel free to
visit %url for more scenery and aircraft.

%package -n FlightGear-doc
Summary: Documentation for FlightGear open-source flight simulator
Group: Books/Computer books

%description -n FlightGear-doc
FlightGear is a free, open-source, multi-platform, and sophisticated
flight simulator framework for the development and pursuit of
interesting flight simulator ideas.

This package contains FlightGear documentation.

See also this nice and eagerly read tutorial:
http://www.4p8.com/eric.brasseur/flight_simulator_tutorial.html

%prep
%setup -n data

%install
mkdir -p %buildroot{%_datadir/flightgear,%_docdir}
mv Docs %buildroot%_docdir/FlightGear-%version
mv AUTHORS ChangeLog NEWS README %buildroot%_docdir/FlightGear-%version/
mv * %buildroot%_datadir/flightgear/

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find %buildroot -name 'Thumbs.db*' -print -delete

%files
%_datadir/flightgear

%files -n FlightGear-doc
%_docdir/FlightGear-%version

%changelog
* Sat Mar 03 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt1
- 2.6.0

* Sat Nov 12 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt2
- move to the current strip regulations, argh
- minor spec tweaks

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt1.1
- disable autoreq (we don't need no svginstr)
- FG-2.4 data expected in %_datadir/flightgear (no camelcase)

* Thu Sep 15 2011 Andrew Clark <andyc@altlinux.org> 2.4.0-alt1
- version update to 2.4.0-alt1

* Tue Mar 2 2010 Andrew Clark <andyc@altlinux.org> 2.0.0-alt1
- update to version 2.0.0-alt1

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.9.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * windows-thumbnail-database-in-package for FlightGear-data
  * postclean-05-filetriggers for spec file

* Tue Mar 24 2009 Michael Shigorin <mike@altlinux.org> 1.9.0-alt1
- 1.9.0
- spec cleanup

* Tue Jan 08 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 0.9.10-alt1
- 0.9.10
- fixes #8683
- noarch
- optimized packaging
  + danced with set_*_method macro parameters
- removed COPYING (standard GPLv2, see License: tag)

* Sat Dec 03 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.9.9-alt1
- Update to 0.9.9 version

* Fri Jan 21 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.9.8-alt1
- Update to 0.9.8 version

* Tue Sep 14 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.9.6-alt2.pre1
- Airports data file moved into main FlightGear package

* Tue Sep 14 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.9.6-alt1.pre1
- New version build
- Added FlightGear launcher
- Removed old menu entries

* Sat Jun 14 2003 Albert R. Valiev <darkstar@altlinux.ru> 0.9.2-alt1
- Initial build to sisyphus
- Created menu entries for majority of flyable aircrafts
