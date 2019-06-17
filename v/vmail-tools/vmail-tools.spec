Summary: Virtual mailbox tools
Name: vmail-tools
Version: 0.1
Release: alt1
License: WTFPL
Group: Networking/Mail
URL: git://git.altlinux.org/gears/v/%name
Source: %name-%version.tar.xz
Requires: perl tcsh
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Tools for virtual mailbox maintenance

%prep
%setup -q -n %{name}-%{version}

%build
%make

%install
umask 022
rm -rf %buildroot
mkdir -p %buildroot%_bindir %buildroot%_sbindir
install -m 755 crypt mkpassphrase %buildroot%_bindir/
install -m 750 vmu %buildroot%_sbindir/

%clean
rm -rf %buildroot

%files
%defattr(-,root,mail)
%_bindir/*
%_sbindir/*

%changelog
* Mon Jun 17 2019 Gremlin from Kremlin <gremlin@altlinux.org> 0.1-alt1
- import from Owl
