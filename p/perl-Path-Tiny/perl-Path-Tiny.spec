%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Cwd.pm) perl(Digest.pm) perl(Digest/SHA.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(File/Copy.pm) perl(File/Path.pm) perl(File/Spec/Functions.pm) perl(File/Spec/Unix.pm) perl(File/Temp.pm) perl(File/stat.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(List/Util.pm) perl(Test/More.pm) perl(autodie/exception.pm) perl(open.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 0.047
%define module_name Path-Tiny
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.047
Release: alt1
Summary: File path utility
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/Path-Tiny

Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Path-Tiny-%{version}.tar.gz
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
%perl_vendor_privlib/P*

%changelog
* Thu Nov 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.047-alt1
- automated CPAN update

* Mon Nov 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.046-alt1
- automated CPAN update

* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1
- automated CPAN update

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.043-alt1
- automated CPAN update

* Sat Oct 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.041-alt1
- automated CPAN update

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1
- automated CPAN update

* Wed Oct 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.038-alt1
- automated CPAN update

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.037-alt1
- automated CPAN update

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.033-alt1
- regenerated from template by package builder

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- initial import by package builder

