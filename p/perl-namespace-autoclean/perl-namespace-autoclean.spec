%define dist namespace-autoclean
Name: perl-%dist
Version: 0.13
Release: alt2

Summary: Keep imports out of your namespace
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-Moose perl-devel perl-namespace-clean

%description
When you import a function into a Perl package, it will naturally also be
available as a method.

The namespace::autoclean pragma will remove all imported symbols at the end
of the current package's compile cycle. Functions called in the package itself
will still be bound by their name, but they won't show up as methods on your
class or instances.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/namespace

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt2
- updated build dependencies

* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- 0.11 -> 0.13

* Wed May 26 2010 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- 0.09 -> 0.11

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- initial revision, for DBIx::Class
