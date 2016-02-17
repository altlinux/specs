# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Array/RefElem.pm) perl(Carp.pm) perl(Data/Dumper.pm) perl(Devel/Peek.pm) perl(English.pm) perl(Exporter.pm) perl(Fatal.pm) perl(File/Spec.pm) perl(HTML/LinkExtor.pm) perl(HTML/TreeBuilder.pm) perl(IO/File.pm) perl(IO/Handle.pm) perl(IPC/Open2.pm) perl(LWP/UserAgent.pm) perl(Math/BigFloat.pm) perl(Math/BigInt.pm) perl(Scalar/Util/Instance.pm) perl(Smart/Comments.pm) perl(Symbol.pm) perl(Text/Diff.pm) perl(Tie/RefHash.pm) perl(Tie/RefHash/Weak.pm) perl(URI/URL.pm) perl(base.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Test-Weaken
%define upstream_version 3.022000

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2_6

Summary:    Test that freed memory is, in fact, freed
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
'Test::Weaken' helps detect unfreed Perl data in arrays, hashes, scalars,
objects, etc, by descending recursively through structures and watching
that everything is freed. Unfreed data is a useless overhead and may cause
an application to abend due to lack of memory.

Normally if the last reference to something is discarded then it and
anything in it is freed automatically. But this might not occur due to
circular references, unexpected global variables or closures, or reference
counting mistakes in XSUBs.

'Test::Weaken' is named for the strategy used to detect leaks. References
are taken to the test objects and all their contents, then those references
are weakened and expected to be then freed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml  README SIGNATURE
%perl_vendor_privlib/*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 3.022000-alt2_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 3.022000-alt2_5
- update by mgaimport

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 3.022000-alt2_4
- update by mgaimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.022000-alt2_3
- moved to Sisyphus

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 3.022000-alt1_3
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.022000-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 3.020000-alt1_1
- converted for ALT Linux by srpmconvert tools

