%define oversion V39
%define pversion V3
%define ppversion V2
Summary: Squeak Sources
Name: squeak-sources
Version: 3.9
Release: alt0.3

License: MIT
Url: http://www.squeak.org

Group: Development/Other
Packager: Anton A. Vinogradov <arc@altlinux.org> 

Source0:  Squeak%oversion.sources.gz
Source1:  Squeak%pversion.sources.gz
Source2:  Squeak%ppversion.sources.gz

BuildArch: noarch

BuildRequires: gzip

#Requires:      squeak-vm >= 3.10
#Requires:      squeak-image >= 3.0.3552

%description
These are the source files needed for the Squeak Virtual Machiene.


%install
mkdir -p %buildroot%_datadir/squeak/
mkdir -p %buildroot/extract/

cp %SOURCE0 %buildroot/extract/; gunzip -f %buildroot/extract/Squeak%oversion.sources.gz
mv %buildroot/extract/Squeak%oversion.sources %buildroot%_datadir/squeak/

cp %SOURCE1 %buildroot/extract/; gunzip -f %buildroot/extract/Squeak%pversion.sources.gz
mv %buildroot/extract/Squeak%pversion.sources %buildroot%_datadir/squeak/

cp %SOURCE2 %buildroot/extract/; gunzip -f %buildroot/extract/Squeak%ppversion.sources.gz
mv %buildroot/extract/Squeak%ppversion.sources %buildroot%_datadir/squeak/

%files
%defattr(0644,root,root,0755)
%_datadir/squeak/*




%changelog
* Thu Jan 28 2010 Anton A. Vinogradov <arc@altlinux.org> 3.9-alt0.3
- switch arch to "noarch"

* Wed Jan 27 2010 Anton A. Vinogradov <arc@altlinux.org> 3.9-alt0.2
- initial build for ALT Linux
