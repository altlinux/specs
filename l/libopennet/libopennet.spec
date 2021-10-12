%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major 0
%define libname	libopennet%{major}
%define develname libopennet-devel

Summary:	Libopennet allows you to open_net() files the same way you open() them now
Name:		libopennet
Version:	0.9.9
Release:	alt2_10
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

%package -n     %{develname}-static
Summary:        Static library for the %{name} library
Group:          Development/C
Requires:       %{develname} = %EVR

%description -n %{develname}-static
This package contains the static %{name} library

%files -n %{develname}-static
%{_libdir}/*.a


%prep
%setup -q
%patch0


%build
# fix soname and shared library build detection
export SHOBJFLAGS="-Wl,-soname=%{name}.so.%{major} -shared -rdynamic -fPIC -D_REENTRANT"
%configure --disable-static
%make_build

%install
%makeinstall_std

%files -n %{libname}
%doc ChangeLog LICENSE README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*


%changelog
* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 0.9.9-alt2_10
- fixed build

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 0.9.9-alt1_10
- update by mgaimport

* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_7
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_6
- new version

