## SPEC file for Perl module CGI::Ex

%define real_name CGI-Ex

Name: perl-CGI-Ex
Version: 2.32
Release: alt1

Summary: CGI utility suite

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/CGI-Ex/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Tue Oct 11 2011
# optimized out: perl-JSON-XS perl-YAML perl-common-sense
BuildRequires: perl-CGI perl-JSON perl-Template-Alloy perl-devel

%description
Perl module CGI::Ex provides a suite of utilities to make
writing CGI scripts more enjoyable. Although they can all
be used separately, the main functionality of each of the
modules  is best represented in the  CGI::Ex::App module.
CGI::Ex::App  is not quite a  framework  but an  extended
application flow that dramatically reduces CGI build time
in most cases. It does so using as little magic as
possible.

%package samples
Summary: sample files for CGI::Ex
Group:   Development/Perl
Requires: %name = %{version}-%{release}

%description samples
Perl module CGI::Ex provides a suite of utilities to make
writing CGI scripts more enjoyable.

This package sample application and examples for CGI::Ex.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/CGI/Ex*

%files samples
%doc samples

%changelog
* Tue Oct 11 2011 Nikolay A. Fetisov <naf@altlinux.ru> 2.32-alt1
- Initial build for ALT Linux Sisyphus
