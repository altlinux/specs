%define dist UNIVERSAL-moniker
Name: perl-%dist
Version: 0.08
Release: alt2

Summary: Guess how class would be called in real world
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Lingua-EN-Inflect perl-devel

%description
UNIVERSAL::moniker enables classes to make a good guess at what they
would be called in the real world.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/UNIVERSAL*

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.08-alt2
- rebuilt

* Thu Jul 14 2005 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- initial revision
