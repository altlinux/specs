Name: sshpass
Version: 1.05
Release: alt1
URL: http://sourceforge.net/projects/sshpass/

Summary: Non-interactive ssh password auth
License: %gpl2only
Group: System/Configuration/Networking
Packager: Andriy Stepanov <stanv@altlinux.ru>

Source: %name-%version.tar

BuildRequires: rpm-build-licenses

%description
Sshpass is a tool for non-interactivly performing password
authentication with SSH's so called "interactive keyboard password
authentication". Most user should use SSH's more secure public key
authentiaction instead.

%prep
%setup 

%build
%configure

%make_build

%install
%makeinstall

%files
%_bindir/%name
%_man1dir/%{name}*
%doc AUTHORS COPYING NEWS README

%changelog
* Wed Apr 18 2012 Andriy Stepanov <stanv@altlinux.ru> 1.05-alt1
- Forward to ALT Linux Sisyphus
