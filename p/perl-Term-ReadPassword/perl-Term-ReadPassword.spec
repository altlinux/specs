%define module Term-ReadPassword
%define m_distro Term-ReadPassword
%define m_name Term::ReadPassword
%define m_author_id unknown
%define _enable_test 1

Name: perl-Term-ReadPassword
Version: 0.11
Release: alt2

Summary: Asking the user for a password 

License: Unknown
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: %m_distro-%version.tar.gz

BuildRequires: perl-devel
BuildRequires: perl-Term-ReadLine-Gnu

%description
This module lets you ask the user for a password in the traditional way, from the keyboard, without echoing.
This is not intended for use over the web; user authentication over the web is another matter entirely.
Also, this module should generally be used in conjunction with Perl's crypt() function, sold separately.
The read_password function prompts for input, reads a line of text from the keyboard, then returns that line to the caller.
The line of text doesn't include the newline character, so there's no need to use chomp.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%dir %perl_vendor_privlib/Term
%perl_vendor_privlib/Term/ReadPassword.pm

%changelog
* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11-alt2
- build repaired

* Mon Sep 01 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11-alt1
- 0.11
- build repaired

* Fri Jun 29 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 0.07-alt1
- Initial for Sisyphus
