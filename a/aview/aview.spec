Name: aview
Version: 1.3.0
Release: alt2.rc1

Summary: High quality ascii-art image (pnm) browser and animation (fli/flc) player
License: GPL
Group: Graphics
Url: http://aa-project.sourceforge.net/aview/

Packager: Sergey Kurakin <kurakin@altlinux.org>

Source: %name-%{version}rc1.tar.gz
Patch1: %name-1.3.0-alt-tmpdir.patch


# Automatically added by buildreq on Fri Jun 15 2007
BuildRequires: aalib-devel libgpm-devel libslang-devel libX11-devel

%description
High quality ascii-art image(pnm) browser and animation(fli/flc) player.
Features:
- High quality ascii art rendering 
- Portable 
- Save into many formats (html, text, ansi, more/less etc...) 
- Contrast, Bright, Gamma control 
- Image zooming/unzooming 
- Three dithering modes 
- Hidden "bonus" features :) 
- Inversion 
- Support for bright, dim, inverse attributes/extended character set

%prep
%setup -n %name-%version
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall

%files
%doc ANNOUNCE AUTHORS ChangeLog INSTALL README README.flip NEWS TODO
%_bindir/*
%_man1dir/*

%changelog
* Fri Oct 24 2008 Sergey Kurakin <kurakin@altlinux.org> 1.3.0-alt2.rc1
- fixed unsafe tmp usage in scripts

* Fri Jun 15 2007 Sergey Kurakin <kurakin@altlinux.ru> 1.3.0-alt1.rc1
- initial build for Sisyphus

