%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Cellular/Automata/Wolfram.pm) perl(Data/Dumper.pm) perl(Data/Float.pm) perl(Devel/Comments.pm) perl(Devel/Peek.pm) perl(Devel/TimeThis.pm) perl(File/Map.pm) perl(File/Slurp.pm) perl(FindBin.pm) perl(Geometry/AffineTransform.pm) perl(Graph.pm) perl(Graph/Easy.pm) perl(IPC/Run.pm) perl(Image/Base.pm) perl(Image/Base/Text.pm) perl(Inline.pm) perl(Language/Logo.pm) perl(List/MoreUtils.pm) perl(List/Pairwise.pm) perl(Math/BaseCnv.pm) perl(Math/BigRat.pm) perl(Math/Complex.pm) perl(Math/ContinuedFraction.pm) perl(Math/Factor/XS.pm) perl(Math/Matrix.pm) perl(Math/NumSeq/Abundant.pm) perl(Math/NumSeq/All.pm) perl(Math/NumSeq/BalancedBinary.pm) perl(Math/NumSeq/Base/IterateIth.pm) perl(Math/NumSeq/DigitCount.pm) perl(Math/NumSeq/DigitCountLow.pm) perl(Math/NumSeq/Fibbinary.pm) perl(Math/NumSeq/FibbinaryBitCount.pm)
BuildRequires: perl(Math/NumSeq/Fibonacci.pm) perl(Math/NumSeq/FibonacciWord.pm) perl(Math/NumSeq/GolayRudinShapiro.pm) perl(Math/NumSeq/MephistoWaltz.pm) perl(Math/NumSeq/Modulo.pm) perl(Math/NumSeq/OEIS.pm) perl(Math/NumSeq/OEIS/Catalogue/Plugin.pm) perl(Math/NumSeq/OEIS/File.pm) perl(Math/NumSeq/ProthNumbers.pm) perl(Math/NumSeq/Squares.pm) perl(Math/Polynomial.pm) perl(Math/Polynomial/Horner.pm) perl(Math/Prime/XS.pm) perl(Math/Symbolic.pm) perl(Math/Symbolic/Custom/Simplification.pm) perl(Math/Symbolic/Custom/Transformation.pm) perl(Math/Symbolic/Derivative.pm) perl(Math/Trig.pm) perl(Memoize.pm) perl(Module/Load.pm) perl(Module/Util.pm) perl(Number/Fraction.pm) perl(POSIX.pm) perl(Set/IntSpan/Fast.pm) perl(Smart/Comments.pm) perl(Tie/IxHash.pm) perl(Time/HiRes.pm) perl(Tk.pm) perl(URI/Escape.pm) perl(Wx.pm)
BuildRequires: perl(Wx/App.pm) perl(Wx/Event.pm) perl(base.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Math-PlanePath
Version:        125
Release:        alt1
Summary:        Mathematical paths through the 2-D plane
License:        GPLv3+
Group:          Development/Perl
URL:            http://user42.tuxfamily.org/math-planepath/index.html
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/Math-PlanePath-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(constant/defer.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Math/BigFloat.pm)
BuildRequires:  perl(Math/BigInt.pm)
BuildRequires:  perl(Math/Libm.pm)
BuildRequires:  perl(Math/NumSeq.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test.pm)
Requires:       perl(constant/defer.pm) >= 5
Requires:       perl(Math/Factor/XS.pm)
Requires:       perl(Math/NumSeq/Modulo.pm)
Requires:       perl(Module/Load.pm)

# Filtering unversioned provides and requires





Source44: import.info
%filter_from_provides /^perl\\(Math.PlanePath.CellularRule.Line.pm\\)$/d
%filter_from_provides /^perl\\(Math.PlanePath.CellularRule.OddSolid.pm\\)$/d
%filter_from_provides /^perl\\(Math.PlanePath.CellularRule.OneTwo.pm\\)$/d
%filter_from_requires /^perl\\(constant.defer.pm\\)$/d
%filter_from_requires /^perl\\(constant.pm\\)$/d

%description
This spot of Perl code calculates various mathematical paths through a 2-D X,Y
plane. There's no drawing in Math-PlanePath, just coordinate calculations.

%prep
%setup -q -n Math-PlanePath-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes COPYING debian/copyright examples
%{perl_vendor_privlib}/Math*

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 125-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 124-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 123-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 122-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 121-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 120-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 118-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 117-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 116-alt1_1
- update to new release by fcimport

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 116-alt1
- automated CPAN update

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 115-alt1_1
- converted for ALT Linux by srpmconvert tools

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 115-alt1
- automated CPAN update

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 114-alt1_2
- moved to Sisyphus for Slic3r (by dd@ request)

