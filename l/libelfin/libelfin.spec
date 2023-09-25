Name: libelfin
Version: 0.3
Release: alt3

Summary: C++11 library for reading ELF binaries and DWARFv4 debug information.
License: GPL
Group: Terminals

Url: https://github.com/aclements/libelfin
Source: %name-%version.tar

# Automatically added by buildreq on Sat Oct 17 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel python-modules python2-base python3 python3-base python3-dev sh4 tzdata
BuildRequires: gcc-c++ python3-module-mpl_toolkits selinux-policy-alt

%package devel
Summary: Development files for programs which will use the Elfin library
Summary(ru_RU.UTF-8): Заголовочные файлы для программ, использующих библиотеку Elfin
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: Static Elfin library
Summary(ru_RU.UTF-8): Версия библиотеки Elfin для статического связывания
Group: Development/C
Requires: %name-devel = %version-%release

%description
Native C++11 code and interface, designed from scratch to interact well
with C++11 features, from range-based for loops to move semantics
to enum classes.

It's not production-ready and there are many parts of the DWARF specification
it does not yet implement, but it's complete enough to be useful for many
things and is a good deal more pleasant to use than every other debug
info library I've tried (author).

%description devel
This package includes development files necessary for developing programs
which use Elfin library.

%description -l ru_RU.UTF-8 devel
Этот пакет содержит заголовочные файлы для библиотеки Elfin.

%description devel-static
This package includes static library necessary for developing statically
which use Elfin library.

%description -l ru_RU.UTF-8 devel-static
Этот пакет содержит версию библиотеки Elfin для статического связывания.

%prep
%setup
%ifarch %e2k
# lcc 1.25.23 ftbfs workaround
sed -i 's,-Werror,& -Wno-error=return-type,g' */Makefile
%endif

%build
%make PREFIX=%_exec_prefix LIBDIR=/%_lib MANPREFIX=%_mandir

%install
%define docdir %_docdir/%name-%version

%makeinstall_std LIBDIR=/%_lib PREFIX=%_exec_prefix MANPREFIX=%_mandir

mkdir -p %buildroot%docdir
install -pm644 README.md %buildroot%docdir/
install -pm644 LICENSE %buildroot%docdir/
mkdir -p %buildroot%docdir/examples
install -pm644 examples/* %buildroot%docdir/examples/

%find_lang %name

%files
%_libdir/*.so.*
%_libdir/pkgconfig/*

%dir %docdir
%docdir/*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Mon Sep 25 2023 Artyom Bystrov <arbars@altlinux.org> 0.3-alt3
- Fix FTBFS.

* Fri Oct 28 2022 Michael Shigorin <mike@altlinux.org> 0.3-alt2
- E2K: lcc 1.25.23 ftbfs workaround.
- Minor spec cleanup.

* Sat Oct 17 2020 Andrey Bergman <vkni@altlinux.org> 0.3-alt1
- Initial release for Sisyphus.
