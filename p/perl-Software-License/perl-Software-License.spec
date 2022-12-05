## SPEC file for Perl module Software::License
%define _unpackaged_files_terminate_build 1
%define real_name Software-License

Name: perl-Software-License
Version: 0.104002
Release: alt1

Summary: Perl module that provide templated software licenses

License: %perl_license
Group: Development/Perl
URL: https://metacpan.org/dist/Software-License/

Packager: Nikolay A. Fetisov <naf@altlinux.org>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Sep 14 2014
# optimized out: perl-Data-OptList perl-MRO-Compat perl-Params-Util perl-Sub-Exporter perl-Sub-Install
BuildRequires: perl-Data-Section perl-Module-Load perl-Sub-Name perl-Text-Template perl-Try-Tiny perl-devel perl-parent

%description
Perl module Software::License provides templated software licenses.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Software/License*

%changelog
* Mon Dec 05 2022 Nikolay A. Fetisov <naf@altlinux.org> 0.104002-alt1
- New version

* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.104001-alt1
- New version
- Update URL

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.103014-alt1
- new version

* Sun Nov 12 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.103013-alt1
- New version

* Sat May 28 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.103012-alt1
- New version

* Sat Jan 23 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.103011-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.103010-alt1
- New version

* Thu Feb 27 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.103009-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.103008-alt1
- New version

* Mon Jan 07 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.103005-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.103004-alt1
- Initial build for ALT Linux Sisyphus

