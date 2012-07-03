%define module XML-Writer-String

Name: perl-%module
Version: 0.1
Release: alt1.1

Summary: Capture output from XML::Writer
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/S/SO/SOLIVER/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed May 19 2010
BuildRequires: perl-XML-Writer perl-devel

%description
This module implements a bare-bones class specifically for the purpose of
capturing data from the XML::Writer module.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/XML

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed May 19 2010 Victor Forsyuk <force@altlinux.org> 0.1-alt1
- Initial build.
