# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major 0
%define libname	libopennet%{major}
%define develname libopennet-devel

Summary:	Libopennet allows you to open_net() files the same way you open() them now
Name:		libopennet
Version:	0.9.9
Release:	alt1_6
Group:		System/Libraries
License:	LGPL
URL:		http://www.rkeene.org/oss/libopennet/
Source0:	http://www.rkeene.org/files/oss/libopennet/%{name}-%{version}.tar.bz2
Patch0:		libopennet-0.9.3-DESTDIR.diff
Source44: import.info

%description
Libopennet allows you to open_net()  urls (or files, for that matter) the same
way you would normally open() just files.

%package -n	%{libname}
Summary:	Libopennet allows you to open_net() files the same way you open() them now
Group:          System/Libraries

%description -n	%{libname}
Libopennet allows you to open_net()  urls (or files, for that matter) the same
way you would normally open() just files.

%package -n	%{develname}
Summary:	Library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Obsoletes:	%{_lib}opennet0-devel < %{version}-%{release}

%description -n	%{develname}
Libopennet allows you to open_net()  urls (or files, for that matter) the same
way you would normally open() just files.

This package contains the %{name} library and its header files.

%prep
%setup -q
%patch0 -p0

%build
# fix soname and shared library build detection
export SHOBJFLAGS="-Wl,-soname=%{name}.so.%{major} -shared -rdynamic -fPIC -D_REENTRANT"
%configure --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc ChangeLog LICENSE README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_mandir}/man3/*


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_6
- new version

