# BEGIN SourceDeps(oneline):
BuildRequires: perl(File/HomeDir.pm) perl(File/chdir.pm) perl(List/MoreUtils.pm) perl(Moose.pm) perl(Moose/Autobox.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Types/Path/Class.pm) perl(Path/Class.pm) perl(Pod/Usage.pm) perl(Test/Differences.pm) perl(Test/Exception.pm) perl(YAML/Tiny.pm)
# END SourceDeps(oneline)
%define module_version 0.003
%define module_name File-Corresponding
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators perl(Module/Build.pm)

Name: perl-%module_name
Version: %module_version
Release: alt2
Summary: File::Corresponding - Find corresponding files in the directory tree
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/A/AN/ANDY/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
In a source tree it is common to have files with the same name, but in
different places in the directory tree.

%prep
%setup -n %module_name-%module_version
rm  t/corresponding-group-corresponding.t t/corresponding-corresponding.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/F*
%exclude %_bindir/*

%changelog
* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- initial import by package builder

