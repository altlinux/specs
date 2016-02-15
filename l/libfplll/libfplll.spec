# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libgmp-devel
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
Name:           libfplll
Version:        4.0.4
Release:        alt1_8
Summary:        LLL-reduces euclidean lattices
License:        LGPLv2+
URL:            https://github.com/dstehle/fplll
Source0:        http://perso.ens-lyon.fr/damien.stehle/fplll/%{name}-%{version}.tar.gz

BuildRequires:  libmpfr-devel
Source44: import.info

%description
fplll contains several algorithms on lattices that rely on
floating-point computations. This includes implementations of the
floating-point LLL reduction algorithm, offering different
speed/guarantees ratios. It contains a 'wrapper' choosing the
estimated best sequence of variants in order to provide a guaranteed
output as fast as possible. In the case of the wrapper, the
succession of variants is oblivious to the user. It also includes
a rigorous floating-point implementation of the Kannan-Fincke-Pohst
algorithm that finds a shortest non-zero lattice vector, and the BKZ
reduction algorithm.


%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Group: Engineering
Summary:        Command line tools that use %{name}
Requires:       %{name}%{?_isa} = %{version}

%description    tools
The %{name}-tools package contains command-line tools that expose
the functionality of %{name}.


%prep
%setup -q

%build
%configure --disable-static LDFLAGS="-Wl,--as-needed $RPM_LD_FLAGS"

# Eliminate hardcoded rpaths, and workaround libtool moving all -Wl options
# after the libraries to be linked
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|-nostdlib|-Wl,--as-needed &|' \
    -i libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%check
export LD_LIBRARY_PATH=$PWD/src/.libs
make check


%files
%doc AUTHORS NEWS README.html
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/fplll.h
%{_includedir}/fplll/
%{_libdir}/*.so

%files tools
%{_bindir}/*


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_7
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_2
- update to new release by fcimport

* Tue Jun 04 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_1
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.3-alt1_1
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_2
- update to new release by fcimport

* Tue Feb 05 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_1
- update to new release by fcimport

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1_2
- update to new release by fcimport

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.12-alt2_5.2
- update to new release by fcimport

* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.12-alt2_4.2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.12-alt2_3.2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 3.0.12-alt2_2.2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 3.0.12-alt1_2.2
- initial import by fcimport

