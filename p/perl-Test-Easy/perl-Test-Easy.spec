%define dist Test-Easy
Name: perl-%dist
Version: 1.01
Release: alt1

Summary: Testing made absolute easy.
License: GPL or Artistic
Group: Development/Perl
Packager: Boris Savelev <boris@altlinux.org>

URL: %CPAN %dist
Source: http://search.cpan.org/CPAN/authors/id/D/DA/DANPEDER/%dist-%version.tar.gz
BuildArch: noarch

# Automatically added by buildreq on Mon Mar 16 2009
BuildRequires: perl-devel

%description
Easy testing suite.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Test/Easy.pm

%changelog
* Mon Mar 16 2009 Boris Savelev <boris@altlinux.org> 1.01-alt1
- initial build
