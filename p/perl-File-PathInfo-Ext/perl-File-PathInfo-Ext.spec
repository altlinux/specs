%define module_version 1.30
%define module_name File-PathInfo-Ext
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Digest/MD5.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Copy.pm) perl(File/PathInfo.pm) perl(File/Type.pm) perl(Smart/Comments.pm) perl(Test/Simple.pm) perl(YAML.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.30
Release: alt2
Summary: metadata files, renaming, some other things on top of PathInfo
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LE/LEOCHARRE/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version
# TODO
rm t/0.t t/4_resolve_arg_to.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/F*

%changelog
* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2
- regenerated from template by package builder

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- initial import by package builder

