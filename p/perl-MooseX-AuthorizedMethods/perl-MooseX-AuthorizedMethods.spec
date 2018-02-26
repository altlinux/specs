%define dist MooseX-AuthorizedMethods
Name: perl-%dist
Version: 0.006
Release: alt1

Summary: Syntax sugar for authorized methods
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Moose perl-Pod-Escapes perl-aliased perl-devel

%description
This method exports the "authorized" declarator that makes a
verification if the user has the required permissions before the acual
invocation. The default verification method will take the "user"
method result and call "roles" to list the roles given to that user.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/MooseX

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.006-alt1
- initial revision
