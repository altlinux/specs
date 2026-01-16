Name: ocaml-inifiles
Version: 2.0
Release: alt1
Summary: An ini file parser
Group: Development/ML
License: LGPL-2.1-or-later
Url: https://github.com/ahrefs/inifiles
VCS: https://github.com/ahrefs/inifiles,git
Source0: %name-%version.tar

BuildRequires: ocaml
BuildRequires: dune >= 3.13

BuildRequires: ocaml-pcre2-devel
BuildRequires: ocaml-menhir >= 20180528

%description
An ini file parser

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p inifiles

%install
%dune_install inifiles

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Fri Jan 16 2026 Anton Farygin <rider@altlinux.org> 2.0-alt1
- Initial build for ALT Linux.

