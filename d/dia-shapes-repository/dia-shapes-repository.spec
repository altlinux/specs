Name: dia-shapes-repository
# No version here. Usiny YEAR.SERIAL
Version: 2010.11
Release: alt1
Buildarch: noarch
Group: Office
Requires: dia
License: GPL
# No single source here, see get.sh in documentation
Source: %name-%version.tar
Source1: get.sh
URL: http://dia-installer.de/shapes.html
Summary: Additional shapes that can be added to the Dia toolbox
Packager: Fr. Br. George <george@altlinux.ru>

%description
    * building_site.zip - Building site shapes more...
    * central_data_processing.zip - Central data processing shapes by Leonardo Oceano Martins more...
    * chemistry_lab.zip - chemistry lab shapes by Ryan Stewart more...
    * Circuit2.zip - Additional Circuit shapes by Terry Sturtevant more...
    * cmos.zip - CMOS shapes by Jason Klaus more...
    * digital.zip - Digital shapes by Jason Klaus more...
    * edpc.zip - EPC shapes more...
    * electric2.zip - Additional electronic shapes by Manoj Rawat more...
    * electronic.zip - Electronic shapes by Jaroslav Benkovsky more...
    * gradient.zip - Gradient shapes more...
    * lst.zip - Living Systems Theory shapes by Ian Smith more...
    * optics.zip - Optics shapes by Johann Kellerman more...
    * Racks.zip - Server rack shapes by Jaroslav Benkovsky more...
    * renewable_energy.zip - Renewable energy shapes by W. Martin Borgert more...
    * scenegraph.zip - Scene graph shapes by Alejandro Aguilar Sierra more...
    * value_stream_mapping.zip - Value stream mapping more...

%prep
%setup

%build
cp %SOURCE1 .

%install
mkdir -p %buildroot%_datadir/dia/shapes %buildroot%_datadir/dia/sheets
cp -a shapes/* %buildroot%_datadir/dia/shapes/
cp -a sheets/* %buildroot%_datadir/dia/sheets/

%files
%doc docs/*
%doc *.sh
%_datadir/dia/shapes/*
%_datadir/dia/sheets/*



%changelog
* Thu Nov 04 2010 Fr. Br. George <george@altlinux.ru> 2010.11-alt1
+ New shape: gradient

* Wed Aug 18 2010 Fr. Br. George <george@altlinux.ru> 2010.3-alt1
+ New shapes: building_site, value_stream_mapping

* Sat Nov 28 2009 Fr. Br. George <george@altlinux.ru> 2009.2-alt1
+ New shapes: Circuit2

* Thu Nov 19 2009 Fr. Br. George <george@altlinux.ru> 2009.1-alt1
- Version up

* Wed Oct 15 2008 Fr. Br. George <george@altlinux.ru> 2008.1-alt1
- Initial build from scratch

