Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl(CGI.pm) perl(CGI/Carp.pm) perl-podlators
# END SourceDeps(oneline)
%define fontpkgname perl-MIME-Lite-HTML
Name:           perl-MIME-Lite-HTML
Version:        1.24
Release:        alt3
Summary:        Provide routine to transform a HTML page in a MIME-Lite mail
License:        %perl_license
URL:            https://metacpan.org/release/MIME-Lite-HTML
Source0:        https://cpan.metacpan.org/modules/by-module/MIME/MIME-Lite-HTML-%{version}.tar
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-core glibc-timezones glibc-utils iconv
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(HTML/LinkExtor.pm)
BuildRequires:  perl(LWP/UserAgent.pm)
BuildRequires:  perl(MIME/Lite.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(URI/URL.pm)
BuildRequires:  perl(vars.pm)
# Tests:
BuildRequires:  perl(Test.pm)

%description
This module is a Perl mail client interface for sending message that
support HTML format and build them for you.. This module provides routine to
transform an HTML page in a MIME::Lite mail. So you need this module to use
MIME-Lite-HTML possibilities.


%prep
%setup -q -n MIME-Lite-HTML-%{version}
chmod a-x README Changes HTML.pm
iconv -f iso8859-1 -t utf-8 Changes > Changes.utf8 && \
touch -r Changes Changes.utf8 && \
mv -f Changes.utf8 Changes
# The 2 following tests are broken by MIME::Lite 3.029
# Headers order is not quaranteed so relying on that to test the module is
# doomed to fail.
# Relevant bugs :
# MIME::Lite::HTML : http://rt.cpan.org/Public/Bug/Display.html?id=86020
# MIME::Lite : https://rt.cpan.org/Public/Bug/Display.html?id=79944
rm -f t/20create_image_part.t t/50generic.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes COPYING README
%perl_vendor_privlib/*


%changelog
* Wed Nov 10 2021 L.A. Kostis <lakostis@altlinux.ru> 1.24-alt3
- Rebuild by human.

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 1.24-alt2_30
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 1.24-alt2_29
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 1.24-alt2_28
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 1.24-alt2_27
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_27
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_26
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_25
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_24
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_23
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_22
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_21
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_20
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_19
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_18
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_17
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_16
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_15
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_14
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_13
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_12
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_9
- update to new release by fcimport

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_8
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_4
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_2
- fc import

