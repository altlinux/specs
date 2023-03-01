%define _unpackaged_files_terminate_build 1
## SPEC file for Perl module Test::PerlTidy

%define real_name Test-PerlTidy

Name: perl-Test-PerlTidy
Version: 20230226
Release: alt1

Summary: Perl module to check that all project files are tidy

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-PerlTidy/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu Apr 18 2019
# optimized out: gem-power-assert perl perl-Algorithm-Diff perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-HTML-Parser perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Path-Tiny perl-Perl-OSType perl-Perl-Tidy perl-Pod-Escapes perl-Pod-Simple perl-devel perl-parent perl-podlators python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: perl-Module-Build perl-PerlIO-utf8_strict perl-Test-Perl-Critic perl-Text-Diff perl(Path/Tiny.pm)

%description
Perl module Test::PerlTidy provides a check during the tests that
that all the perl files included with the distribution are tidy.
If you make any changes please remember to tidy them.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test/PerlTidy*

%changelog
* Wed Mar 01 2023 Igor Vlasenko <viy@altlinux.org> 20230226-alt1
- new version

* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 20220902-alt2
- fixed build - added BR: perl(Path/Tiny.pm)

* Wed Sep 21 2022 Igor Vlasenko <viy@altlinux.org> 20220902-alt1
- new version

* Sun Jul 11 2021 Nikolay A. Fetisov <naf@altlinux.org> 20210709-alt1
- New version

* Tue Nov 17 2020 Nikolay A. Fetisov <naf@altlinux.org> 20200930-alt1
- New version

* Tue May 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 20200412-alt1
- New version

* Thu Apr 18 2019 Nikolay A. Fetisov <naf@altlinux.org> 20190402-alt1
- New version (Closes: #36225)

* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 20130104-alt2
- Initial build for ALT Linux Sisyphus
