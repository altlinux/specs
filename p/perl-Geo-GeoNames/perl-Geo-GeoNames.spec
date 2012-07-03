%define module Geo-GeoNames

Name: perl-%module
Version: 0.06
Release: alt2.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Perform geographical queries using GeoNames Web Services
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Geo/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jul 03 2008
BuildRequires: perl-JSON perl-XML-Simple perl-devel perl-libwww

%description
Provides a perl interface to the webservices found at http://ws.geonames.org.
That is, given a placename or postalcode, the module will look it up and
return more information (longitude, lattitude, etc) for the given placename
or postalcode. Wikipedia lookups are also supported. If more than one match
is found, a list of locations will be returned.

%prep
%setup -n %module-%version

%build
# Module tests will not succeed in current Sisyphus build environment.
# (They need access to ws.geonames.org web site)
%define _without_test 1

%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Geo

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Nov 06 2008 Victor Forsyuk <force@altlinux.org> 0.06-alt2
- Fix build failure in current Sisyphus build environment (by disabling
  module tests).

* Thu Jul 03 2008 Victor Forsyuk <force@altlinux.org> 0.06-alt1
- Initial build.
