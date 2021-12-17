# BEGIN SourceDeps(oneline):
BuildRequires: libgmp-devel mpir-devel
# END SourceDeps(oneline)
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 10

Name:           libfplll
Version:        5.4.1
%global so_version 7
Release:        alt1_%autorelease
Summary:        Lattice algorithms using floating-point arithmetic

License:        LGPLv2+
URL:            https://fplll.github.io/fplll/
Source0:        https://github.com/fplll/fplll/releases/download/%{version}/fplll-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(qd)

BuildRequires:  help2man
Source44: import.info

%description
fplll contains implementations of several lattice algorithms. The
implementation relies on floating-point orthogonalization, and LLL is central
to the code, hence the name.

It includes implementations of floating-point LLL reduction algorithms,
offering different speed/guarantees ratios. It contains a 'wrapper' choosing
the estimated best sequence of variants in order to provide a guaranteed output
as fast as possible. In the case of the wrapper, the succession of variants is
oblivious to the user.

It includes an implementation of the BKZ reduction algorithm, including the
BKZ-2.0 improvements (extreme enumeration pruning, pre-processing of blocks,
early termination). Additionally, Slide reduction and self dual BKZ are
supported.

It also includes a floating-point implementation of the Kannan-Fincke-Pohst
algorithm that finds a shortest non-zero lattice vector. Finally, it contains a
variant of the enumeration algorithm that computes a lattice vector closest to
a given vector belonging to the real span of the lattice.


%package        devel
Group: Development/C
Summary:        Development files for libfplll

Requires:       libfplll = %{version}-%{release}

%description    devel
The libfplll-devel package contains libraries and header files for
developing applications that use libfplll.


# The static library is required by Macaulay2. See its spec file for a full
# explanation; the essential justification is excerpted below:
#
#   We have to use the static version of the libfplll and givaro library. They
#   have global objects whose constructors run before GC is initialized. If we
#   allow the shared libraries to be unloaded, which happens as a normal part
#   of Macaulay2's functioning, then GC tries to free objects it did not
#   allocate, which leads to a segfault.
%package        static
Group: System/Libraries
Summary:        Static library for libfplll


%description    static
The libfplll-static package contains a static library for libfplll.


%package        tools
Group: Engineering
Summary:        Command line tools that use libfplll

Requires:       libfplll = %{version}-%{release}

%description    tools
The libfplll-tools package contains command-line tools that expose
the functionality of libfplll.


%prep
%setup -q -n fplll-%{version}



%build
autoreconf --install --force --verbose
%configure --disable-silent-rules

# Eliminate hardcoded rpaths, and work around libtool moving all -Wl options
# after the libraries to be linked
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|-nostdlib|-Wl,--as-needed &|' \
    -i libtool

%make_build

# Build man pages with help2man. The result is not as good as hand-written, but
# quite adequate.
for cmd in fplll latticegen
do
  LD_LIBRARY_PATH="${PWD}/fplll/.libs" \
      help2man --no-info --output="${cmd}.1" "./fplll/${cmd}"
done


%install
%makeinstall_std
find '%{buildroot}' -type f -name '*.la' -print -delete

install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p *.1


%check
LD_LIBRARY_PATH="${PWD}/src/.libs" %make_build check


%files
%doc NEWS README.md
%doc --no-dereference COPYING
%{_libdir}/libfplll.so.%{so_version}*
%{_datadir}/fplll/


%files devel
%{_includedir}/fplll.h
%{_includedir}/fplll/
%{_libdir}/libfplll.so
%{_libdir}/pkgconfig/fplll.pc


%files static
%{_libdir}/libfplll.a


%files tools
%{_bindir}/fplll
%{_bindir}/latticegen
%{_mandir}/man1/fplll.1*
%{_mandir}/man1/latticegen.1*


%changelog
* Fri Dec 17 2021 Igor Vlasenko <viy@altlinux.org> 5.4.1-alt1_10
- update to new release by fcimport

* Fri Oct 01 2021 Igor Vlasenko <viy@altlinux.org> 5.4.1-alt1_2
- new version

* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 5.3.1-alt2_1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Fri Dec 27 2019 Igor Vlasenko <viy@altlinux.ru> 5.3.1-alt1_1
- update to new release by fcimport

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

