# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libfplll
Version:        3.0.12
Release:        alt2_4.2
Summary:        LLL-reduces euclidian lattices
Group:          System/Libraries
License:        LGPLv2+
URL:            http://perso.ens-lyon.fr/damien.stehle/english.html#software
Source0:        http://perso.ens-lyon.fr/damien.stehle/downloads/libfplll-%{version}.tar.gz

BuildRequires:  libgmp-devel libgmp_cxx-devel
BuildRequires:  libmpfr-devel
Source44: import.info


%description
fpLLL-3.0 contains several algorithms on lattices that rely on
floating-point computations. This includes implementations of the
floating-point LLL reduction algorithm, offering different
speed/guarantees ratios. It contains a 'wrapper' choosing the
estimated best sequence of variants in order to provide a guaranteed
output as fast as possible. In the case of the wrapper, the
succession of variants is oblivious to the user. It also includes
a rigorous floating-point implementation of the Kannan-Fincke-Pohst
algorithm that finds a shortest non-zero lattice vector.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libfplll = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mv $RPM_BUILD_ROOT%{_bindir}/generate \
  $RPM_BUILD_ROOT%{_bindir}/fplll_generate
mkdir -p $RPM_BUILD_ROOT%{_includedir}/fplll
mv $RPM_BUILD_ROOT%{_includedir}/*.{h,cpp} \
  $RPM_BUILD_ROOT%{_includedir}/fplll


%check
make check


%files
%doc COPYING README NEWS
%{_libdir}/*.so.*
%{_bindir}/fplll
%{_bindir}/fplll_micro
%{_bindir}/fplll_verbose
%{_bindir}/fplll_generate
%{_bindir}/llldiff

%files devel
%{_includedir}/fplll
%{_libdir}/*.so


%changelog
* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.12-alt2_4.2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.12-alt2_3.2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 3.0.12-alt2_2.2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 3.0.12-alt1_2.2
- initial import by fcimport

