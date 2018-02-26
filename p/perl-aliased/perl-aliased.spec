%define dist aliased
Name: perl-%dist
Version: 0.30
Release: alt1

Summary: Use shorter versions of class names
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
"aliased" is simple in concept but is a rather handy module.  It loads
the class you specify and exports into your namespace a subroutine that
returns the class name.  You can explicitly alias the class to another
name or, if you prefer, you can do so implicitly.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/aliased*

%changelog
* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.30-alt1
- initial revision, for MooseX::Role::WithOverloading
