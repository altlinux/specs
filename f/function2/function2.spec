Name:    function2
Version: 4.2.4
Release: alt1

Summary: Improved and configurable drop-in replacement to std::function
License: BSL
Group:   Development/Other
Url:     https://naios.github.io/function2
Vcs:     https://github.com/Naios/function2.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++

%description
%summary
that supports move only types, multiple overloads and more.

%package devel
Summary: %summary
Group: Development/Other

%description devel
%summary
that supports move only types, multiple overloads and more.

%prep
%setup

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install
find %buildroot%prefix -maxdepth 1 \
'(' -iname 'license.txt' -o -iname 'readme.md' ')' -print -delete

%files devel
%doc *.md LICENSE.txt
%_includedir/%name
%_cmakedir/%name

%changelog
* Thu Apr 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 4.2.4-alt1
- Initial build for Sisyphus.
