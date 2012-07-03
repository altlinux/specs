%define module Text-Trac

Name: perl-%module
Version: 0.15
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Perl extension for formatting text with Trac Wiki Style
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Text/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 30 2009
BuildRequires: perl-Class-Accessor perl-Class-Data-Inheritable perl-HTML-Parser perl-List-MoreUtils perl-Test-Base perl-Test-Pod perl-Test-Pod-Coverage perl-Tie-IxHash perl-UNIVERSAL-require

%description
Text::Trac parses text with Trac WikiFormatting and convert it to html format.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Text/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Nov 30 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- 0.15

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 0.12-alt1
- 0.12

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 0.11-alt1
- 0.11

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.10-alt1
- Initial build.
