# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cjose
%define major     0
%define libname   lib%{name}%{major}
%define develname lib%{name}-devel

Name:		cjose
Version:	0.6.2.2
Release:	alt1_1
Summary:	C library implementing the Javascript Object Signing and Encryption (JOSE)
Group:		System/Libraries
License:	MIT
URL:		https://github.com/OpenIDC/cjose
Source0:	https://github.com/OpenIDC/cjose/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	doxygen
BuildRequires:	gcc
BuildRequires:	pkgconfig(check) >= 0.9.2
BuildRequires:	pkgconfig(jansson) >= 2.3
BuildRequires:	pkgconfig(openssl) >= 1.0.1h
Source44: import.info

%description
cjose is a C library implementing the Javascript Object Signing
and Encryption (JOSE).

%package -n %{libname}
Summary:	C library implementing the Javascript Object Signing and Encryption (JOSE)
Group:		System/Libraries

%description -n %{libname}
cjose is a C library implementing the Javascript Object Signing
and Encryption (JOSE).

%package -n %{develname}
Summary:	Development files for cjose
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
cjose is a C library implementing the Javascript Object Signing
and Encryption (JOSE).

This package contains development files for %{name}.

%prep
%setup -q -n %{name}-%{version}


%build

# Undo the effects of -Werror so deprecation warnings don't halt the build
CFLAGS="$CFLAGS -Wno-error"
%configure --disable-static
%make_build

%check
# testsuite fails on arm
%ifnarch %{arm}
make check || (cat test/test-suite.log; exit 1)
%endif

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/doc/%{name}


%changelog
* Mon Oct 02 2023 Igor Vlasenko <viy@altlinux.org> 0.6.2.2-alt1_1
- update by mgaimport

* Tue Aug 02 2022 Igor Vlasenko <viy@altlinux.org> 0.6.1-alt1_3
- update by mgaimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_1
- update by mgaimport

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.5.1-alt2_1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Mar 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_1
- added Url

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_1
- new version

