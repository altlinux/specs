# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/curl /usr/bin/wget boost-python-devel gcc-c++ python-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname ompl
Name:           libompl
Version:        1.0.0
Release:        alt1_10
Summary:        The Open Motion Planning Library

Group:          System/Libraries
License:        BSD
URL:            http://ompl.kavrakilab.org/
Source0:        https://bitbucket.org/%{oldname}/%{oldname}/downloads/%{oldname}-%{version}-Source.tar.gz
# https://bitbucket.org/ompl/ompl/issues/206/cannot-compile-as-c-11
Patch0:         ompl-1.0.0-cxx11.patch
BuildRequires: boost-devel boost-devel-headers boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel
BuildRequires: ctest cmake
BuildRequires:  doxygen
BuildRequires:  flann-devel
BuildRequires:  graphviz
BuildRequires:  libode-devel
BuildRequires:  python
BuildRequires:  ruby
Source44: import.info
Provides: ompl = %{version}-%{release}

%description
The Open Motion Planning Library (OMPL) consists of many state-of-the-art 
sampling-based motion planning algorithms. OMPL itself does not contain 
any code related to, e.g., collision checking or visualization. This is 
a deliberate design choice, so that OMPL is not tied to a particular 
collision checker or visualization front end.

%package        devel
Summary:        Development files for %{oldname}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}
Requires: boost-devel-headers
Provides: ompl-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.


%prep
%setup -q -n %{oldname}-%{version}-Source
%patch0 -p1
# Get rid of bundled odeint
rm -rf src/external/omplext_odeint/

%build
# Python bindings are disabled because dependencies pygccxml and pyplusplus are not packaged for Fedora
mkdir build
cd build
%{fedora_cmake} -DCMAKE_SKIP_RPATH=ON \
  -DOMPL_BUILD_PYBINDINGS=OFF \
  -DOMPL_LIB_INSTALL_DIR=%{_lib} \
  -DBOOST_LIBRARYDIR=%{_libdir} \
  -DODE_LIB_PATH=%{_libdir} \
  -DBUILD_OMPL_TESTS=ON  \
  -DOMPL_ODESOLVER=ON \
  -DOMPL_REGISTRATION=OFF ..

make %{?_smp_mflags}
make doc
rm -f doc/html/installdox

%install
make -C build install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/cmake/Modules
cp %{buildroot}%{_datadir}/ompl/ompl-config.cmake %{buildroot}%{_datadir}/cmake/Modules/FindOMPL.cmake

rm -f %{buildroot}%{_datadir}/%{oldname}/demos/*.py
rm -rf %{buildroot}%{_includedir}/%{oldname}/CMakeFiles
rm -rf %{buildroot}%{_bindir}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make -C build test || exit 0

%files
%doc LICENSE README.md
%{_libdir}/libompl.so.*
%{_mandir}/man1/*.1.*

%files devel
%doc doc/html
%{_libdir}/libompl.so
%{_includedir}/%{oldname}
%{_datadir}/%{oldname}
%{_libdir}/pkgconfig/*.pc
%{_datadir}/cmake/Modules/FindOMPL.cmake

%changelog
* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_10
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2
- update to new release by fcimport

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.0.0-alt1_1.1
- rebuild with boost 1.57.0

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.14.2-alt1_3
- update to new release by fcimport

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.2-alt1_2.1
- Rebuilt with new ode

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.14.2-alt1_2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_2
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_1
- update to new release by fcimport

* Sun Apr 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1_4
- initial fc import

