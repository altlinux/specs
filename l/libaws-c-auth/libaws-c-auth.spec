%define        _unpackaged_files_terminate_build 1
%define        oname aws-c-auth

Name:          lib%oname
Version:       0.7.11
Release:       alt1
Group:         Development/C
Summary:       C99 library implementation of AWS client-side authentication
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-auth
Vcs:           https://github.com/awslabs/aws-c-auth.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: libaws-c-common-devel
BuildRequires: libaws-c-sdkutils-devel
BuildRequires: libaws-c-cal-devel
BuildRequires: libaws-c-http-devel

%description
C99 library implementation of AWS client-side authentication: standard
credentials providers and signing.


%package       devel
Group:         Development/C
Summary:       C99 library implementation of AWS client-side authentication development files
Requires:      cmake
Requires:      libaws-c-common-devel
Requires:      libaws-c-sdkutils-devel
Requires:      libaws-c-cal-devel
Requires:      libaws-c-http-devel

%description   devel
Development headers and libraries for %oname.

C99 library implementation of AWS client-side authentication: standard
credentials providers and signing.


%prep
%setup
%autopatch

%build
%cmake_insource \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_TESTING=ON

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
%_includedir/aws/auth


%changelog
* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.11-alt1
- Initial build v0.7.11 for Sisyphus
