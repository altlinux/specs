%define module_version 0.06
%define module_name ExtUtils-MakeMaker-CPANfile
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cwd.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Path.pm) perl(File/Spec/Functions.pm) perl(FindBin.pm) perl(Module/CPANfile.pm) perl(Test/More.pm) perl(version.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.06
Release: alt2
Summary: cpanfile support for EUMM
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/I/IS/ISHIGAKI/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
ExtUtils::MakeMaker::CPANfile loads `cpanfile' in your distribution
and modifies parameters for `WriteMakefile' in your Makefile.PL.
Just use it instead of the ExtUtils::MakeMaker manpage (which should be
loaded internally), and prepare `cpanfile'.

As of version 0.03, ExtUtils::MakeMaker::CPANfile also removes
WriteMakefile parameters that the installed version of
ExtUtils::MakeMaker doesn't know, to avoid warnings.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md LICENSE
%perl_vendor_privlib/E*

%changelog
* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- moved to Sisyphis as dependency

* Tue Apr 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- initial import by package builder

