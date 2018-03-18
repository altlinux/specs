# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        Fetion protocol library powered by ofetion project
Name:           libofetion
Version:        2.2.2
Release:        alt1_9
Group:          Networking/Instant messaging
License:        GPLv2+
URL:            http://code.google.com/p/ofetion/
Source0:        http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(openssl) < 1.1
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  ccmake cmake ctest
Conflicts:      openfetion < 2.1.0
Source44: import.info

%description
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%files
%{_datadir}/libofetion1

#---------------------------------------------------------------
%define major   1
%define libname libofetion%{major}

%package -n     %libname
Summary:        Fetion protocol library powered by ofetion project
Group:          Networking/Instant messaging
Requires:       %{name} = %{version}

%description -n %libname
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%files -n %libname
%{_libdir}/libofetion.so.%{major}
%{_libdir}/libofetion.so.%{major}.*

#---------------------------------------------------------------
%define develname libofetion-devel

%package -n     %develname
Summary:        Fetion protocol library powered by ofetion project
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %develname
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%files -n %develname
%{_includedir}/*
%{_libdir}/libofetion.so
%{_libdir}/pkgconfig/*.pc

#---------------------------------------------------------------

%prep
%setup -q

%build
%{mageia_cmake}
%make_build

%install
%makeinstall_std -C build

# we don't want these
find %{buildroot} -name '*.a' -delete


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1_9
- new version

