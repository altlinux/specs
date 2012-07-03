%define dist Params-Classify
Name: perl-%dist
Version: 0.013
Release: alt1

Summary: Argument type classification
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-parent

%description
This module provides various type-testing functions.  These are intended
for functions that, unlike most Perl code, care what type of data they
are operating on.  For example, some functions wish to behave differently
depending on the type of their arguments (like overloaded functions
in C++).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Params
%perl_vendor_autolib/Params

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.013-alt1
- initial revision
