%define module MIME-Explode

Name: perl-%module
Version: 0.39
Release: alt2

Summary: Perl extension for explode MIME messages
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/modules/by-module/MIME/%module-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel

%description
MIME::Explode is Perl module for parsing and decoding single or
multipart MIME messages, and outputting its decoded components to a
given directory. This module is designed to allows users to extract
the attached files out of a MIME encoded email messages or mailboxes.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/MIME
%perl_vendor_autolib/MIME

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.39-alt2
- rebuilt for perl-5.14

* Tue Jul 19 2011 Victor Forsiuk <force@altlinux.org> 0.39-alt1
- 0.39

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.38-alt1.1
- rebuilt with perl 5.12

* Fri Jul 06 2007 Victor Forsyuk <force@altlinux.org> 0.38-alt1
- Initial build.
