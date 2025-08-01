# BEGIN SourceDeps(oneline):
BuildRequires: libgc-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name chibi
%define		upstream_name_scheme %{name}-scheme

%define major   0
%define libname lib%{upstream_name_scheme}%{major}
%define devname lib%{name}-devel

Name:		chibi
Version:	0.11
Release:	alt1_1
Summary:	A small-footprint library for use as a C Extension Language
Group:		Development/Tools
License:	BSD
URL:		https://github.com/ashinn/chibi-scheme
Source0:	https://github.com/ashinn/%{upstream_name_scheme}/releases/download/%{version}/%{upstream_name_scheme}-%{version}.0.tgz

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

%package	-n %{devname}
Summary:	Development files for the %{name} package
Group:		Development/Tools
Provides:	%{upstream_name_scheme}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Provides:	chibi-devel = %{version}-%{release}
Obsoletes:	chibi-devel < 0.8-6

%description	-n %{devname}
This package contains development and include files for the
%{name} package.


%prep
%setup -qn %{upstream_name_scheme}-%{version}.0

%build
make	CFLAGS="%{optflags}" \
	LDFLAGS="" XLIBS=-lm all

%install
%makeinstall_std \
	PREFIX=%{_prefix} LIBDIR=%{_libdir} \
	SOLIBDIR=%{_libdir} BINMODDIR=%{_libdir}/%{name}

%files
%doc AUTHORS README.md
%doc --no-dereference COPYING
%{_bindir}/%{name}-*
%{_bindir}/snow-%{name}
%{_bindir}/snow-%{name}.*
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}-*.1*

%files -n %{libname}
%doc --no-dereference COPYING
%{_libdir}/libchibi-scheme.so.%{major}
%{_libdir}/libchibi-scheme.so.%{major}.*

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/libchibi-scheme.so
%{_libdir}/pkgconfig/%{upstream_name_scheme}.pc


%changelog
* Fri Aug 01 2025 Igor Vlasenko <viy@altlinux.org> 0.11-alt1_1
- update by mgaimport

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- update by mgaimport

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.3-alt1_1
- new version

