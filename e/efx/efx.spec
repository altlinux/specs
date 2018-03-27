Epoch: 1
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name efx
%define version 1.9.99
%define option  0
%define date    20140509
%if %option
%define rel 0.%option.1
%define namevers %name-%version-%option
%else
%define rel 2
%define namevers %name-%version
%endif
%if %date
%define release -c %date %rel
%else
%define release %rel
%endif

%define major 1
%define libname lib%{name}%{major}
%define libnamedev lib%{name}-devel

Summary: Graphics Library
Name:    efx
Version: 1.9.99
Release: alt2_2
License: LGPLv2+
Group: Graphical desktop/Enlightenment
# creating archive is quite simple:
# svn export http://svn.enlightenment.org/svn/e/branches/%name-1.1 %name
# tar cJf %name-%svn.tar.xz %name
%if %date
Source: %name-%date.tar.bz2
%else
Source: http://download.enlightenment.org/releases/%namevers.tar.bz2
%endif
URL: http://trac.enlightenment.org/e/wiki/Efx
BuildRequires: doxygen
BuildRequires: efl-libs-devel libelementary-devel
Source44: import.info


%description
%name is a graphics library.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{?epoch:%epoch:}%{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries.

%prep
%if %date
%setup -qn %name
%else
%setup -qn %namevers
%endif

%build
%if %date
LC_ALL=C NOCONFIGURE=1 ./autogen.sh
%endif
%configure --disable-static
%make

%install
%makeinstall_std

find %buildroot -name *.la | xargs rm

%files
%doc AUTHORS
%{_bindir}/test_*

%files -n %libname
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*
%{_datadir}/%name

%files -n %libnamedev
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/*


%changelog
* Tue Mar 27 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.9.99-alt2_2
- revived as mgaimport

* Wed Mar 02 2016 Ildar Mulyukov <ildar@altlinux.ru> 1.11.99-alt1.git.4.g1792af5
- initial build for ALT Linux Sisyphus

