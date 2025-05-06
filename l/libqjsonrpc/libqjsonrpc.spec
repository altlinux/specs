%define _unpackaged_files_terminate_build 1
%set_verify_elf_method unresolved=relaxed

Name: libqjsonrpc
Version: 1.0.0
Release: alt1

Summary: Fork of the original QJsonRpc library with cmake based build.
License: LGPLv2+
Group: Development/C++
Url: https://github.com/august-alt/qjsonrpc

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake cmake-modules gcc-c++
BuildRequires: qt5-base-devel qt5-base-common
BuildRequires: libhttp-parser-devel

Source0: %name-%version.tar

%description
Fork of the original QJsonRpc library with cmake based build.
QJsonRpc is a Qt implementation of the JSON-RPC protocol.
It integrates nicely with Qt, leveraging Qt's meta object system in order
to provide services over the JSON-RPC protocol. QJsonRpc is licensed under
the LGPLv2.1.

%package devel
Summary: QJsonRpc development libraries and header files
Group: Development/C++
Requires: %name = %version-%release
Requires: cmake

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/libqjsonrpc.so.*

%files devel
%doc README.md

%_includedir/qjsonrpc/*.h

%_libdir/libqjsonrpc.so

%_libdir/qjsonrpc/QJSonRPCConfig.cmake

%changelog
* Tue May 6 2025 Vladimir Rubanov <august@altlinux.org> 1.0.0-alt1
- 1.0.0-alt1
- Initial build

