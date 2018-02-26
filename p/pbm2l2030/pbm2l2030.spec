Summary: Driver for the Lexmark 2030 printer

Name: pbm2l2030
Version: 1.4
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

Group: Publishing
License: GPL
Source: %name-%version.tar

%description
Lexmark 2030 Color Jetprinter printer driver.

%prep

%setup -q

%build
%__cc %optflags -o pbm2l2030 pbm2l2030.c pbm.c

%install
%__install -Dpm 755 %name %buildroot%_bindir/%name

%files
%doc README* LICENSE *.pbm
%_bindir/*

%changelog
* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 1.4-alt1
- Initial build
