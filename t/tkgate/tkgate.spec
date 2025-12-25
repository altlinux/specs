%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: tkgate
Version: 2.1
Release: alt1

Summary: Tcl/Tk based digital circuit editor and simulator
License: GPL-2.0-or-later
Group: Engineering
Url: https://github.com/glixx/tkgate

Source: %name-%version.tar
Source1: index.html

# sync with version 2.1+repack-8 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires: flex
BuildRequires: pkgconfig(pangoxft)
BuildRequires: pkgconfig(tk)

Requires: tkgate-data

%description
TkGate is a digital circuit editor and simulator with a Tcl/Tk based
interface. TkGate includes a large number of built-in devices including basic
gates, memories, ttys and modules for hierarchical design. The simulator can
be controlled either interactively or through a simulation script. Memory
contents can be loaded from files, and a microcode/macrocode compiler (gmac)
is included to create tkgate memory files from a high-level description. The
simulator supports continuous simulation, single step simulation (by clock or
epoch) and breakpoints. Save files are in a Verilog-like format.

TkGate also includes a number of tutorial and example circuits which can be
loaded through the "Help" menu. The examples range from a simple gate-level
3-bit adder to a 16-bit CPU programmed to play the "Animals" game.

TkGate has a multi-language interface with support for English, Japanese,
French and Spanish.

%package data
Summary: Tcl/Tk based digital circuit editor and simulator - data files
Group: Engineering
BuildArch: noarch

%description data
TkGate is a digital circuit editor and simulator with a Tcl/Tk based
interface.

This package contains the architecture independent data files.

%package doc
Summary: Tcl/Tk based digital circuit editor and simulator - documentation
Group: Documentation
BuildArch: noarch

%description doc
TkGate is a digital circuit editor and simulator with a Tcl/Tk based
interface.

This package contains the documentation.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

# install index.html as done in Debian for tkgate-doc
install -m644 -D %SOURCE1 %buildroot%_datadir/tkgate/doc/index.html
cp -arv doc/* %buildroot%_datadir/tkgate/doc/

# make symlinks as done in Debian for tkgate-doc
mkdir -pv %buildroot%_datadir/doc/tkgate
ln -srfv %buildroot%_datadir/tkgate/doc %buildroot%_datadir/doc/tkgate/doc

mkdir -pv %buildroot%_datadir/doc/tkgate-doc
ln -srfv %buildroot%_datadir/tkgate/doc %buildroot%_datadir/doc/tkgate-doc/doc

mkdir -pv %buildroot%_datadir/doc/tkgate-data/examples
mv -v %buildroot%_datadir/tkgate/test/* %buildroot%_datadir/doc/tkgate-data/examples/

%check
# do some magic to run the testsuite as done in Debian
mkdir -pv %buildroot%_datadir/doc/tkgate-data/examples/../src/verga/
cp -pv %buildroot/usr/bin/verga %buildroot%_datadir/doc/tkgate-data/examples/../src/verga/verga

cd %buildroot%_datadir/doc/tkgate-data/examples/ && sh runtests.sh

rm -vf %buildroot%_datadir/doc/tkgate-data/examples/../src/verga/verga

%files
%doc README README.verga TODO
%doc ChangeLog COPYING
%_bindir/gmac
%_bindir/tkgate
%_bindir/verga
%_desktopdir/tkgate.desktop
%exclude %_datadir/doc/tkgate/COPYING
%exclude %_datadir/doc/tkgate/ChangeLog
%exclude %_datadir/doc/tkgate/README
%exclude %_datadir/doc/tkgate/README.verga
%exclude %_datadir/doc/tkgate/TODO
%exclude %_datadir/tkgate/libexec/tkgate
%exclude %_datadir/tkgate/libexec/verga
%_man1dir/gmac.1.*
%_man1dir/tkgate.1.*
%_man1dir/verga.1.*
%_pixmapsdir/tkgate.png
%_pixmapsdir/tkgate.xpm

%files data
%_datadir/tkgate/site-preferences
%_datadir/tkgate/images
%_datadir/tkgate/gdf
%_datadir/tkgate/locale
%_datadir/tkgate/scripts
%_datadir/tkgate/bindings
%_datadir/tkgate/vlib
%_datadir/tkgate/vpd
%_datadir/tkgate/primitives
%dir %_datadir/doc/tkgate-data/examples
%_datadir/doc/tkgate-data/examples/*
%exclude %_datadir/doc/tkgate-data/examples/verga/*.out

%files doc
%dir %_datadir/tkgate/doc
%_datadir/tkgate/doc/*
%_datadir/doc/tkgate-doc/doc
%_datadir/doc/tkgate/doc

%changelog
* Wed Dec 24 2025 Nikolay Strelkov <snk@altlinux.org> 2.1-alt1
- Initial build for Sisyphus
