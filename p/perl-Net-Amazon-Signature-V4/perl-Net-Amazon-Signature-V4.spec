%define module_name Net-Amazon-Signature-V4
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Digest/SHA.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Slurper.pm) perl(HTTP/Request.pm) perl(Test/More.pm) perl(Time/Piece.pm) perl(URI/Escape.pm) perl(sort.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.21
Release: alt2
Summary: Implements the Amazon Web Services signature version 4, AWS4-HMAC-SHA256
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/D/DB/DBOOK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/N*

%changelog
* Mon Aug 01 2022 Igor Vlasenko <viy@altlinux.org> 0.21-alt2
- to Sisyphus as perl-Amazon-S3 dep

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- updated by package builder

* Thu Feb 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- updated by package builder

* Sat Aug 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- regenerated from template by package builder

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- regenerated from template by package builder

* Mon May 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- initial import by package builder

