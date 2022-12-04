%define _unpackaged_files_terminate_build 1
## SPEC file for Perl module CGI::Ex

%define real_name CGI-Ex

Name: perl-CGI-Ex
Version: 2.54
Release: alt1

Summary: CGI utility suite

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/CGI-Ex/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sun Aug 09 2020
# optimized out: perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON perl-JSON-PP perl-JSON-XS perl-Parse-CPAN-Meta perl-Types-Serialiser perl-XML-Simple perl-common-sense perl-devel perl-parent python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: perl-CGI perl-CPAN-Meta perl-Config-IniHash perl-Template-Alloy perl-YAML

%description
Perl module CGI::Ex provides a suite of utilities to make
writing CGI scripts more enjoyable. Although they can all
be used separately, the main functionality of each of the
modules  is best represented in the  CGI::Ex::App module.
CGI::Ex::App  is not quite a  framework  but an  extended
application flow that dramatically reduces CGI build time
in most cases. It does so using as little magic as
possible.

%package samples
Summary: sample files for CGI::Ex
Group:   Development/Perl
Requires: %name = %{version}-%{release}

%description samples
Perl module CGI::Ex provides a suite of utilities to make
writing CGI scripts more enjoyable.

This package sample application and examples for CGI::Ex.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes README
%perl_vendor_privlib/CGI/Ex*

%files samples
%doc samples

%changelog
* Sat Dec 03 2022 Nikolay A. Fetisov <naf@altlinux.org> 2.54-alt1
- New version

* Sun Aug 09 2020 Nikolay A. Fetisov <naf@altlinux.org> 2.50-alt1
- New version

* Tue Mar 31 2020 Nikolay A. Fetisov <naf@altlinux.org> 2.49-alt1
- New version

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.48-alt1
- new version

* Sat Aug 18 2018 Nikolay A. Fetisov <naf@altlinux.org> 2.47-alt1
- New version

* Sun Aug 05 2018 Nikolay A. Fetisov <naf@altlinux.org> 2.46-alt1
- New version

* Sun Jul 30 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.45-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.44-alt1
- New version

* Sun Oct 04 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.43-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.42-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.38-alt1
- New version

* Tue Oct 11 2011 Nikolay A. Fetisov <naf@altlinux.ru> 2.32-alt1
- Initial build for ALT Linux Sisyphus
