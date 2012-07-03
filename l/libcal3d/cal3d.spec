# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/blender /usr/bin/db2html /usr/bin/doxygen /usr/bin/valgrind
# END SourceDeps(oneline)
BuildRequires: gcc-c++
%add_optflags %optflags_shared
%define oldname cal3d
Name:           libcal3d
Version:        0.11.0
Release:        alt1_12
Summary:        Skeletal based 3-D character animation library

License:        LGPLv2+
URL:            http://gna.org/projects/cal3d
Source0:        http://download.gna.org/%{oldname}/sources/%{oldname}-%{version}.tar.gz
Patch0:         %{oldname}-0.11.0-gcc43.patch

BuildRequires:  doxygen libtool

%if 0%{?suse_version}
Group:          System/Libraries
BuildRequires:  docbook-toys gcc-c++
%else
Group:          System/Libraries
BuildRequires:  docbook-utils
%endif
Source44: import.info
Provides: cal3d = %{version}-%{release}

%description
Cal3D is a skeletal based 3-D character animation library written in C++
in a platform-/graphic API-independent way.

%package devel
Summary:        Header files, libraries and development documentation for Cal3D
Group:          Development/C++
Requires:       libcal3d = %{version}-%{release}
Provides: cal3d-devel = %{version}-%{release}

%description devel
This package contains the header files, libraries and documentation
for Cal3D.

%package doc
Summary:        Documentation files for Cal3D
Group:          Documentation
Requires:       libcal3d = %{version}-%{release}
Provides: cal3d-doc = %{version}-%{release}

%description doc
This package contains modeling documentation and a users guide for Cal3D.


%prep
%setup -q -n %{oldname}-%{version}
%patch0 -p0 -b .gcc43


%build
LIBTOOL=libtool %configure
make LIBTOOL=libtool %{?_smp_mflags}
( cd docs && make doc-guide && make doc-api )


%install
make install DESTDIR=$RPM_BUILD_ROOT

# remove libtool archives and static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a


%check
# https://gna.org/bugs/index.php?8416
#make check


%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/cal3d_converter
%{_mandir}/man1/cal3d_converter.1.*
%{_libdir}/*.so.*

%files devel
%doc docs/api/html/*
%{_includedir}/%{oldname}
%{_libdir}/pkgconfig/%{oldname}.pc
%{_libdir}/*.so

%files doc
%doc docs/guide
# upstream forgot this for 0.11.0: docs/modeling


%changelog
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_12
- rebuild to get rid of #27020

* Fri Feb 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_11
- new fc release

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_10
- initial release by fcimport

