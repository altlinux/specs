%def_disable   check
%def_enable    devel
%{?!_disable_devel:%define _unpackaged_files_terminate_build 1}
%define        nomen aws-c-event-stream

Name:          lib%nomen
Version:       1.0.0
Release:       alt1
Group:         Development/C
Summary:       C99 implementation of the vnd.amazon.eventstream content-type
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-event-stream
Vcs:           https://github.com/awslabs/aws-c-event-stream.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: clang
BuildRequires: cmake(aws-c-common)
BuildRequires: cmake(aws-c-cal)
BuildRequires: cmake(aws-c-io)
BuildRequires: cmake(aws-checksums)
BuildRequires: cmake(s2n)

%description
C99 implementation of the vnd.amazon.event-stream content-type.

%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       C99 implementation of the vnd.amazon.eventstream content-type development files
Requires:      ctest
Requires:      cmake
Requires:      clang
Requires:      cmake(aws-c-common)
Requires:      cmake(aws-c-cal)
Requires:      cmake(aws-c-io)
Requires:      cmake(aws-checksums)
Requires:      cmake(s2n)

%description   devel
Development headers and libraries for %nomen.

C99 implementation of the vnd.amazon.event-stream content-type.
%endif


%prep
%setup
%autopatch

%build
%cmake \
%{?!_disable_check:-DBUILD_TESTING=ON} \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DCMAKE_C_COMPILER=clang \
   -DBUILD_SHARED_LIBS=ON \
   %nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest


%files
%doc README*
%_libdir/%name.so.*

%if_enabled    devel
%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%nomen
%_includedir/aws/event-stream
%endif


%changelog
* Thu Oct 08 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.4.0 -> 1.0.0

* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- Initial build v0.4.0 for Sisyphus
