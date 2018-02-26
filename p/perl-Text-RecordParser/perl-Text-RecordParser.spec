%define dist Text-RecordParser

Name: perl-%dist
Version: 1.5.0
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Text::RecordParser - read record-oriented files
License: GPLv2 only
Group: Development/Perl

URL: %CPAN %dist
Source: http://search.cpan.org/CPAN/authors/id/K/KC/KCLARK/Text-RecordParser-v%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Oct 11 2010
BuildRequires: fonts-type1-urw perl-Class-Accessor perl-GraphViz perl-IO-stringy perl-List-MoreUtils perl-Module-Build perl-Readonly perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage perl-Text-TabularDisplay

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators
BuildRequires: perl-Readonly-XS

%description
This module is for reading record-oriented data. The most common example have
records separated by newlines and fields separated by commas or tabs, but this
module aims to provide a consistent interface for handling sequential records in
a file however they may be delimited. 

%prep
%setup -n %dist-v%version

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/*
%perl_vendor_privlib/Text
%_man1dir/*

%changelog
* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 11 2010 Victor Forsiuk <force@altlinux.org> 1.5.0-alt1
- 1.5.0

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Nov 30 2009 Victor Forsyuk <force@altlinux.org> 1.3.0-alt1
- 1.3.0

* Thu May 22 2008 Victor Forsyuk <force@altlinux.org> 1.2.1-alt2
- Rebuild to fix #15541.

* Wed Jul 11 2007 Victor Forsyuk <force@altlinux.org> 1.2.1-alt1
- 1.2.1

* Thu Aug 25 2005 Alexey Morozov <morozov@altlinux.org> 0.09-alt1
- Initial build for ALT Linux
