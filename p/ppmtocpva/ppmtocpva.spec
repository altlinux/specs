Name: ppmtocpva
Version: 1.0
Release: alt1
License: GPL
Group: System/Configuration/Printing

Url: http://www.stevens-bradfield.com/ppmtomd/

# Source: http://www.dcs.ed.ac.uk/home/jcb/%name-%version.tar.bz2
Source: %name-%version.tar
Patch1: ppmtocpva-1.0-netpbm.patch
Patch2: ppmtocpva-1.0-LDFLAGS.patch
BuildRequires: libnetpbm-devel

Summary: Converts PPM files to the format used by the Citizen Printiva series printers
%description
This program converts PPM files to the format used by the Citizen Printiva
series printers and some printers of the Alps MD series.

%prep
%setup
%patch1 -p1
%patch2 -p0

# fix attribs
chmod 644 *

%build
%make CFLAGS="%optflags"

%install
install -d %buildroot%_bindir

install -m0755 ppmtocpva %buildroot%_bindir/
install -m0755 cpva-colour %buildroot%_bindir/

%files
%doc README
%_bindir/*

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.0-alt1
- Initial build for ALT

