%define module_version 0.007
%define module_name Signal-Mask
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(IPC/Signal.pm) perl(POSIX.pm) perl(Test/More.pm) perl(Thread/SigMask.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.007
Release: alt2
Summary: Signal masks made easy
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LE/LEONT/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/S*

%changelog
* Fri Jun 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.007-alt2
- moved to Sisyphus as dependency

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- initial import by package builder

