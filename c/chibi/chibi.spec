# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name chibi
%define		upstream_name_scheme %{name}-scheme
%define		major 0

%define libname lib%{upstream_name_scheme}%{major}

Name:		chibi
Version:	0.7.3
Release:	alt1_1
Summary:	A small-footprint library for use as a C Extension Language
Source0:	https://github.com/ashinn/%{upstream_name_scheme}/archive/%{version}.tar.gz
Group:		Development/Tools
License:	BSD
URL:		https://code.google.com/p/chibi-scheme/
Provides:	%{upstream_name_scheme} = %{version}-%{release}
Source44: import.info

%description
%{name} is a very small library intended for use as an extension
and scripting language in C programs.  In addition to support for
lightweight VM-based threads, each VM itself runs in an isolated heap
allowing multiple VMs to run simultaneously in different OS threads.

%package	-n %{libname}
Summary:	A small-footprint library for use as a C Extension Language
Group:		Development/Tools

%description	-n %{libname}
%{name} is a very small library intended for use as an extension
and scripting language in C programs.  In addition to support for
lightweight VM-based threads, each VM itself runs in an isolated heap
allowing multiple VMs to run simultaneously in different OS threads.

%package	devel
Summary:	Development files for the %{name} package
Group:		Development/Tools
Provides:	%{upstream_name_scheme}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description	devel
This package contains development and include files for the
%{name} package.


%prep
%setup -qn %{upstream_name_scheme}-%{version}

%build
make	PREFIX=%{_prefix} LIBDIR=%{_libdir} SOLIBDIR=%{_libdir} \
	BINMODDIR=%{_libdir}/%{name} CFLAGS="%{optflags}" \
	LDFLAGS="" XLIBS=-lm all

%install
make	PREFIX=%{_prefix} LIBDIR=%{_libdir} SOLIBDIR=%{_libdir} \
	BINMODDIR=%{_libdir}/%{name} DESTDIR=%{buildroot} install

%files
%doc AUTHORS COPYING README
%{_mandir}/man1/%{name}-*.1*
%{_bindir}/%{name}-*
%{_bindir}/snow-%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/libchibi-scheme.so.%{major}*

%files devel
%{_includedir}/%{name}
%{_libdir}/libchibi-scheme.so
%{_libdir}/pkgconfig/%{upstream_name_scheme}.pc


%changelog
* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.3-alt1_1
- new version

