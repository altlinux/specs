%define module MIME-Lite-TT-HTML

Name: perl-%module
Version: 0.04
Release: alt1

Summary: Create html mail with MIME::Lite and TT
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHUNZI/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Jan 11 2011
BuildRequires: perl-DateTime-Format-Mail perl-HTML-FormatText-WithLinks perl-MIME-Lite perl-MIME-tools perl-Module-Build perl-Template

%description
This module provide easy interface to make MIME::Lite object with html
formatted mail.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/MIME/*

%changelog
* Tue Jan 11 2011 Victor Forsiuk <force@altlinux.org> 0.04-alt1
- Initial build.
