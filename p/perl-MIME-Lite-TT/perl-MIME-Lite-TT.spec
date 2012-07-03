%define module MIME-Lite-TT

Name: perl-%module
Version: 0.02
Release: alt1

Summary: TT enabled MIME::Lite wrapper
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/H/HO/HORIUCHI/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Jan 11 2011
BuildRequires: perl-MIME-Lite perl-Template perl-devel

%description
MIME::Lite::TT is the wrapper of MIME::Lite which enabled Template::Toolkit as
a template of email.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/MIME/*

%changelog
* Tue Jan 11 2011 Victor Forsiuk <force@altlinux.org> 0.02-alt1
- Initial build.
