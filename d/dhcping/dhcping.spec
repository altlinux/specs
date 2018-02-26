# $Id: dhcping.spec 2975 2005-03-09 05:31:45Z dag $
# Authority: dries
# Upstream: Edwin Groothuis <edwin$mavetju,org>

Summary: DHCP daemon ping program
Name: dhcping
Version: 1.2
Release: alt2
License: BSD
Group: Communications
Packager: Pavlov Konstantin <thresh@altlinux.ru>
URL: http://sourceforge.net/projects/mavetju
Source: http://www.mavetju.org/download/dhcping-%{version}.tar.gz

%description
Dhcping allows the system administrator to check if a remote DHCP 
server is still functioning.

%prep
%setup

%build
%configure \
	--program-prefix="%?_program_prefix"

%make

%install
%makeinstall

%files
%doc CHANGES CONTACT LICENSE
%doc %_mandir/man?/*
%_bindir/dhcping

%changelog
* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2-alt2
- Minor spec cleanup.
- Added Packager field.

* Sat Feb 11 2006 Grigory Milev <week@altlinux.ru> 1.2-alt1
- Initial build for ALT Linux

* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 1.2-2 #2975
- Cosmetic changes.
- Fix program-prefix for RH73 and older.

* Sun Mar 21 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- Initial package
