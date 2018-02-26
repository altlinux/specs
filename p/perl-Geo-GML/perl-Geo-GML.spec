%define dist Geo-GML
Name: perl-%dist
Version: 0.15
Release: alt1

Summary: Process Geography Markup Language
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-Geo-Point perl-Test-Pod perl-XML-Compile-Cache perl-XML-Compile-Tester

%description
Provides access to the GML definitions specified in XML. The details
about GML structures can differ, and therefore you should be explicit
which versions you understand and produce.
If you need the <b>most recent</b> version of GML, then you get involved
with the ISO19139 standard. See CPAN module Geo::ISO19139.
The first releases of this module will not powerful, but hopefully people
contribute. For instance, an example conversion script between various
versions is very welcome! It would be nice to help each other. I will
clean-up the implementation, to make it publishable, but do not have
the knowledge about what is needed.

%prep
%setup -q -n %dist-%version

# disable Geo::Point tests which fail
rm t/40gpgml3.t
rm t/41gpgml2.t

# furthermore, disable dependency on Geo::Point
%add_findreq_skiplist */Geo/GML/GeoPoint*

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Geo

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- 0.11 -> 0.15
- disabled dependency on Geo::Point for now

* Sun Jan 11 2009 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt1
- initial build for ALT Linux Sisyphus
