%define _unpackaged_files_terminate_build 1
%define dist Digest-Perl-MD5
Name: perl-%dist
Version: 1.9
Release: alt1

Summary: Perl Implementation of Rivest's MD5 algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DE/DELTA/Digest-Perl-MD5-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-devel

%description
This modules has the same interface as the much faster Digest::MD5.

%prep
%setup -q -n %dist-%version
chmod -c -x lib/Digest/Perl/MD5.pm

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc README
%perl_vendor_privlib/Digest

%changelog
* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1
- automated CPAN update

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 1.8-alt1
- initial revision
