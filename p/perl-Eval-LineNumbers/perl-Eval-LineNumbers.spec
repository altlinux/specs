# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.34
%define module_name Eval-LineNumbers
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.34
Release: alt1
Summary: Add line numbers to eval'ed heredoc blocks
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MU/MUIR/modules/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Add a `#line "this-file" 392' comment to heredoc/hereis text that is going.to be eval'ed so that error messages will point back to the right place.

Please note: when you embed `\n' in your code, it gets expanded in
double-quote hereis documents so it will mess up your line numbering.
Use `\\n' instead when you can.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/E*

%changelog
* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- build for Sisyphus

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_8
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_6
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_3
- fc import

