%define dist ph
Name: perl-%dist
Version: 0.10
Release: alt1

Summary: Perl *.ph files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar

# Automatically added by buildreq on Sun Sep 19 2010
BuildRequires: perl-devel

%description
This package provides the following Perl header files.

	ioctl.ph	sys/ioctl.ph
	syscall.ph	sys/syscall.ph
	syslog.ph	sys/syslog.ph
	socket.ph	sys/socket.ph

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/*.ph
%dir %perl_vendor_archlib/sys
%perl_vendor_archlib/sys/*.ph

%changelog
* Sun Sep 19 2010 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- separate package
