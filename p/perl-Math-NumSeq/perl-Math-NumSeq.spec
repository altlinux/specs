%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(B/Concise.pm) perl(Bit/Vector.pm) perl(Class/Singleton.pm) perl(Compress/Zlib.pm) perl(Data/Float.pm) perl(Devel/Peek.pm) perl(Devel/TimeThis.pm) perl(Encode.pm) perl(File/Find.pm) perl(File/Map.pm) perl(Graph/Easy.pm) perl(HTML/Entities/Interpolate.pm) perl(IO/Select.pm) perl(IO/Uncompress/Gunzip.pm) perl(List/MoreUtils.pm) perl(Locale/Messages.pm) perl(Math/BaseCnv.pm) perl(Math/BigFloat.pm) perl(Math/BigRat.pm) perl(Math/Fibonacci.pm) perl(Math/Prime/Util.pm) perl(Math/Sequence.pm) perl(Math/Symbolic/AuxFunctions.pm) perl(Math/Symbolic/Custom/Simplification.pm) perl(Math/Symbolic/Custom/Transformation.pm) perl(Math/Symbolic/Derivative.pm) perl(Path/Class.pm) perl(Safe.pm) perl(Search/Dict.pm) perl(Smart/Comments.pm) perl(String/BitCount.pm) perl(String/Parity.pm) perl(Symbol.pm) perl(Test/Weaken.pm) perl(Text/Tabs.pm) perl(Tie/File.pm) perl(Tie/IxHash.pm) perl(Time/HiRes.pm) perl(URI/Escape.pm) perl(X11/Keysyms.pm) perl(X11/Protocol.pm) perl(X11/Protocol/WM.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Math-NumSeq
Version:        72
Release:        alt1
Summary:        Number sequences
License:        GPLv3+
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Math-NumSeq/
Source:        http://www.cpan.org/authors/id/K/KR/KRYDE/Math-NumSeq-%{version}.tar.gz
BuildArch:      noarch

%global with_maximum_interoperation 0

BuildRequires:  perl
BuildRequires:  perl(constant/defer.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dumper.pm)
#BuildRequires:  perl(Devel/FindRef.pm)
BuildRequires:  perl(Devel/StackTrace.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(File/HomeDir.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Math/BigInt.pm)
BuildRequires:  perl(Math/Factor/XS.pm)
BuildRequires:  perl(Math/Libm.pm)
BuildRequires:  perl(Math/Prime/XS.pm)
BuildRequires:  perl(Math/Trig.pm)
BuildRequires:  perl(Module/Load.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(Module/Util.pm)
BuildRequires:  perl(Parse/CPAN/Meta.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(SDBM_File.pm)
BuildRequires:  perl(Test.pm)
BuildRequires:  perl(Test/ConsistentVersion.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Synopsis.pm)
BuildRequires:  perl(Test/YAML/Meta.pm)
BuildRequires:  perl(YAML.pm)
BuildRequires:  perl(YAML/Syck.pm)
BuildRequires:  perl(YAML/Tiny.pm)
BuildRequires:  perl(YAML/XS.pm)
Requires:       perl(File/HomeDir.pm)
Requires:       perl(File/Temp.pm)
Requires:       perl(Math/Trig.pm)
Requires:       perl(Module/Load.pm)
Requires:       perl(SDBM_File.pm)

%if 0%{with_maximum_interoperation}
BuildRequires:  perl(Language/Expr.pm)
BuildRequires:  perl(Language/Expr/Compiler/Perl.pm)
BuildRequires:  perl(Math/Expression/Evaluator.pm)
BuildRequires:  perl(Math/Symbolic.pm)
Requires:       perl(Math/Expression/Evaluator.pm)
Requires:       perl(Math/Symbolic.pm)
Requires:       perl(Language/Expr.pm)
Requires:       perl(Language/Expr/Compiler/Perl.pm)
%endif
Source44: import.info

%description
This is a base class for some number sequences. Sequence objects can
iterate through values and some sequences have random access and/or
predicate test.

%prep
%setup -q -n Math-NumSeq-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
# TODO
#make test

%files
%doc Changes COPYING
%{perl_vendor_privlib}/Math/*

%changelog
* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 72-alt1
- automated CPAN update

* Sat Nov 21 2015 Igor Vlasenko <viy@altlinux.ru> 71-alt2
- dropped BR: perl(Devel/FindRef.pm)

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 71-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 70-alt1
- automated CPAN update

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 69-alt1
- automated CPAN update

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 68-alt1_1
- moved to Sisyphus for Slic3r (by dd@ request)

