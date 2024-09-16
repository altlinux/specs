%define libname ppx_yojson_conv_lib
Name: ocaml-%libname
Version: 0.17.0
Release: alt1
Summary: Runtime lib for ppx_yojson_conv
License: MIT
Group: Development/ML
Url: https://github.com/janestreet/ppx_yojson_conv_lib
VCS: https://github.com/janestreet/ppx_yojson_conv_lib
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-yojson-devel

%description
%summary


%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %libname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime


%files devel -f ocaml-files.devel

%changelog
* Fri Sep 13 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- first build for ALT Linux
