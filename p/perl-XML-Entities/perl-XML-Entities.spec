%define module_dir XML
%define real_name  %module_dir-Entities


Name: perl-XML-Entities
Version: 1.0000
Release: alt1

Packager: Pavel Zilke <zidex at altlinux dot org>

Summary: XML::Entities - Decode strings with XML entities
License: Perl style license
Group: Development/Perl
URL: http://cpan.org/modules/by-module/%module_dir

BuildArch: noarch
Source0: %url/%real_name-%version.tar.gz

AutoReqProv: perl, yes

# Automatically added by buildreq on Thu Nov 26 2009
BuildRequires: libnss-mdns perl-devel perl-libwww
BuildRequires: perl-Tie-RefHash
BuildRequires: perl-autodie
BuildRequires: perl-Module-Build

%description
Based upon the HTML::Entities module by Gisle Aas
This module deals with decoding of strings with XML character entities.
The module provides two functions:
decode( $entity_set, $string, ... )
numify( $entity_set, $string, ... )
    
%prep
%setup -n %real_name

%build
%__rm -rf LibXML
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/%module_dir/*

%changelog
* Tue Jul 05 2011 Pavel Zilke <zidex at altlinux dot org> 1.0000-alt1
- New version

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.0307-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Nov 26 2009 Pavel Zilke <zidex at altlinux dot org> 0.0307-alt1
- Initial build for ALTLinux

