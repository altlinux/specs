%define dist Perl-OSType
Name: perl-%dist
Version: 1.002
Release: alt1

Summary: Map Perl operating system names to generic types
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 28 2011
BuildRequires: perl-devel

%description
Modules that provide OS-specific behaviors often need to know if the
current operating system matches a more generic type of operating
systems. For example, 'linux' is a type of 'Unix' operating system and
so is 'freebsd'.

This module provides a mapping between an operating system name as given
by $^O and a more generic type. The initial version is based on the OS
type mappings provided in Module::Build and ExtUtils::CBuilder. (Thus,
Microsoft operating systems are given the type 'Windows' rather than
'Win32'.)

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Perl

%changelog
* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 1.002-alt1
- initial revision
