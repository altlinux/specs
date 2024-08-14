%def_disable snapshot

%define _name libxml++
%define git_name libxmlplusplus
%define ver_major 5.4
%define api_ver 5.0

%def_disable doc
%def_enable check

Name: %{_name}5
Version: %ver_major.0
Release: alt1

Summary: C++ wrapper for the libxml2 XML parser library
Group: System/Libraries
License: LGPL-2.1
Url: https://libxmlplusplus.sourceforge.net/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Vcs: https://github.com/libxmlplusplus/libxmlplusplus.git
Source: %git_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson mm-common gcc-c++
BuildRequires: libglibmm2.68-devel >= 2.68.0
BuildRequires: libxml2-devel >= 2.7.7
%{?_enable_doc:BuildRequires: doxygen graphviz docbook-style-xsl xsltproc}

%description
libxml++ is a C++ wrapper for the libxml2 XML parser library.
It has SAX and DOM-like APIs, but does not attempt to conform exactly to
the DOM specification. Its API is simpler than the underlying libxml2 C API.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
This package contains the headers and libraries for libxml++ development.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C++
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains the development documentation for libxml++ library.

%prep
%setup -n %{?_disable_snapshot:%_name}%{?_enable_snapshot:%git_name}-%version

%build
%{?_enable_snapshot:mm-common-prepare --force --copy}
%meson \
    %{?_enable_snapshot:-Dmaintainer-mode=true \
    %{?_disable_doc:-Dbuild-documentation=false}}
    %{?_enable_doc:-Dbuild-documentation=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%_name-%api_ver.so.*
%doc NEWS README*

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%_name-%api_ver.so
%_libdir/%_name-%api_ver/
%_pkgconfigdir/%_name-%api_ver.pc

%if_enabled docs
%files devel-doc
%_datadir/devhelp/books/%_name-%api_ver/*.devhelp2
%_docdir/%_name-%api_ver/*
%endif

%changelog
* Wed Aug 14 2024 Yuri N. Sedunov <aris@altlinux.org> 5.4.0-alt1
- 5.4.0

* Fri Apr 12 2024 Yuri N. Sedunov <aris@altlinux.org> 5.2.0-alt1
- first build for sisyphus

