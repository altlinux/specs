%define module_name Sphinx-Search
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Class/Accessor/Fast.pm) perl(Config.pm) perl(DBD/mysql.pm) perl(DBI.pm) perl(Data/Dumper.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(Errno.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(File/SearchPath.pm) perl(List/MoreUtils.pm) perl(Math/BigInt.pm) perl(Path/Class.pm) perl(Socket.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-Sphinx-Search
Version: 0.31
Release: alt2

Summary: Sphinx search engine API Perl client
Group: Development/Perl

License: perl
Url: %CPAN %module_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://mirror.yandex.ru/mirrors/cpan/authors/id/J/JJ/JJSCHUTZ/%module_name-%version.tar
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/S*

%changelog
* Sun Nov 18 2018 Vitaly Lipatov <lav@altlinux.ru> 0.31-alt2
- initial build for ALT Sisyphus

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- regenerated from template by package builder

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- initial import by package builder

