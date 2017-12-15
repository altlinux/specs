# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/CBuilder.pm) perl(ExtUtils/CChecker.pm) perl(ExtUtils/PkgConfig.pm) perl(IO/Handle.pm) perl(IO/Poll.pm) perl(Module/Build.pm) perl(Module/Build/Compat.pm) perl(Socket.pm) perl(Test/Identity.pm) perl(Test/More.pm) perl(Test/Refcount.pm) perl(XSLoader.pm) pkgconfig(libasyncns)
# END SourceDeps(oneline)
%define module_version 0.02
%define module_name Net-LibAsyncNS
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.02
Release: alt1.1.1.1.1
Summary: a Perl wrapper around F<libasyncns>
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/P/PE/PEVANS/Net-LibAsyncNS-%{version}.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README Changes examples
%perl_vendor_archlib/N*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- rebuild with new perl 5.20.1

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- automated CPAN update

* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- build for Sisyphus (required for perl update)

