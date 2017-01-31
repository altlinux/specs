# BEGIN SourceDeps(oneline):
BuildRequires: perl(Any/Moose.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/File.pm) perl(Moose.pm) perl(Test/Most.pm) perl(Text/Clip.pm) perl(Try/Tiny.pm)
# END SourceDeps(oneline)
%define module_version 0.0016
%define module_name Term-EditorEdit
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.0016
Release: alt2
Summary: Edit a document via $EDITOR
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/R/RO/ROKR/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/T*

%files scripts
%_bindir/*

%changelog
* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.0016-alt2
- to Sisyphus

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.0016-alt1
- initial import by package builder

