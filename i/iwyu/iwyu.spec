Name: iwyu
Version: 0.22
Release: alt1

Summary: C/C++ source files #include analyzer based on clang
License: NCSA
Group: Development/C
Url: https://github.com/include-what-you-use/include-what-you-use

Packager: %packager

BuildRequires: clang18.1-devel llvm18.1-devel cmake gcc-c++ ninja-build rpm-build-python3

Source0: %name-%version-%release.tar

%description
"Include what you use" means this: for every symbol (type, function, variable,
or macro) that you use in foo.cc (or foo.cpp), either foo.cc or foo.h should
include a .h file that exports the declaration of that symbol. (Similarly, for
foo_test.cc, either foo_test.cc or foo.h should do the including.) Obviously
symbols defined in foo.cc itself are excluded from this requirement.

This puts us in a state where every file includes the headers it needs to
declare the symbols that it uses. When every file includes what it uses,
then it is possible to edit any file and remove unused headers, without fear
of accidentally breaking the upwards dependencies of that file. It also
becomes easy to automatically track and update dependencies in the source
code.

%prep
%setup -n %name-%version-%release
sed -e s@lib/@lib\${LLVM_LIBDIR_SUFFIX}/@g -i CMakeLists.txt
#%%py3_shebang_fix *.py

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DIWYU_LLVM_ROOT_PATH=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%_bindir/include-what-you-use
%_bindir/fix_includes.py
%_bindir/iwyu_tool.py
%dir %_datadir/include-what-you-use/
%_datadir/include-what-you-use/*
%_man1dir/include-what-you-use.1*
%docdir *

%changelog
* Fri Jun 21 2024 Andrey Bergman <vkni@altlinux.org> 0.22-alt1
- Update to version 0.22 (Clang 18).

* Sun Feb 18 2024 Andrey Bergman <vkni@altlinux.org> 0.21-alt1
- Initial release for Sisyphus.

