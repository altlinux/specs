# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/blender /usr/bin/db2html /usr/bin/doxygen /usr/bin/valgrind
# END SourceDeps(oneline)
BuildRequires: gcc-c++
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname cal3d
Name:           libcal3d
Version:        0.11.0
Release:        alt2_16
Summary:        Skeletal based 3-D character animation library
License:        LGPLv2+
URL:            http://gna.org/projects/cal3d
Source0:        http://download.gna.org/%{oldname}/sources/%{oldname}-%{version}.tar.gz
Patch0:         %{oldname}-0.11.0-gcc43.patch
BuildRequires:  doxygen libtool
BuildRequires:  docbook-utils
Source44: import.info
Provides: cal3d = %{version}-%{release}

%description
Cal3D is a skeletal based 3-D character animation library written in C++
in a platform-/graphic API-independent way.

%package        devel
Group: Development/C++
Summary:        Header files, libraries and development documentation for Cal3D
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides: cal3d-devel = %{version}-%{release}

%description devel
This package contains the header files, libraries and documentation
for Cal3D.

%package doc
Group: Documentation
Summary:        Documentation files for Cal3D
BuildArch:      noarch
Provides: cal3d-doc = %{version}-%{release}

%description doc
This package contains modeling documentation and a users guide for Cal3D.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p0 -b .gcc43

%build
LIBTOOL=libtool %configure
make LIBTOOL=libtool %{?_smp_mflags}
( cd docs && make doc-guide && make doc-api )

%install
make install DESTDIR=%{buildroot}

# remove libtool archives and static libraries
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a

%check
# https://gna.org/bugs/index.php?8416
#make check

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/cal3d_converter
%{_mandir}/man1/cal3d_converter.1*
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
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt2_15
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt2_14
- update to new release by fcimport

* Mon Jan 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt2_13
- rebuild to fix requires

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_13
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_12
- rebuild to get rid of #27020

* Fri Feb 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_11
- new fc release

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_10
- initial release by fcimport

