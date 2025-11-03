Name: unordered_dense
Version: 4.8.1
Release: alt1

Summary: A fast & densely stored hashmap and hashset based on robin-hood backward shift deletion for C++17 and later.
License: MIT
Group: Development/C++

Url: https://github.com/martinus/%name
Vcs: https://github.com/martinus/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/martinus/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++

%description
A fast & densely stored hashmap and hashset based on robin-hood backward shift deletion for C++17 and later.

The classes ankerl::unordered_dense::map and ankerl::unordered_dense::set are (almost) drop-in replacements of std::unordered_map and std::unordered_set. While they don't have as strong iterator / reference stability guaranties, they are typically much faster.

Additionally, there are ankerl::unordered_dense::segmented_map and ankerl::unordered_dense::segmented_set with lower peak memory usage. and stable iterator/references on insert.

%package -n lib%name-devel
Summary: A fast & densely stored hashmap and hashset based on robin-hood backward shift deletion for C++17 and later.
Group: Development/C++

%description -n lib%name-devel
A fast & densely stored hashmap and hashset based on robin-hood backward shift deletion for C++17 and later.

The classes ankerl::unordered_dense::map and ankerl::unordered_dense::set are (almost) drop-in replacements of std::unordered_map and std::unordered_set. While they don't have as strong iterator / reference stability guaranties, they are typically much faster.

Additionally, there are ankerl::unordered_dense::segmented_map and ankerl::unordered_dense::segmented_set with lower peak memory usage. and stable iterator/references on insert.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name-devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%_includedir/ankerl
%_cmakedir/%name

%changelog
* Mon Nov 03 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.1-alt1
- New version 4.8.1.

* Mon Oct 27 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.0-alt1
- New version 4.8.0.

* Sat Oct 11 2025 Nazarov Denis <nenderus@altlinux.org> 4.7.0-alt1
- New version 4.7.0.

* Thu Oct 09 2025 Nazarov Denis <nenderus@altlinux.org> 4.6.0-alt1
- New version 4.6.0.

* Mon Aug 25 2025 Nazarov Denis <nenderus@altlinux.org> 4.5.0-alt1
- Initial build for ALTLinux
