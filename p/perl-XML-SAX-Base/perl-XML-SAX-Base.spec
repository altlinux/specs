%define dist XML-SAX-Base
Name: perl-%dist
Version: 1.08
Release: alt1

Summary: Base class for SAX Drivers and Filters
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# released separately from XML-SAX distribution
Conflicts: perl-XML-SAX < 0.99

# Automatically added by buildreq on Thu Oct 06 2011
BuildRequires: perl-devel

%description
This module is the base class for all SAX Exceptions, those defined in
the spec as well as those that one may create for one's own SAX errors.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# This file is used to generate lib/XML/SAX/Base.pm.
rm %buildroot%perl_vendor_privlib/XML/SAX/BuildSAXBase.pl

%files
%doc Changes README
%perl_vendor_privlib/XML

%changelog
* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 1.08-alt1
- initial revision
