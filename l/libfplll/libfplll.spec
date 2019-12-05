# BEGIN SourceDeps(oneline):
BuildRequires: libgmp-devel mpir-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libfplll
Version:        5.3.0
Release:        alt1_1
Summary:        LLL-reduces euclidean lattices
License:        LGPLv2+
URL:            https://github.com/fplll/fplll
Source0:        https://github.com/fplll/fplll/releases/download/%{version}/fplll-%{version}.tar.gz
# https://github.com/fplll/fplll/pull/398
Patch0:         0001-Fix-out-of-bounds-vector-accesses-in-Pruner-enforce.patch
# https://github.com/cr-marcstevens/snippets/pull/1
Patch1:         0002-Eliminate-race-condition-in-thread-pool.patch

BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libmpfr-devel
BuildRequires:  libqd-devel
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
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Group: System/Libraries
Summary:        Static library for %{name}

%description    static
The %{name}-static package contains a static library for %{name}.


%package        tools
Group: Engineering
Summary:        Command line tools that use %{name}
Requires:       %{name} = %{version}-%{release}

%description    tools
The %{name}-tools package contains command-line tools that expose
the functionality of %{name}.


%prep
%setup -q -n fplll-%{version}
%patch0 -p1
%patch1 -p1


# Fix broken test for a bool type
sed -e '/#ifndef bool/,/#endif/d' \
    -e '/#ifndef false/,/#endif/d' \
    -e '/#if false/,/#endif/d' \
    -e '/#ifndef true/,/#endif/d' \
    -e '/#if true/,/#endif/d' \
    -e '/ac_cv_type__Bool/s/\$ac_includes_default/#include <stdbool.h>/' \
    -i configure

%build
%configure --disable-silent-rules LIBS=-lpthread

# Eliminate hardcoded rpaths, and workaround libtool moving all -Wl options
# after the libraries to be linked
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|-nostdlib|-Wl,--as-needed &|' \
    -i libtool

%make_build

# Build the man pages
cd fplll
export LD_LIBRARY_PATH=$PWD/.libs
help2man -N -o ../fplll.1 ./fplll
help2man -N -o ../latsieve.1 ./latsieve
help2man -N -o ../latticegen.1 ./latticegen
cd -

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p *.1 %{buildroot}%{_mandir}/man1

%check
LD_LIBRARY_PATH=$PWD/src/.libs make check


%files
%doc NEWS README.md
%doc --no-dereference COPYING
%{_libdir}/libfplll.so.6*
%{_datadir}/fplll/

%files devel
%{_includedir}/fplll.h
%{_includedir}/fplll/
%{_libdir}/libfplll.so
%{_libdir}/pkgconfig/fplll.pc

%files static
%{_libdir}/*.a

%files tools
%{_bindir}/*
%{_mandir}/man1/fplll.1*
%{_mandir}/man1/latsieve.1*
%{_mandir}/man1/latticegen.1*


%changelog
* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 5.3.0-alt1_1
- update to new release by fcimport

* Thu Aug 29 2019 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt1_4
- fixed self-BR (thanks to rider@)

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt1_1
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.0-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_4
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_2
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.5-alt1_2
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.5-alt1_1
- update to new release by fcimport

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

