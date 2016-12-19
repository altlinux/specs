# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gettext /usr/bin/svn gcc-c++ libclaw-devel
# END SourceDeps(oneline)
BuildRequires: /proc
%add_optflags %optflags_shared
Name:           libclaw
Version:        1.7.4
Release:        alt1_15
Summary:        C++ Library of various utility functions
Group:          System/Libraries
License:        LGPLv2
URL:            http://libclaw.sourceforge.net/
Source0:        http://dl.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:         libclaw-1.6.1-nostrip.patch
Patch1:         libclaw-1.7.4-libdir.patch
Patch2:		libclaw-1.7.4-gcc62.patch
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires: ctest cmake
BuildRequires:  doxygen
BuildRequires: gettext-tools libasprintf-devel
BuildRequires: boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
Source44: import.info
Patch33: libclaw-1.7.4-alt-linkage.patch

%description
Claw (C++ Library Absolutely Wonderful) is a C++ library of various utility
functions. In doesn't have a particular objective but being useful to
anyone.


%package devel
Summary:        Development files for Claw library
Group:          Development/Other
Requires:       libclaw = %{version}
Requires: ctest cmake

%description devel
This package contains files needed to develop and build software against
Claw (C++ Library Absolutely Wonderful).


%prep
%setup -q
%patch0 -p1 -b .nostrip
%patch1 -p1 -b .libdir
%patch2 -p1 -b .gcc62
%patch33 -p1


%build
%{fedora_cmake} .
make %{?_smp_mflags} VERBOSE=1
find examples -type f |
while read F
do
        iconv -f iso8859-1 -t utf-8 $F |sed 's/\r//' >.utf8
        touch -r $F .utf8
        mv .utf8 $F
done


%install
make install DESTDIR=%{buildroot} VERBOSE=1
%find_lang %{name}


%files -f %{name}.lang
%{_libdir}/*.so.*
%doc %dir %{_datadir}/doc/libclaw1
%doc %{_datadir}/doc/libclaw1/COPYING


%files devel
%{_bindir}/claw-config
%{_datadir}/cmake/%{name}
%{_includedir}/claw
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%doc %{_datadir}/doc/libclaw1
%doc examples


%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.4-alt1_15
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.4-alt1_13
- update to new release by fcimport

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.7.4-alt1_12
- fixed build

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt3_5.1
- Rebuilt with libpng15

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt3_5
- fixed build

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt2_5
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt2_4
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt2_1
- spec cleanup thanks to ldv@

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_1
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- initial release by fcimport

