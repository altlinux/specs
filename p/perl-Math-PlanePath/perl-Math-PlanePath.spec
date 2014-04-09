# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Cellular/Automata/Wolfram.pm) perl(Class/Singleton.pm) perl(Data/Dumper.pm) perl(Data/Float.pm) perl(Devel/Comments.pm) perl(Devel/Peek.pm) perl(Devel/TimeThis.pm) perl(Encode.pm) perl(File/HomeDir.pm) perl(File/Map.pm) perl(FindBin.pm) perl(Geometry/AffineTransform.pm) perl(Graph.pm) perl(Graph/Easy.pm) perl(HTML/Entities/Interpolate.pm) perl(IPC/Run.pm) perl(Image/Base.pm) perl(Image/Base/Text.pm) perl(Inline.pm) perl(Language/Logo.pm) perl(List/MoreUtils.pm) perl(List/Pairwise.pm) perl(Math/BaseCnv.pm) perl(Math/BigRat.pm) perl(Math/Complex.pm) perl(Math/ContinuedFraction.pm) perl(Math/Factor/XS.pm) perl(Math/Matrix.pm) perl(Math/Polynomial.pm) perl(Math/Polynomial/Horner.pm) perl(Math/Prime/XS.pm) perl(Math/Symbolic.pm) perl(Math/Symbolic/Custom/Simplification.pm) perl(Math/Symbolic/Custom/Transformation.pm) perl(Math/Symbolic/Derivative.pm) perl(Math/Trig.pm) perl(Module/Load.pm) perl(Module/Util.pm) perl(Number/Fraction.pm) perl(POSIX.pm) perl(Search/Dict.pm) perl(Set/IntSpan/Fast.pm) perl(Smart/Comments.pm) perl(Tie/IxHash.pm) perl(Time/HiRes.pm) perl(Tk.pm) perl(URI/Escape.pm) perl(Wx.pm) perl(Wx/App.pm) perl(Wx/Event.pm) perl(base.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Math-PlanePath
Version:        115
Release:        alt1
Summary:        Mathematical paths through the 2-D plane
License:        GPLv3+
Group:          Development/Perl
URL:            http://user42.tuxfamily.org/math-planepath/index.html
Source:        http://www.cpan.org/authors/id/K/KR/KRYDE/Math-PlanePath-%{version}.tar.gz
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
#make test

%files
%doc Changes COPYING debian/copyright
%{perl_vendor_privlib}/Math*

%changelog
* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 115-alt1
- automated CPAN update

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 114-alt1_2
- moved to Sisyphus for Slic3r (by dd@ request)

