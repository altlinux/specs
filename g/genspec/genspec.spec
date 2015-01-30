Name:     genspec
Version:  1.0.0
Release:  alt1

Summary:  Script for generation RPM spec file from template
License:  GPLv3+
Group:    System/Configuration/Packaging
URL: 	  http://altlinux.org/genspec
Packager: Andrey Cherepanov <cas@altlinux.org> 

BuildArch: noarch

Source:   %name-%version.tar

%description
Script for generation RPM spec file from template.

%prep
%setup

%install
install -Dm755 %name %buildroot%_bindir/%name
mkdir -p %buildroot%_datadir/spectemplates
cp -av spectemplates/* %buildroot%_datadir/spectemplates/

%files
%_bindir/%name
%_datadir/spectemplates

%changelog
* Fri Jan 30 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial publish
