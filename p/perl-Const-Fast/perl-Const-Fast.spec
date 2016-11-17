# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Data/Dumper.pm) perl(File/Find.pm) perl(File/Temp.pm) perl(Module/Build/Tiny.pm) perl(Scalar/Util.pm) perl(Storable.pm) perl(Sub/Exporter/Progressive.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_version 0.014
%define module_name Const-Fast
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.014
Release: alt2
Summary: Facility for creating read-only scalars, arrays, and hashes
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LE/LEONT/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
use Const::Fast;

 const my $foo => 'a scalar value';
 const my @bar => qw/a list value/;
 const my %%buz => (a => 'hash', of => 'something');


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_privlib/C*

%changelog
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2
- to Sisyphus

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- update

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_2
- update to new release by fcimport

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1_4
- fc import

