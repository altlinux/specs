%define module WWW-Yandex-TIC
# Disable tests 'cause they rely on Internet access and Yandex site accessibility
%def_without test

Name: perl-%module
Version: 0.07
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: WWW::Yandex::TIC - Query Yandex Thematic Index of Citing (TIC) for domain
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/WWW/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 30 2009
BuildRequires: perl-devel perl-libwww

%description
The WWW::Yandex::TIC is a class implementing a interface for querying Yandex
Thematic Index of Citing (TIC) for domain.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/WWW/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Nov 30 2009 Victor Forsyuk <force@altlinux.org> 0.07-alt1
- 0.07

* Fri Sep 12 2008 Victor Forsyuk <force@altlinux.org> 0.04-alt1
- 0.04

* Wed Aug 06 2008 Victor Forsyuk <force@altlinux.org> 0.03-alt1
- Initial build.
