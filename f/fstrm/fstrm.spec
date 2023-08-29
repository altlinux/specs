Group: Development/C
%define _unpackaged_files_terminate_build 1
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name fstrm
%define version 0.6.1
%global _hardened_build 1
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name: fstrm
Summary: Frame Streams implementation in C
Version: 0.6.1
Release: alt1_8
License: MIT AND NTP
URL: https://github.com/farsightsec/fstrm
Source0: https://dl.farsightsecurity.com/dist/%{name}/%{name}-%{version}.tar.gz
# Patches to libmy library
# https://github.com/farsightsec/libmy/pull/4
Patch1: fstrm-0.6.1-Fix-deadcode-and-check-return-code.patch
Patch2: fstrm-0.6.1-Invalid-dereference.patch
Patch3: fstrm-0.6.1-Possible-resource-leak-fix.patch
Patch4: fstrm-0.6.1-Fix-CLANG_WARNING.patch
BuildRequires: autoconf automake libtool
BuildRequires: libevent-devel
# Upstream repository without a single release
# https://github.com/farsightsec/libmy
# Always included as sources copy in farsightsec projects
Provides: bundled(libmy)
Source44: import.info

%description
Frame Streams is a light weight, binary clean protocol that allows for the
transport of arbitrarily encoded data payload sequences with minimal framing
overhead -- just four bytes per data frame. Frame Streams does not specify
an encoding format for data frames and can be used with any data serialization
format that produces byte sequences, such as Protocol Buffers, XML, JSON,
MessagePack, YAML, etc.

%package -n libfstrm0
Summary:        Shared library for the %name library
Group:          System/Libraries

%description -n libfstrm0
Frame Streams is a light weight, binary clean protocol that allows for the
transport of arbitrarily encoded data payload sequences with minimal framing
overhead -- just four bytes per data frame. Frame Streams does not specify
an encoding format for data frames and can be used with any data serialization
format that produces byte sequences, such as Protocol Buffers, XML, JSON,
MessagePack, YAML, etc.

This package contains the shared library.

%package utils
Group: Development/C
Summary: Frame Streams (fstrm) utilities
Requires: libfstrm0 = %EVR

%description utils
Frame Streams is a light weight, binary clean protocol that allows for the
transport of arbitrarily encoded data payload sequences with minimal framing
overhead -- just four bytes per data frame. Frame Streams does not specify
an encoding format for data frames and can be used with any data serialization
format that produces byte sequences, such as Protocol Buffers, XML, JSON,
MessagePack, YAML, etc.

The fstrm-utils package contains command line utilities.

%package -n libfstrm-devel
Group: Development/C
Summary: Development Files for fstrm library
Requires: libfstrm0 = %EVR
Provides: %name-devel = %EVR

%description -n libfstrm-devel
The fstrm-devel package contains header files required to build an application
using fstrm library.

%package doc
Group: Development/C
Summary: API documentation for fstrm library
BuildArch: noarch
BuildRequires: doxygen
Requires: libfstrm0 = %EVR

%description doc
The fstrm-doc package contains Doxygen generated API documentation for
fstrm library.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# regenerated build scripts to:
# - remove RPATHs
# - allow dynamic linking and execution of 'make check'
autoreconf -fi

%build
%configure --disable-static
%make_build
make html

%install
# install the library
%makeinstall_std
rm %{buildroot}%{_libdir}/libfstrm.la

# install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}/
cp -ar html %{buildroot}%{_docdir}/%{name}/html

%check
make check

%if 0%{?fedora} || 0%{?rhel} > 7
# https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets
%else
%endif
%files -n libfstrm0
%exclude %{_docdir}/%{name}/html
%doc COPYRIGHT LICENSE
%_libdir/libfstrm.so.0
%_libdir/libfstrm.so.0.*

%files utils
%{_bindir}/fstrm_capture
%{_bindir}/fstrm_dump
%{_bindir}/fstrm_replay
%{_mandir}/man1/fstrm_*

%files -n libfstrm-devel
%doc README.md
%{_includedir}/fstrm.h
%{_includedir}/fstrm/
%{_libdir}/pkgconfig/libfstrm.pc
%{_libdir}/libfstrm.so

%files doc
%doc %{_docdir}/%{name}/html

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.6.1-alt1_8
- update to new release by fcimport

* Thu Apr 15 2021 Igor Vlasenko <viy@altlinux.org> 0.6.1-alt1_2
- update to new release by fcimport

* Sun Nov 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_3
- new version

