%define dist Package-Stash-XS
Name: perl-%dist
Version: 0.25
Release: alt1

Summary: Faster and more correct implementation of the Package::Stash API
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Test-Fatal

%description
This is a backend for Package::Stash, which provides the functionality in
a way that's less buggy and much faster.  It will be used by default if it's
installed, and should be preferred in all environments with a compiler.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Package*
%perl_vendor_autolib/Package*

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- initial revision
