%define _name gumbo-parser
%def_with docs
%def_with python

%define soname 2

Name: libgumbo
Version: 0.12.1
Release: alt2.g1440b18

Summary: An HTML5 parsing library
License: Apache-2.0
Group: System/Libraries

Url: https://codeberg.org/gumbo-parser/gumbo-parser
Vcs: https://codeberg.org/gumbo-parser/gumbo-parser.git
Source: %_name-%version.tar
Patch: %_name-%version-%release.patch

BuildRequires: gcc-c++

%{?_with_python:BuildRequires: python3-devel python3-module-setuptools}
%{?!_without_check:%{?!_disable_check:BuildRequires: libgtest-devel}}

%{?_with_docs:BuildRequires: doxygen}

%define _unpackaged_files_terminate_build 1

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented as
a pure C99 library with no outside dependencies.
It's designed to serve as a building block for other tools and libraries such as
linters, validators, templating languages, and refactoring and analysis tools.

%package -n %name%soname
Summary: %summary
Group: System/Libraries

%description -n %name%soname
Gumbo is an implementation of the HTML5 parsing algorithm implemented as
a pure C99 library with no outside dependencies.
It's designed to serve as a building block for other tools and libraries such as
linters, validators, templating languages, and refactoring and analysis tools.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%soname = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name.

%if_with docs
%package devel-doc
Summary: Development files for %name
Group: Development/C
Conflicts: %name-devel < %version
BuildArch: noarch

%description devel-doc
This package contains development documentation for %name.
%endif

%if_with python
%package -n python3-module-gumbo
Summary: Python3 bindings to %name
Group: Development/Python3
Requires: %name%soname = %version-%release
BuildArch: noarch

%add_python3_self_prov_path %buildroot%python3_sitelibdir_noarch

%description -n python3-module-gumbo
This package contains a module that permits applications
written in the Python3 programming language to use the interface
supplied by %name.
%endif

%prep
%setup -n %_name-%version
%patch -p1

%build
# Remove python tests:
# otherwise they will be installed
find python/ -name '*_test.py' -delete
%autoreconf
%configure \
    --disable-static
%make_build

%if_with docs
doxygen Doxyfile
%endif

%if_with python
%python3_build
%endif

%install
%makeinstall_std

%if_with docs
install -m 755 -d %buildroot%_man3dir/
install -m 644 docs/man/man3/*.3 %buildroot%_man3dir/
%endif

%if_with python
%python3_install
%endif

%check
make check

%files -n %name%soname
%_libdir/%name.so.%soname
%_libdir/%name.so.%soname.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%if_with docs
%files devel-doc
%doc docs/html/ doc/COPYING doc/*.md
%_man3dir/*
%endif

%if_with python
%files -n python3-module-gumbo
%python3_sitelibdir_noarch/*
%endif

%changelog
* Tue Oct 15 2024 Mikhail Efremov <sem@altlinux.org> 0.12.1-alt2.g1440b18
- Updated Url and Vcs tags.
- Upstream git snapshot (fixed potential segfault).

* Wed Nov 22 2023 Mikhail Efremov <sem@altlinux.org> 0.12.1-alt1
- Added Vcs tag.
- Updated url tag.
- Don't use rpm-build-licenses.
- Updated to 0.12.1.

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.10.1-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Sat Aug 31 2019 Michael Shigorin <mike@altlinux.org> 0.10.1-alt2
- Fixed build without check (gcc-c++ is requisite).

* Tue Jul 30 2019 Mikhail Efremov <sem@altlinux.org> 0.10.1-alt1
- Patches from Debain.
- Patch from upstream.
- Initial build.
