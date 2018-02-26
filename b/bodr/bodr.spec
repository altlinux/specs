Name: bodr
Version: 9
Release: alt1

Summary: Blue Obelisk Data Repository
Group: Sciences/Chemistry
License: MIT
Url: http://bodr.sourceforge.net

Source: http://downloads.sourceforge.net/%name/%name-%version.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Mon Mar 15 2010
BuildRequires: perl-devel xml-utils xsltproc

%description
The Blue Obelisk Movement is the name used by a diverse Internet group
promoting reusable chemistry via open source software development,
consistent and complimentary chemoinformatics research, open data, and
open standards.

The Blue Obelisk Data Repository lists many important chemoinformatics
data such as elemental properties, atomic radii, isotopes, atom typing
rules, etc. including references to original literature. Developers can
use this repository to make their software interoperable.

%define pkgdocdir %_docdir/%name-%version

%prep
%setup -q

%build
%configure --docdir=%pkgdocdir
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_datadir/bodr
%_datadir/pkgconfig/bodr.pc
%doc %pkgdocdir

%changelog
* Fri Aug 26 2011 Yuri N. Sedunov <aris@altlinux.org> 9-alt1
- new version

* Mon Mar 15 2010 Yuri N. Sedunov <aris@altlinux.org> 8-alt1
- first build for Sisyphus

