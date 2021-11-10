Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-podlators
# END SourceDeps(oneline)
%define real_name Crypt-CipherSaber
Name:           perl-Crypt-CipherSaber
Version:        1.01
Release:        alt3
Summary:        Perl module implementing CipherSaber encryption
License:        %perl_license
URL:            https://metacpan.org/release/%real_name
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/%real_name-%version.tar
# Fix parsing encrypted file, bug #1104075, CPAN RT#28370
Patch0:         Crypt-CipherSaber-1.01-Fix-reading-IV-with-new-lines-from-a-file.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-devel
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(vars.pm)
# Tests:
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Warn.pm)

# Filter under-specified dependencies
%filter_from_requires /^perl(Scalar.Util.pm)/d

%description
The Crypt::CipherSaber module implements CipherSaber encryption, described
at http://ciphersaber.gurus.com/. It is simple, fairly speedy, and
relatively secure algorithm based on RC4.

%prep
%setup -q -n %real_name-%version
%patch0 -p1
rm *.list ||:

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/*

%changelog
* Wed Nov 10 2021 L.A. Kostis <lakostis@altlinux.ru> 1.01-alt3
- Rebuild by human.

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 1.01-alt2_18
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 1.01-alt2_17
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 1.01-alt2_16
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_15
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_15
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_14
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_13
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_12
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_11
- update to new release by fcimport

* Thu Mar 14 2019 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_10
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_12
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_11
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_10
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_8
- fc import

