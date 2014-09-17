## SPEC file for Perl module Encode-Escape

%define real_name  Encode-Escape

Name: perl-Encode-Escape
Version: 0.14
Release: alt2

Summary: Perl extension for Encodings of various escape sequences

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Encode-Escape/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar
Patch0: perl-Encode-Escape-0.14-alt-export_to_level.patch
Patch1: perl-Encode-Escape-0.14-alt-global_var.patch

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Wed Sep 17 2014
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-JSON-PP perl-Module-Metadata perl-Module-Runtime perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-devel perl-podlators
BuildRequires: perl-HTML-Parser perl-Import-Into perl-Module-Build

%description
Encode::Escape  Perl module is  a wrapper class  for encodings
of escape sequences in strings.  It is NOT for an escape-based
encoding (eg. ISO-2022-JP). It is for encoding/decoding escape
sequences, generally used in source codes.

%prep
%setup  -n %real_name-%version
%patch0
%patch1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Encode/Escape*

%changelog
* Wed Sep 17 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.14-alt2
- Fix build 5.18

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Dec 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.14-alt1
- Initial build for ALT Linux Sisyphus
