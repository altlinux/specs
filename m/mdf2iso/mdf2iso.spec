Name: mdf2iso
Version: 0.3.0
Release: alt2
Summary: MDF to ISO Converter
License: GPL
Group: Archiving/Cd burning
URL: http://mdf2iso.berlios.de/

Packager: Pavlov Konstantin <thresh@altlinux.ru>

Source: %name-%version-src.tar.bz2
Patch0: mdf2iso-0.3.0-largefiles.patch

%description
MDF2ISO is a very simple utility to convert an 
Alcohol 120%% (c) (tm) bin image to the standard ISO-9660 format.

%prep
%setup -q -n %name

%patch0 -p1

%build
%configure
%make_build

%install
%makeinstall

%files 
#%doc %attr (644,root,root) CHANGELOG gpl.txt
#%attr (755,root,root) %_datadir/doc/%name-%version
%_bindir/%name

%changelog
* Tue Jan 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.0-alt2
- Added largefiles support patch.
- Added packager field.
- Minor descriptions/summaries cleanup.

* Sat Jun 11 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.3.0-alt1
- 0.3.0 release.

* Wed Mar 30 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.2.2-alt1
- Initial build for ALT Linux Sisyphus.

