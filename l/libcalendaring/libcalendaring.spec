# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: /usr/bin/perl
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name libcalendaring
%define major 0
%define libname libkolab%{major}
%define develname lib%{name}-devel

Name:           libcalendaring
Version:        4.9.1
Release:        alt1_1
Summary:        Library for Calendaring

Group:          System/Servers
License:        LGPLv2+
URL:            http://www.kolab.org/about/libcalendaring

Source0:        https://cgit.kolab.org/libcalendaring/libcalendaring-4.9.1.tar.gz

BuildRequires:  boost-devel
BuildRequires:  ccmake cmake ctest
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libical)
BuildRequires:  libqt4-devel qt5-declarative-devel qt5-tools
Source44: import.info


%description
Advanced calendaring library for Kolab, based on parts of KDE = 4.9
This package is only required for building kolab-utils and only as long as kolab-utils isn't ported
to KF5/QT5. After porting, this package can be obsoleted.


#main package (contains .so.[major]. only)
%package -n     %{libname}
Summary:        Library for Calendaring
Group:          System/Servers
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
Advanced calendaring library for Kolab, based on parts of KDE >= 4.9


%package -n     %{develname}
Summary:        Development headers
Group:          System/Servers
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
These are development headers. Don't bother.

%prep
%setup -q

%build

%{mageia_cmake} \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DLIB_INSTALL_DIR=%{_libdir} \
    -DQT_NO_DEBUG_OUTPUT=1 \
    -DQT_NO_WARNING_OUTPUT=1 \
    ..


%install
%makeinstall_std -C build

 
%files -n %{libname}
%{_libdir}/libcalendaring-*.so.%{major}*

%files -n %{develname}
%{_includedir}/calendaring
%{_libdir}/libcalendaring*.so
%{_libdir}/libcalendaring*.a



%changelog
* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 4.9.1-alt1_1
- new version

