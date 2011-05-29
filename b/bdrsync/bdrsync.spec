# -*- coding: latin-1; mode: rpm-spec -*-

Name: bdrsync
Version: 0.1
Release: alt1

Summary: Block devices synchronization tool 
License: GPL2
Group: Archiving/Backup
Url: http://github.com/dottedmag/bdrsync
Source: %name-%version.tar

Packager: Evgenii Terechkov <evg@altlinux.org>

%description
Block devices synchronization tool 

%prep
%setup
%build
make

%install
install -m 755 -Dp %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc README.md

%changelog
* Sun May 29 2011 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
