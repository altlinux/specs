%define dist POE-Component-Syndicator
Name: perl-%dist
Version: 0.06
Release: alt1

Summary: A POE component base class which implements the Observer pattern
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Object-Pluggable perl-POE perl-devel

%description
POE::Component::Syndicator is a base class for POE components which need
to handle a persistent resource (e.g. a connection to an IRC server) for
one or more sessions in an extendable way.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/POE

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- initial revision
