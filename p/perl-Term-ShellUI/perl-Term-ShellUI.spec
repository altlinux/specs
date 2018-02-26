# Spec file for Perl module Term::ShellUI

Name: perl-Term-ShellUI
Version: 0.91
Release: alt1

Summary: Perl module to write a fully-featured shell-like CLI

%define real_name Term-ShellUI

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Term-ShellUI/

Packager: Nikolay Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch
AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

BuildRequires: perl-Term-ReadLine-Gnu

%description
Perl module Term::ShellUI makes it easy to implement a
comprehensive Bash or GDB-like command line user interface.
It supports history, autocompletion, quoting, escaping,
pretty much everything you would expect of a decent shell.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes 
%perl_vendor_privlib/Term/ShellUI*
%perl_vendor_privlib/Text/Shellwords*

%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.91-alt1
- New version

* Sun May 29 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.9-alt1
- Initial build for ALT Linux Sisyphus
