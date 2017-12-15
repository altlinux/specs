%define module_version 0.004
%define module_name Thread-SigMask
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Module/Build.pm) perl(POSIX.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.004
Release: alt2.1.1.1.1
Summary: Thread specific signal masks
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LE/LEONT/%module_name-%module_version.tar.gz

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
%perl_vendor_archlib/T*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.004-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.004-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.004-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt2.1
- rebuild with new perl 5.20.1

* Fri Jun 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt2
- moved to Sisyphus as dependency

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- initial import by package builder

