%ifnarch %ix86 armh 
%def_with check
%else
%def_without check
%endif
%define modulename bigstringaf
Name: ocaml-%modulename
Version: 0.9.1
Release: alt1
Summary: Bigstring intrinsics and fast blits based on memcpy/memmove
License: BSD-3-Clause
Group: Development/ML
Url: https://github.com/inhabitedtype/bigstringaf
Source: %name-%version.tar
BuildRequires: dune ocaml-dune-configurator-devel
%if_with check
BuildRequires: ocaml-alcotest-devel
%endif

%description
The OCaml compiler has a bunch of intrinsics for Bigstrings, but they're not
widely-known, sometimes misused, and so programs that use Bigstrings are slower
than they have to be. And even if a library got that part right and exposed the
intrinsics properly, the compiler doesn't have any fast blits between
Bigstrings and other string-like types.

So here they are. Go crazy.


%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Tue Mar 30 2021 Anton Farygin <rider@altlinux.org> 0.7.0-alt1
- first build for ALT
