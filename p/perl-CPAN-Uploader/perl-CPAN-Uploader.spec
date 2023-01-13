## SPEC file for Perl module CPAN-Uploader

Name: perl-CPAN-Uploader
Version: 0.103017
Release: alt1

Summary: Perl module to upload things to the CPAN

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/CPAN-Uploader/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name CPAN-Uploader
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sat Nov 06 2021
# optimized out: libgpg-error perl perl-CPAN-Meta-Requirements perl-Encode perl-HTTP-Date perl-HTTP-Message perl-JSON-PP perl-Parse-CPAN-Meta perl-Pod-Escapes perl-Pod-Simple perl-Try-Tiny perl-URI perl-libwww perl-parent perl-podlators python3-base sh4
BuildRequires: perl-CPAN-Meta perl-Clone perl-Getopt-Long-Descriptive perl-LWP-Protocol-https perl-TermReadKey perl-devel

BuildRequires: perl-podlators

%description
Perl module CPAN::Uploader upload things to the CPAN.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/CPAN/Uploader*

%_bindir/cpan-upload
%_man1dir/cpan-upload*

%changelog
* Fri Jan 13 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.103017-alt1
- New version

* Sat Nov 06 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.103016-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.103015-alt1
- New version

* Sun Jun 28 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.103014-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.103013-alt1
- New version

* Tue Jan 05 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.103012-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.103011-alt1
- New version

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.103010-alt1
- New version

* Fri Jun 12 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.103009-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.103007-alt1
- New version

* Thu Feb 27 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.103006-alt1
- New version

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.103004-alt1
- New version

* Mon Jan 07 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.103002-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.103001-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.103000-alt1
- Initial build for ALT Linux Sisyphus

