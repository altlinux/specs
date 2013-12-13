Name: bustle
Version: 0.4.3
Release: alt1

Summary: D-Bus activity visualiser
License: LGPLv2.1+
Group: Development/Debug
Url: http://www.willthompson.co.uk/bustle/

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: libpcap-devel help2man ghc7.6.1-common ghc7.6.1-cairo
BuildRequires: ghc7.6.1-pango ghc7.6.1-dbus ghc7.6.1-gtk ghc7.6.1-pcap
BuildRequires: gtk2hs-buildtools glib2-devel libgio-devel libgtk+2-devel
BuildRequires: libxml2-devel

%description
Bustle is a tool to chart and provide timing information of D-Bus
calls for profiling and debugging purposes. It is intended to replace
reading the cryptic output of dbus-monitor.

Calls are displayed using Message Sequence Charts, a succinct way of
representing entities and interactions over time. It can also output
data in Graphviz format.

This package contains the graphical visualizer for traces generated
with the bustle-pcap tool.

%prep
%setup -q

%build
ghc -package Cabal Setup.hs -o setup
./setup configure --prefix /usr
./setup build

%make_build PREFIX=%prefix

%install
./setup copy --destdir %buildroot
%make_install PREFIX=%prefix DESTDIR=%buildroot install

%files
%doc HACKING INSTALL LICENSE* NEWS README
%_bindir/bustle
%_bindir/bustle-pcap
%dir %_datadir/%name-%version
%_datadir/%name-%version/
%_man1dir/bustle-pcap.*

%changelog
* Fri Dec 13 2013 Igor Zubkov <icesik@altlinux.org> 0.4.3-alt1
- 0.4.3

* Wed Sep 04 2013 Igor Zubkov <icesik@altlinux.org> 0.4.2-alt1
- build for Sisyphus

