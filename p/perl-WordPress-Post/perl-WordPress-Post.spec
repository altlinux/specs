%define module_version 1.07
%define module_name WordPress-Post
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cwd.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Type.pm) perl(Image/Magick.pm) perl(LEOCHARRE/CLI.pm) perl(MIME/Base64.pm) perl(Test/Simple.pm) perl(XMLRPC/Lite.pm) perl(YAML.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.07
Release: alt2
Summary: DEPRECATED see WordPress::CLI instead
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LE/LEOCHARRE/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/W*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.07-alt2
- regenerated from template by package builder

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- initial import by package builder

