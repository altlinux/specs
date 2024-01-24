%define        _unpackaged_files_terminate_build 1
%define        oname aws-c-event-stream

Name:          lib%oname
Version:       0.4.0
Release:       alt1
Group:         Development/C
Summary:       C99 implementation of the vnd.amazon.eventstream content-type
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-event-stream
Vcs:           https://github.com/awslabs/aws-c-event-stream.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: libaws-c-common-devel
BuildRequires: libaws-c-cal-devel
BuildRequires: libaws-c-io-devel
BuildRequires: libaws-checksums-devel
BuildRequires: libs2n-devel

%description
C99 implementation of the vnd.amazon.event-stream content-type.

%package       devel
Group:         Development/C
Summary:       C99 implementation of the vnd.amazon.eventstream content-type development files

%description   devel
Development headers and libraries for %oname.

C99 implementation of the vnd.amazon.event-stream content-type.


%prep
%setup
%autopatch

%build
%cmake_insource \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_TESTING=ON

%cmake_build

%install
%cmakeinstall_std

%check
%make test


%files
%doc README*
%_libdir/%name.so.*

%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%oname
%_includedir/aws/event-stream


%changelog
* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- Initial build v0.4.0 for Sisyphus
