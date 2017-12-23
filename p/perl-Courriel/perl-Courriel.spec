## SPEC file for Perl module Courriel

%define real_name Courriel

Name: perl-Courriel
Version: 0.45
Release: alt1

Summary: Perl module for high level email parsing and manipulation

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Courriel/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Due to Moose internal errors
%add_findreq_skiplist */Courriel/HeaderAttribute.pm

# Automatically added by buildreq on Sat Jan 21 2017
# optimized out: perl perl-Algorithm-Diff perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Method-Modifiers perl-Class-Singleton perl-Class-Tiny perl-Clone perl-Data-OptList perl-Date-Calc-XS perl-DateTime perl-DateTime-Format-Mail perl-DateTime-Format-Natural perl-DateTime-Locale perl-DateTime-TimeZone perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-PartialDump perl-Devel-StackTrace perl-Email-Abstract perl-Email-Address perl-Email-Address-List perl-Email-MIME-Encodings perl-Email-MessageID perl-Email-Simple perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-LibMagic perl-File-Slurp-Tiny perl-List-AllUtils perl-List-MoreUtils perl-List-SomeUtils perl-List-UtilsBy perl-MIME-tools perl-MRO-Compat perl-MailTools perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-MooX-Types-MooseLike perl-Moose perl-MooseX-Role-Parameterized perl-MooseX-StrictConstructor perl-MooseX-Types perl-MooseX-Types-Common perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Role-Tiny perl-Specio perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Fatal perl-Text-Diff perl-Throwable perl-TimeDate perl-Try-Tiny perl-Variable-Magic perl-boolean perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3-base
BuildRequires: perl-CPAN-Meta perl-Class-XSAccessor perl-Date-Calc perl-DateTime-Format-Mail perl-DateTime-Format-Natural perl-Email-Address-List perl-Email-Sender perl-File-LibMagic perl-File-Slurp-Tiny perl-List-AllUtils perl-MooseX-Role-Parameterized perl-MooseX-StrictConstructor perl-MooseX-Types-Common perl-Path-Class perl-Test-Differences perl-Test-Requires perl-Params-ValidationCompiler perl-Devel-PartialDump

%description
Perl module Courriel provides a high level API for email parsing
and manipulation, particular for processing incoming email.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/Courriel*
%perl_vendor_privlib/Email*

%changelog
* Sat Dec 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.45-alt1
- New version

* Sat Jan 21 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.44-alt1
- New version

* Sun Aug 14 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.42-alt2
- Fix BuildRequires

* Thu Jul 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.42-alt1
- New version

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.41-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.40-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.39-alt1
- New version

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.36-alt1
- Initial build for ALT Linux Sisyphus
