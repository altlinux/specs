## SPEC file for Perl module Dist::Zilla::PluginBundle::RJBS

%define real_name Dist-Zilla-PluginBundle-RJBS

Name: perl-Dist-Zilla-PluginBundle-RJBS
Version: 5.036
Release: alt1

Summary: BeLike::RJBS when you build your dists

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-PluginBundle-RJBS/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Mar 10 2026
# optimized out: libgpg-error perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Data-Section perl-Digest-SHA perl-Dist-Zilla perl-Encode perl-JSON-PP perl-Moose perl-Parse-CPAN-Meta perl-Path-Tiny perl-Pod-Elemental perl-Pod-Elemental-PerlMunger perl-Pod-Weaver perl-Sub-Exporter-ForMethods perl-devel perl-parent python3 python3-base sh5
BuildRequires: perl-Dist-Zilla-Config-Slicer perl-Dist-Zilla-Plugin-CheckChangesHasContent perl-Dist-Zilla-Plugin-CheckExtraTests perl-Dist-Zilla-Plugin-CheckPrereqsIndexed perl-Dist-Zilla-Plugin-Git perl-Dist-Zilla-Plugin-Git-Contributors perl-Dist-Zilla-Plugin-Git-Remote-Check perl-Dist-Zilla-Plugin-GithubMeta perl-Dist-Zilla-Plugin-PodWeaver perl-Dist-Zilla-Plugin-PromptIfStale perl-Dist-Zilla-Plugin-TaskWeaver perl-Dist-Zilla-Plugin-Test-Compile perl-Dist-Zilla-Plugin-Test-ReportPrereqs perl-Dist-Zilla-Role-PluginBundle-PluginRemover perl-Pod-Elemental-Transformer-List perl-Pod-Weaver-Section-Contributors

%description
Perl module Dist::Zilla::PluginBundle::RJBS is a Dist::Zilla plugin
to bundle settings that RJBS uses.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/PluginBundle/RJBS*
%exclude %perl_vendor_privlib/Dist/Zilla/App/Command/*
%perl_vendor_privlib/Pod*

%changelog
* Tue Mar 10 2026 Nikolay A. Fetisov <naf@altlinux.org> 5.036-alt1
- New version

* Mon Feb 09 2026 Nikolay A. Fetisov <naf@altlinux.org> 5.035-alt1
- New version

* Tue Nov 04 2025 Nikolay A. Fetisov <naf@altlinux.org> 5.033-alt1
- New version

* Wed May 29 2024 Nikolay A. Fetisov <naf@altlinux.org> 5.029-alt1
- New version

* Sun Nov 26 2023 Nikolay A. Fetisov <naf@altlinux.org> 5.025-alt1
- New version

* Wed Jul 26 2023 Nikolay A. Fetisov <naf@altlinux.org> 5.024-alt1
- New version

* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 5.022-alt1
- New version

* Sun Jul 11 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.020-alt1
- New version

* Sat Jul 03 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.019-alt1
- New version

* Mon Jun 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.018-alt1
- New version

* Tue Jun 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.017-alt1
- New version

* Sat May 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.015-alt1
- New version

* Thu Mar 18 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.013-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.012-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 5.010-alt2
- Initial build for ALT Linux Sisyphus
