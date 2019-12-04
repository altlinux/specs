# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 0
%define libname libredblack%{major}
%define develname libredblack-devel

Summary:        Library for handling red-black tree searching algorithm
Name:           libredblack
Version:        1.3
Release:        alt1_4
Group:          System/Libraries
License:        LGPLv2+
URL:            http://libredblack.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         libredblack-typo.diff
Patch1:         libredblack-1.3-optflags.patch
Source44: import.info

%description
This implements the red-black balanced tree algorithm.

%package -n     %{libname}
Summary:        Library for handling red-black tree searching algorithm
Group:          System/Libraries

%description -n %{libname}
This implements the redblack balanced tree algorithm.

%package -n     %{develname}
Summary:        Libraries and header files for the %{libname} library
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
To develop programs based upon the libredblack library, the system needs to
have these header and object files available for creating the executables.

%prep

%setup -q
%patch0 -p1
%patch1 -p1


%build
# fix build on aarch64
autoreconf -vfi

%configure --disable-static --with-python=/usr/bin/python2
%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%doc AUTHORS ChangeLog README
%{_libdir}/libredblack.so.%{major}*

%files -n %{develname}
%doc example*.c example*.rb
%{_bindir}/rbgen
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_datadir}/libredblack


%changelog
* Wed Dec 04 2019 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4
- fixed build

* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2
- new version

