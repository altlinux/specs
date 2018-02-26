Summary: Driver for the Alps Micro-Dry printers and similars

Name: ppmtomd
Version: 1.5
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

License: GPL
Group: Publishing

URL: http://www.stevens-bradfield.com/ppmtomd/
Source: http://www.stevens-bradfield.com/ppmtomd/%name-%version.tar
Patch: ppmtomd-1.3-alt-build.patch

# Automatically added by buildreq on Wed Nov 07 2007
BuildRequires: libnetpbm-devel

%description
A program to convert images from PPM format into the control language for the
Alps Micro-Dry printers, at various times sold by Citizen, Alps and Okidata.

This program drives the Alps Micro-Dry series of printers, including the
Citizen Printiva series, Alps MD series, and Oki DP series (but not yet the
DP-7000).

In the current release, the program drives the standard mode fairly well; the
dye sublimation mode very well; and the VPhoto mode reasonably well.

It supports all the colours available up to the DP-5000, including the foil
colours.

%prep

%setup -q
%patch -p1

chmod a+r *

%build
%make CFLAGS="%optflags"

%install

%__install -d %buildroot%_bindir
%__install -d %buildroot%_man1dir

%make BINDIR=$RPM_BUILD_ROOT%_bindir MANDIR=$RPM_BUILD_ROOT%_man1dir install

%files
%doc LICENCE README
%_bindir/*
%_man1dir/*


%changelog
* Wed Nov 07 2007 Stanislav Ievlev <inger@altlinux.org> 1.5-alt1
- Build as a separate package
