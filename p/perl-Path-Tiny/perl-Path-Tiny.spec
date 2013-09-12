# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Cwd.pm) perl(Digest.pm) perl(Digest/SHA.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(File/Copy.pm) perl(File/Path.pm) perl(File/Spec/Functions.pm) perl(File/Spec/Unix.pm) perl(File/Temp.pm) perl(File/stat.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(List/Util.pm) perl(Test/More.pm) perl(autodie/exception.pm) perl(open.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 0.032
%define module_name Path-Tiny
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.032
Release: alt1
Summary: File path utility
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/Path-Tiny

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
%doc LICENSE README Changes
%perl_vendor_privlib/P*

%changelog
* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- initial import by package builder

