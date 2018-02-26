%define dist Mail-Transport-Dbx
Name: perl-%dist
Version: 0.07
Release: alt2.2

Summary: Parse Outlook Express mailboxes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
Mail::Transport::Dbx is a wrapper around libdbx to read Outlook Express
mailboxes (more commonly known as .dbx files). It relies on a patched
version of libdbx to make it work on big-endian machines (like Solaris).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Mail
%perl_vendor_autolib/Mail

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.07-alt2.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt2.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt2
- fix directory ownership violation

* Sat Feb 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- initial build for ALT Linux Sisyphus

