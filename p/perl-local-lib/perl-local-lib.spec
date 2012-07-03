%define dist local-lib
Name: perl-%dist
Version: 1.008004
Release: alt1

Summary: Create and use a local lib/ for perl modules with PERL5LIB
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Nov 10 2011
BuildRequires: perl-CPAN perl-Capture-Tiny perl-File-HomeDir perl-Module-Build perl-Pod-Parser

%description
This module provides a quick, convenient way of bootstrapping a user-local
Perl module library located within the user's home directory. It also
constructs and prints out for the user the list of environment variables
using the syntax appropriate for the user's current shell (as specified
by the SHELL environment variable), suitable for directly adding to one's
shell configuration file.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/lib
%perl_vendor_privlib/local

%changelog
* Thu Nov 10 2011 Alexey Tourbin <at@altlinux.ru> 1.008004-alt1
- initial revision
