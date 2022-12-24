%define _unpackaged_files_terminate_build 1

Name: perl-Code-TidyAll
Version: 0.83
Release: alt1
Summary: Test::Code::TidyAll - Check that all your files are tidy and valid according to tidyall
License: GPL-1.0+  or Artistic-1.0-Perl
Group: Development/Perl
Url: https://metacpan.org/pod/Test::Code::TidyAll
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/Code-TidyAll-%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(lib/relative.pm) perl(Test/Most.pm) perl(Path/Tiny.pm) perl(Test/Class/Most.pm) perl(Capture/Tiny.pm) perl(Digest/SHA.pm) perl(autodie.pm) perl(Specio/Library/Path/Tiny.pm) perl(Moo.pm) perl(Config/INI/Reader.pm) perl(File/Which.pm) perl(IPC/Run3.pm) perl(Date/Format.pm) perl(File/pushd.pm) perl(List/SomeUtils.pm) perl(Time/Duration/Parse.pm) perl(IPC/System/Simple.pm) perl(Encode.pm) perl(Test/Warnings.pm) perl(Pod/Man.pm) perl(Log/Any.pm) perl(Scope/Guard.pm) perl(JSON/MaybeXS.pm) perl(Mason/Tidy/App.pm) perl(Perl/Tidy/Sweetened.pm) perl(Pod/Checker.pm) perl(Pod/Spell.pm) perl(Pod/Tidy.pm) perl(SVN/Look.pm) perl(List/Compare.pm)
BuildRequires: subversion-server-common

%description
Uses Code::TidyAll's check_only mode to check that all the files in your project
are in a tidied and valid state, i.e. that no plugins throw errors or would
change the contents of the file. Does not actually modify any files.
By default, we look for the config file tidyall.ini or .tidyallrc in the current
directory and parent directories, which is generally the right place if you are
running prove.
When invoking Code::TidyAll, we pass mode => 'test' by default; see modes.

%prep
%setup -q -n Code-TidyAll-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTING.md README.md
%_bindir/*
%perl_vendorlib/*
%_man1dir/*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.83-alt1
- automated CPAN update

* Thu May 26 2022 Alexandr Antonov <aas@altlinux.org> 0.82-alt1
- initial build for ALT

