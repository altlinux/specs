## SPEC file for Perl module Compiler::Lexer

%define real_name Compiler-Lexer

Name: perl-Compiler-Lexer
Version: 0.22
Release: alt2.1.1

Summary: Lexical Analyzer for Perl5

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Compiler-Lexer/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jun 27 2016
# optimized out: libstdc++-devel perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-CBuilder perl-IPC-Cmd perl-JSON-PP perl-Locale-Maketext-Simple perl-Module-Build perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Params-Check perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-devel perl-parent perl-podlators python-base python-modules python3
BuildRequires: gcc-c++ perl-HTML-Parser perl-Module-Build-XSUtil perl-PerlIO-utf8_strict

%description
Perl module Compiler::Lexer is a Lexical Analyzer for Perl5.

%prep
%setup
#%%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_archlib/Compiler/Lexer*
%perl_vendor_autolib/Compiler/Lexer*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2.1
- rebuild with new perl 5.24.1

* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.22-alt2
- Initial build for ALT Linux Sisyphus
