Name:    logisim
Version: 2.7.1
Release: alt1

Summary: Graphical tool for designing and simulating logic circuits
License: GPL
Group:   Sciences/Computer science
URL:     http://ozark.hendrix.edu/~burch/logisim/
BuildArch: noarch

Requires: jre >= 1.5.0
Source0: %name
Source1: %name-generic-%version.jar
Source2: %name-icon-128.png
Source3: %name.desktop

AutoReqProv: no

%description
Graphical tool for designing and simulating logic circuits.
Logisim is an educational tool for designing and simulating digital
logic circuits. With its simple toolbar interface and simulation of
circuits as you build them, it is simple enough to facilitate learning
the most basic concepts related to logic circuits. With the capacity to
build larger circuits from smaller subcircuits, and to draw bundles of
wires with a single mouse drag, Logisim can be used (and is used) to 
design and simulate entire CPUs for educational purposes.

%install
mkdir -p %buildroot%_bindir
cp -f %SOURCE0 %buildroot%_bindir
mkdir -p %buildroot%_datadir/{%{name},pixmaps,applications}
cp -f %SOURCE1 %buildroot%_datadir/%name
cp -f %SOURCE2 %buildroot%_pixmapsdir
cp -f %SOURCE3 %buildroot%_desktopdir

%files
%_bindir/%name
%_datadir/%name
%_pixmapsdir/%name-icon-128.png
%_desktopdir/%name.desktop

%changelog
* Thu Dec 26 2013 Andrey Cherepanov <cas@altlinux.org> 2.7.1-alt1
- Initial build in Sisyphus

* Thu Sep 13 2012 AlexL <loginov.alex.valer@gmail.com> 2.7.1-1
- first build for Mageia
