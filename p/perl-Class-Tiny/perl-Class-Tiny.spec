# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec/Functions.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(List/Util.pm) perl(Test/More.pm) perl(base.pm) perl(subs.pm)
# END SourceDeps(oneline)
%define module_version 0.008
%define module_name Class-Tiny
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.008
Release: alt1
Summary: Minimalist class construction
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/Class-Tiny

Source0: http://cpan.org.ua/authors/id/D/DA/DAGOLDEN/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/C*

%changelog
* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- initial import by package builder

