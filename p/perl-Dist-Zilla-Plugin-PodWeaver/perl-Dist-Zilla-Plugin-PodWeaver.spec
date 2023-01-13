## SPEC file for Perl module Dist::Zilla::Plugin::PodWeaver

%define real_name Dist-Zilla-Plugin-PodWeaver

Name: perl-Dist-Zilla-Plugin-PodWeaver
Version: 4.010
Release: alt1

Summary: weave Pod together from configuration and Dist::Zilla

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-PodWeaver/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Clone perl-Config-MVP perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-File-Find-Rule perl-IO-String perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-Types perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-String-Flogger perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Text-Glob perl-Throwable perl-Tie-IxHash perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3-base
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla perl-PPI-XS perl-Pod-Elemental-PerlMunger perl-Pod-Weaver

%description
Perl module Dist::Zilla::Plugin::PodWeaver is the bridge between
Dist::Zilla and Pod::Weaver. It rips apart your kinda-Pod and
reconstructs it as boring old real Pod.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/PodWeaver*

%changelog
* Fri Jan 13 2023 Nikolay A. Fetisov <naf@altlinux.org> 4.010-alt1
- New version

* Mon Jun 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 4.009-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 4.008-alt2
- Initial build for ALT Linux Sisyphus
