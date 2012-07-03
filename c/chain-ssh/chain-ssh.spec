Name: chain-ssh
Version: 1.0
Release: alt2

Summary: Utility for chained ssh access for remote hosts
License: GPLv3
Group: Shells
Url: http://git.altlinux.org/people/gns/
Packager: Mykola Grechukh <gns@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar.gz

%description
This package provides tool for 'chained' ssh access to 
remote hosts via 'proxy' hosts.

%prep
%setup

%build

%install
install -D %name.sh %buildroot/%_bindir/%name

%files
%_bindir/*

%changelog
* Wed Apr 14 2010 Mykola Grechukh <gns@altlinux.ru> 1.0-alt2
- licensing information added to code ;)

* Wed Apr 14 2010 Mykola Grechukh <gns@altlinux.ru> 1.0-alt1
- first public version
