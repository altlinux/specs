%define dist Test-Taint
Name: perl-%dist
Version: 1.04
Release: alt2

Summary: Checks for taintedness of variables
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
Tainted data is data that comes from an unsafe source, such as the
command line, or, in the case of web apps, any GET or POST transactions.
Read the the perlsec manpage man page for details on why tainted data is bad,
and how to untaint the data.

When you're writing unit tests for code that deals with tainted data,
you'll want to have a way to provide tainted data for your routines to
handle, and easy ways to check and report on the taintedness of your data,
in standard the Test::More manpage style.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Test
%perl_vendor_autolib/Test

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.04-alt2
- rebuilt for perl-5.14

* Sat Dec 04 2010 Denis Baranov <baraka@altlinux.org> 1.04-alt1
- initial build for ALT Linux Sisyphus
