# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/CBuilder.pm) perl(ExtUtils/CChecker.pm) perl(ExtUtils/PkgConfig.pm) perl(IO/Handle.pm) perl(IO/Poll.pm) perl(Module/Build.pm) perl(Module/Build/Compat.pm) perl(Socket.pm) perl(Test/Identity.pm) perl(Test/More.pm) perl(Test/Refcount.pm) perl(XSLoader.pm) pkgconfig(libasyncns)
# END SourceDeps(oneline)
%define module_version 0.01
%define module_name Net-LibAsyncNS
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.01
Release: alt1
Summary: a Perl wrapper around F<libasyncns>
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/P/PE/PEVANS/%module_name-%module_version.tar.gz

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
* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- build for Sisyphus (required for perl update)

