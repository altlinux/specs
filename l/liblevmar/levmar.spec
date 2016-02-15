# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: libblas-devel
%add_optflags %optflags_shared
%define oldname levmar
# SOlib major and minor version
%global major 2
%global minor 2

Name:		liblevmar
Version:	2.5
Release:	alt1_13
Summary:	Levenberg-Marquardt nonlinear least squares algorithm
URL:		http://www.ics.forth.gr/~lourakis/levmar/

Source0:	http://www.ics.forth.gr/~lourakis/levmar/levmar-%{version}.tgz

# Patch to fix compilation of the shared library and compile the demo program
# Sent to levmar author on 28-Jan-2010
Patch0:		levmar-shared.patch

License:	GPLv2+
Group:		System/Libraries

BuildRequires:	dos2unix
BuildRequires:	liblapack-devel
Source44: import.info
Provides: levmar = %{version}-%{release}

%description
levmar is a native ANSI C implementation of the Levenberg-Marquardt
optimization algorithm.  Both unconstrained and constrained (under linear
equations, inequality and box constraints) Levenberg-Marquardt variants are
included.  The LM algorithm is an iterative technique that finds a local
minimum of a function that is expressed as the sum of squares of nonlinear
functions.  It has become a standard technique for nonlinear least-squares
problems and can be thought of as a combination of steepest descent and the
Gauss-Newton method.  When the current solution is far from the correct on,
the algorithm behaves like a steepest descent method: slow, but guaranteed
to converge.  When the current solution is close to the correct solution, it
becomes a Gauss-Newton method.

%package devel
Summary:	Development files for levmar library, and demo program
Group:		Development/C
Requires:	levmar = %{version}
Provides: levmar-devel = %{version}-%{release}

%description devel
Development files for the levmar library, and demo program.

%prep
%setup -n %{oldname}-%{version} -q
%patch -P 0 -p1 -b .shared
dos2unix -k README.txt

%build
mkdir sobj
make CFLAGS="%{optflags} -funroll-loops -fPIC" %{?_smp_mflags} -f Makefile.so

%install
install -D -p -m 755 sobj/liblevmar.so.%{major}.%{minor} %{buildroot}%{_libdir}/liblevmar.so.%{major}.%{minor}
install -D -p -m 644 levmar.h %{buildroot}%{_includedir}/levmar.h
install -D -p -m 755 lmdemo %{buildroot}%{_bindir}/lmdemo
ln -s liblevmar.so.%{major}.%{minor} %{buildroot}%{_libdir}/liblevmar.so.%{major}
ln -s liblevmar.so.%{major}.%{minor} %{buildroot}%{_libdir}/liblevmar.so

%files
%doc README.txt LICENSE
%{_libdir}/liblevmar.so.%{major}.%{minor}
%{_libdir}/liblevmar.so.%{major}

%files devel
%{_includedir}/levmar.h
%{_libdir}/liblevmar.so
%{_bindir}/lmdemo

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_10
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_9
- new version

