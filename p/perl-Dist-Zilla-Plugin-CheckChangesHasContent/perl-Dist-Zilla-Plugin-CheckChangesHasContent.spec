## SPEC file for Perl module Dist::Zilla::Plugin::CheckChangesHasContent

%define real_name Dist-Zilla-Plugin-CheckChangesHasContent

Name: perl-Dist-Zilla-Plugin-CheckChangesHasContent
Version: 0.011
Release: alt1

Summary: Dist::Zilla plugin to ensure Changes has content before releasing

License: %asl 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-CheckChangesHasContent/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jan 23 2017
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Capture-Tiny perl-Data-Section perl-Encode perl-File-pushd perl-Moose perl-Parse-CPAN-Meta perl-Path-Tiny perl-Sub-Exporter-ForMethods perl-Try-Tiny perl-autodie perl-devel perl-namespace-autoclean python-base python-modules python3-base
BuildRequires: perl-Dist-Zilla

%description
Perl module Dist::Zilla::Plugin::Test::ChangesHasContent is a
"before release" Dist::Zilla plugin that ensures that your
Changes file actually has some content since the last release.
If it doesn't find any, it will abort the release process.

%prep
%setup -q -n %real_name-%version

rm -f -- t/checkhascontent.t
rm -f -- t/test_changeshascontent.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/*

%changelog
* Sat Dec 09 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.011-alt1
- New version

* Mon Jan 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.010-alt2
- Initial build for ALT Linux Sisyphus
