%define m_distro Template-Toolkit-Simple

Name: perl-%m_distro
Version: 0.16
Release: alt1

Summary: Parameterizable packages

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/CPAN/authors/id/I/IN/INGY/Template-Toolkit-Simple-0.16.tar.gz

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Thu Oct 18 2012
BuildRequires: perl-devel perl(Template.pm) perl(YAML/XS.pm)


%description
This module allows you to build packages that return different variations
depending on what parameters are given.

Users of your package will receive a subroutine able to take parameters
and return the name of a suitable variant package. The implmenetation does
not care about what kind of package it builds.

%prep
%setup -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/tt-*
%perl_vendor_privlib/Template*

%changelog
* Thu Oct 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- initial build for ALT Linux Sisyphus

