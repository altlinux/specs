Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

Name: perl-utf8-all
Version: 0.024
Release: alt1

Summary: Turn on Unicode everywhere

License: GPL+ or Artistic
Url: http://search.cpan.org/dist/utf8-all/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source0: http://www.cpan.org/authors/id/H/HA/HAYOBAAN/utf8-all-%{version}.tar.gz

BuildArch: noarch
BuildRequires: su
BuildRequires: findutils
BuildRequires: perl-DBM perl-I18N-Collate perl-I18N-LangTags perl-NEXT perl-POSIX-1003 perl-Term-ReadLine-Gnu perl-Tie-File perl-Tie-RefHash perl-base perl-devel perl-threads perl-unicore
BuildRequires: rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
# Run-time:
BuildRequires: perl(Carp.pm)
BuildRequires: perl(charnames.pm)
BuildRequires: perl(Config.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(feature.pm)
BuildRequires: perl(Import/Into.pm)
BuildRequires: perl(open.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(PerlIO/utf8_strict.pm)
BuildRequires: perl(Symbol.pm)
BuildRequires: perl(utf8.pm)
# Tests:
BuildRequires: perl(autodie.pm)
BuildRequires: perl(constant.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(IPC/Open3.pm)
BuildRequires: perl(locale.pm)
BuildRequires: perl(PerlIO.pm)
BuildRequires: perl(Test/Exception.pm)
BuildRequires: perl(Test/Fatal.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Warn.pm)
BuildRequires: perl(threads.pm)
BuildRequires: perl(threads/shared.pm)
BuildRequires: perl(version.pm)
Source44: import.info

%description
Pragma utf8 allows you to write your Perl encoded in UTF-8. That means UTF-8
strings, variable names, and regular expressions. utf8::all goes further, and
makes @ARGV encoded in UTF-8, and file handles are opened with UTF-8 encoding
turned on by default (including STDIN, STDOUT, STDERR), and character names
are imported so \N{...} sequences can be used to compile Unicode characters
based on names. If you don't want UTF-8 for a particular file handle, you'll
have to set binmode $filehandle.

%prep
%setup -q -n utf8-all-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%buildroot
find %buildroot -type f -name .packlist -delete
# %_fixperms -c %buildroot

%check
make test

%files
%doc LICENSE README
%doc Changes README.mkdn
%perl_vendor_privlib/*

%changelog
* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- automated CPAN update

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.023-alt3
- fixed build with new perl 5.26

* Sun Oct 29 2017 Vitaly Lipatov <lav@altlinux.ru> 0.023-alt2
- initial build for ALT Sisyphus

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1_2
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1_2
- update to new release by fcimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1_1
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1_3
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1_2
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1_3
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1_2
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1_1
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_2
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_2
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_1
- initial fc import

