# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(File/Spec/Functions.pm) perl(Scalar/Util.pm) perl(Test/Deep.pm) perl(Test/Differences.pm) perl(Test/Exception.pm) perl(Test/Warn.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Math-MatrixReal
Version:        2.09
Release:        alt2_4
Summary:        Manipulate matrix of reals
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Math-MatrixReal/
Source0:        http://www.cpan.org/authors/id/L/LE/LETO/Math-MatrixReal-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Benchmark.pm)
BuildRequires:  perl(Math/Complex.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Test/Simple.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Most.pm)
Requires:       perl(Exporter.pm)
Source44: import.info

%description
Implements the data type "matrix of reals" (and consequently also
"vector of reals") which can be used almost like any other basic
Perl type thanks to OPERATOR OVERLOADING, i.e.,

    $A = $matrix1 * $matrix2;
    $B = $A ** 2;
    $C = $A + 2*B;
    $D = $C - $B/2;
    $inverse = $C ** -1;
    $inverse = 1/$C;
    
does what you would like it to do.

%prep
%setup -q -n Math-MatrixReal-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%check
./Build test

%files
%doc CHANGES CREDITS GOALS README.mkd OLD_README TODO
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.09-alt2_4
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1_4
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1_2
- fc import

