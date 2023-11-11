%define _unpackaged_files_terminate_build 1
## SPEC file for Perl module Net::IDN::Encode

%define real_name Net-IDN-Encode

Name: perl-Net-IDN-Encode
Version: 2.500
Release: alt2

Summary: Encoding and decoding of Internationalized Domain Names

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Net-IDN-Encode/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

# Make Unicode property generator compatible with perl 5.30-RC1,
# CPAN RT#129588, <https://github.com/cfaerber/Net-IDN-Encode/pull/8>
Patch0: Net-IDN-Encode-2.500-Make-generated-arrays-available-at-compile-time.patch
# Adapt to perl-5.38.0 and stricter GCC, bug #2241714, CPAN RT#149108,
# proposed to an upstream.
Patch1: Net-IDN-Encode-2.500-use_uvchr_to_utf8_flags_instead_of_uvuni_to_utf8_flags.patch

BuildRequires(pre): rpm-build-licenses

Requires: perl-unicore

# Automatically added by buildreq on Sat Jan 21 2017
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Devel-StackTrace perl-Encode perl-ExtUtils-CBuilder perl-IPC-Cmd perl-JSON-PP perl-Locale-Maketext-Simple perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Params-Check perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-devel perl-parent perl-podlators perl-unicore python-base python-modules python3
BuildRequires: perl-HTML-Parser perl-Module-Build perl-Test-NoWarnings perl-Unicode-Normalize perl-Test-Pod perl-Test-Pod-Coverage perl-unicore

%description
Perl module Net::IDN::Encode is a high-level interface for encoding
and decoding of Internationalized Domain Names (implements toASCII
and toUNICODE as defined in RFC 3490)

Net::IDN::Punycode - ASCII-compatible encoding of Unicode
(Punycode, RFC 3492)

%prep
%setup -q -n %real_name-%version
%patch0 -p1
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_autolib/Net
%perl_vendor_archlib/Net

%changelog
* Sat Nov 11 2023 Igor Vlasenko <viy@altlinux.org> 2.500-alt2
- NMU:
- perl 5.38 support (uvuni_to_utf8_flags is removed)
- added patches from Fedora

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.500-alt1
- new version

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.401-alt1.1
- rebuild with new perl 5.28.1

* Sat Sep 22 2018 Nikolay A. Fetisov <naf@altlinux.org> 2.401-alt1
- New version

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.400-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.400-alt1.1
- rebuild with new perl 5.24.1

* Sat Jan 21 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.400-alt1
- New version

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.300-alt1.1
- rebuild with new perl 5.22.0

* Tue Aug 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.300-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.202-alt1
- New version

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.201-alt1.1
- rebuild with new perl 5.20.1

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.201-alt1
- New version

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.200-alt1
- automated CPAN update

* Tue Mar 11 2014 Igor Vlasenko <viy@altlinux.ru> 2.100-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 2.004-alt1
- 2.003 -> 2.004

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.003-alt2
- added dependency on perl-unicore

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 2.003-alt1
- 1.100 -> 2.003
- built for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.100-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.100-alt1.1
- rebuilt with perl 5.12

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.100-alt1
- New version

* Tue Mar 23 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.000-alt1
- Initial build for ALT Linux Sisyphus
