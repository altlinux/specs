BuildRequires: rpm-build-mingw32
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-libp11
Version:        0.2.8
Release:        alt1_1
Summary:        MingGW Windows libp11 library

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.opensc-project.org/libp11
Source0:        http://www.opensc-project.org/files/libp11/libp11-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 53
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libltdl
BuildRequires:  mingw32-openssl
BuildRequires:  pkgconfig

Requires:       pkgconfig
Source44: import.info


%description
Libp11 is a library implementing a small layer on top of PKCS#11 API to
make using PKCS#11 implementations easier.

This is the MinGW cross-compiled Windows library.


%{?_mingw32_debug_package}


%prep
%setup -q -n libp11-%{version}


%build
%{_mingw32_configure} --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Remove documentation from a wrong place.
# We install it with %%doc instead.
rm -rf $RPM_BUILD_ROOT%{_mingw32_docdir}/libp11


%files
%doc COPYING NEWS
%{_mingw32_bindir}/libp11-2.dll
%{_mingw32_libdir}/libp11-2.dll.def
%{_mingw32_libdir}/libp11.dll.a
%{_mingw32_libdir}/libp11.la
%{_mingw32_libdir}/pkgconfig/*
%{_mingw32_includedir}/*


%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.8-alt1_1
- initial release by fcimport

