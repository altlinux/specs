%define dist POSIX-strptime

Name: perl-%dist
Version: 0.13
Release: alt1
Summary: Perl extension to the POSIX date parsing strptime(3) function
Group: Development/Perl
License: GPL+ or Artistic
URL: https://metacpan.org/release/POSIX-strptime

Source0: https://cpan.metacpan.org/authors/id/G/GO/GOZER/POSIX-strptime-%version.tar.gz

BuildRequires: perl-devel

%description
Perl interface to strptime(3).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/POSIX
%perl_vendor_autolib/POSIX

%changelog
* Tue Dec 07 2021 Valery Inozemtsev <shrek@altlinux.ru> 0.13-alt1
- initial release

