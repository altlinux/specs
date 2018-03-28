# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name rpmconstant
%define major		0
%define libname		lib%{name}%{major}
%define develname	lib%{name}-devel

Summary: A library to bind RPM constant values
Name: rpmconstant
Version: 0.1.4
Release: alt2_7
Source0: http://rpm4.zarb.org/download/%{name}-%{version}.tar.gz
License: LGPLv2.1
Group: Development/C
Url: https://github.com/gitpan/rpmconstant
BuildRequires: libpopt-devel 
BuildRequires: librpm-devel
Source44: import.info

%description
This library provides basic functions to map internal RPM constant values
with their name. This is useful for perl/python or other language which has
binding over rpmlib.

%package -n %libname
Summary: A library to bind rpm constant
Group: Development/C
Provides: lib%{name} = %version-%release

%description -n %libname
This library provides basics functions to map internal rpm constant value
with their name. This is useful for perl/python or other language which has
binding over rpmlib.

%package -n %develname
Summary: Development files from librpmconstant
Group: Development/C
Provides: %name-devel = %version-%release
Provides: lib%{name}-devel = %version-%release
Requires: %libname = %version-%release
Obsoletes: librpmconstant0-devel

%description -n %develname
This library provides basics functions to map internal rpm constant value
with their name. This is useful for perl/python or other language which has
binding over rpmlib.

You need this package to build applications using librpmconstant.

%prep
%setup -q

%build
mv rpmconstanttbl.c rpmconstanttbl.c.old # Ensure this file is regenated
%configure --disable-static
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la

%files
%doc AUTHORS ChangeLog README
%_bindir/%name

%files -n %libname
%_libdir/lib%name.so.%{major}
%_libdir/lib%name.so.%{major}.*

%files -n %develname
%doc constant.c AUTHORS ChangeLog README
%_includedir/%name/%name.h
%_libdir/lib%name.so


%changelog
* Wed Mar 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.4-alt2_7
- set url to https://github.com/gitpan/rpmconstant (closes: #34723)

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.4-alt1_7
- new version

