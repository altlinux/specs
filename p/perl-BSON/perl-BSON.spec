%define _unpackaged_files_terminate_build 1
%define module_name BSON
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Carp.pm) perl(Data/Dumper.pm) perl(DateTime.pm) perl(DateTime/Tiny.pm) perl(Digest/MD5.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(JSON/MaybeXS.pm) perl(MIME/Base64.pm) perl(Mango/BSON/Time.pm) perl(Math/BigInt.pm) perl(Module/Runtime.pm) perl(Moo.pm) perl(Path/Tiny.pm) perl(Scalar/Util.pm) perl(Sys/Hostname.pm) perl(Test/Deep.pm) perl(Test/More.pm) perl(Tie/IxHash.pm) perl(Time/HiRes.pm) perl(Time/Local.pm) perl(Time/Moment.pm) perl(base.pm) perl(boolean.pm) perl(constant.pm) perl(if.pm) perl(lib.pm) perl(namespace/clean.pm) perl(overload.pm) perl(re.pm) perl(strict.pm) perl(threads/shared.pm) perl(utf8.pm) perl(version.pm) perl(warnings.pm) perl(Crypt/URandom.pm)
# END SourceDeps(oneline)
#BuildRequires: perl(MongoDB.pm) perl(MongoDB/BSON.pm) perl(MongoDB/BSON/Binary.pm) perl(MongoDB/OID.pm)
BuildRequires: rpm-build-perl perl-devel perl-podlators perl(Test/Fatal.pm)

Name: perl-%module_name
Version: 1.12.2
Release: alt2
Summary: Pure Perl implementation of MongoDB's BSON serialization
Group: Development/Perl
License: apache
URL: https://github.com/mongodb/mongo-perl-bson

Source0: http://www.cpan.org/authors/id/M/MO/MONGODB/%{module_name}-v%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-v%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes corpus/README.md README
%perl_vendor_privlib/B*

%changelog
* Mon Aug 23 2021 Igor Vlasenko <viy@altlinux.org> 1.12.2-alt2
- fixed build

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.12.2-alt1
- automated CPAN update

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1
- automated CPAN update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1
- automated CPAN update

* Thu Dec 13 2018 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1
- automated CPAN update

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1
- automated CPAN update

* Thu Sep 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1
- automated CPAN update

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt1
- automated CPAN update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt1
- automated CPAN update

* Wed Jun 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt1
- automated CPAN update

* Fri Jun 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1
- automated CPAN update

* Mon May 28 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1
- automated CPAN update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1
- automated CPAN update

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1
- automated CPAN update

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1
- automated CPAN update

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2
- removed BR on MongoDB

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2
- to Sisyphus

* Thu Sep 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- regenerated from template by package builder

* Sun Aug 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- regenerated from template by package builder

* Fri Apr 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- initial import by package builder

