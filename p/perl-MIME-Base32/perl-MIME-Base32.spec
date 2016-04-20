%define module MIME-Base32

Name: perl-%module
Version: 1.301
Release: alt1

Summary: Base32 encoder/decoder
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/R/RE/REHSACK/MIME-Base32-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Oct 05 2009
BuildRequires: perl-devel

%description
Encode data similar way like MIME::Base64 does. Main purpose is to create
encrypted text used as id or key entry typed-or-submitted by user.

%prep
%setup -n MIME-Base32-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/MIME
#exclude %perl_vendor_privlib/MIME/test1.pl

%changelog
* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.301-alt1
- automated CPAN update

* Sat Aug 13 2011 Victor Forsiuk <force@altlinux.org> 1.02a-alt1
- 1.02a

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 05 2009 Victor Forsyuk <force@altlinux.org> 1.01-alt1
- Initial build.
