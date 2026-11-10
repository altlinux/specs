%define _unpackaged_files_terminate_build 1
%define soversion 1.1

Name: libstudxml
Version: 1.1.0
Release: alt1

Summary: Streaming XML pull parser and serializer for C++
License: MIT
Group: Development/C++
Url: https://www.codesynthesis.com/projects/libstudxml/
VCS: https://git.codesynthesis.com/libstudxml/libstudxml.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: libexpat-devel

%description
libstudxml provides a streaming XML pull parser and serializer for C++11.
It supports XML namespaces, typed values and incremental processing of
XML documents. The parser uses the system Expat library; the serializer
uses the private Genx implementation included by upstream.

%package -n libstudxml%soversion
Summary: libstudxml shared library
Group: System/Libraries

%description -n libstudxml%soversion
libstudxml provides a streaming XML pull parser and serializer for C++11.
It supports XML namespaces, typed values and incremental processing of
XML documents.

This package contains the shared runtime library.

%package -n libstudxml-devel
Summary: Development files for libstudxml
Group: Development/C++
Requires: libstudxml%soversion = %EVR

%description -n libstudxml-devel
This package contains the headers, linker symlink and pkg-config metadata
needed to develop applications using libstudxml.

%prep
%setup
%autopatch -p1
cp libstudxml/details/genx/LICENSE GENX-LICENSE

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n libstudxml%soversion
%doc LICENSE GENX-LICENSE
%_libdir/libstudxml-%soversion.so

%files -n libstudxml-devel
%doc README
%_includedir/libstudxml/
%_libdir/libstudxml.so
%_pkgconfigdir/libstudxml.pc

%changelog
* Tue Nov 10 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.1.0-alt1
- First build for ALT.
