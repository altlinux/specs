%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Cwd.pm) perl(Digest.pm) perl(Digest/SHA.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(File/Copy.pm) perl(File/Path.pm) perl(File/Spec/Functions.pm) perl(File/Spec/Unix.pm) perl(File/Temp.pm) perl(File/stat.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(List/Util.pm) perl(Test/More.pm) perl(autodie/exception.pm) perl(open.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_name Path-Tiny
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.144
Release: alt1.1
Summary: File path utility
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/Path-Tiny

Source0: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/P*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.144-alt1.1
- automated CPAN update

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 0.144-alt1
- automated CPAN update

* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 0.142-alt1
- automated CPAN update

* Sat Oct 22 2022 Igor Vlasenko <viy@altlinux.org> 0.130-alt1
- automated CPAN update

* Sat Sep 03 2022 Igor Vlasenko <viy@altlinux.org> 0.124-alt1
- automated CPAN update

* Wed Jan 19 2022 Igor Vlasenko <viy@altlinux.org> 0.122-alt1
- automated CPAN update

* Tue Oct 26 2021 Igor Vlasenko <viy@altlinux.org> 0.120-alt1
- automated CPAN update

* Wed Feb 10 2021 Igor Vlasenko <viy@altlinux.ru> 0.118-alt1
- automated CPAN update

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 0.116-alt1
- automated CPAN update

* Mon Apr 27 2020 Igor Vlasenko <viy@altlinux.ru> 0.114-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.112-alt1
- automated CPAN update

* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.110-alt1
- automated CPAN update

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.108-alt1
- automated CPAN update

* Fri Jul 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.106-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.104-alt1
- automated CPAN update

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.100-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.098-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.096-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.094-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.090-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.088-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.086-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.084-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.082-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.076-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.072-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.068-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.061-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.060-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.059-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.058-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.056-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.055-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.054-alt1
- automated CPAN update

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.052-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.051-alt1
- automated CPAN update

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

