%define _unpackaged_files_terminate_build 1
%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

%def_enable check
%_python3_set_noarch

%define oname alt_releases_matrix

Name: alt-releases-matrix
Version: 0.2.6
Release: alt1

Summary: A comprehensive, cross-language set of constants and definitions related to ALT Linux repositories and distributions
License: LGPLv2.1+
Group: Development/Other
URL: https://altlinux.space/ALTLinux/alt-releases-matrix
VCS: https://altlinux.space/ALTLinux/alt-releases-matrix.git

Source: %name-%version.tar
Patch1: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-nodejs
BuildRequires: golang
BuildRequires: rustfmt
BuildRequires: clang-tools
BuildRequires: ocaml
BuildRequires: dune
BuildRequires: ocaml-ocamlformat
BuildRequires: shfmt
BuildRequires: python3-module-black
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-yaml

%if_enabled check
BuildRequires: python3-module-pytest
%endif

%description
This project provides a comprehensive, cross-language set of constants and 
definitions related to ALT Linux repositories and distributions, offering 
developers native representations for multiple programming languages.

%package devel
BuildArch: noarch
Summary: C header-only library from %name
Group: Development/C

%description devel
Package contains a header-only C library with data definitions from from %name.

%package -n python3-module-%oname
BuildArch: noarch
Summary: Python library form %name
Group: Development/Python3

%description -n python3-module-%oname
Package contains a Python library with data definitions from from %name.

%package -n node-%name-js
BuildArch: noarch
Summary: JavaScript library form %name
Group: Development/Other

%description -n node-%name-js
Package contains a JavaScript library with data definitions from from %name.

%package -n node-%name-ts
BuildArch: noarch
Summary: TypeScript library form %name
Group: Development/Other

%description -n node-%name-ts
Package contains a typeScript library with data definitions from from %name.

%package -n ocaml-%name
Summary: OCaml library from %name
Group: Development/ML

%description -n ocaml-%name
Package contains an OCaml library with data definitions from %name.

%package -n ocaml-%name-devel
Summary: OCaml library from %name
Requires: ocaml-%name = %EVR
Group: Development/ML

%description -n ocaml-%name-devel
Package contains development files for an OCaml library with data
definitions from %name.

%prep
%setup
%autopatch -p1

%build
BUILD_BRANCH=%altbranch make all

%check
python3 -m pytest -vra tests

%install
# main package files
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/%name/lib
cp -r data/ %buildroot%_datadir/%name/
cp -r generated/bash %buildroot%_datadir/%name/lib
cp -r generated/go %buildroot%_datadir/%name/lib
cp -r generated/rust %buildroot%_datadir/%name/lib
# C library files
mkdir -p %buildroot%_includedir/%name
cp generated/c/%oname.h %buildroot%_includedir/%name
# Python library files
install -Dm0644 generated/python/%oname.py %buildroot%python3_sitelibdir/%oname.py
# JavaScript library files
mkdir -p %buildroot%nodejs_sitelib/%name-js
cp -r generated/javascript/* %buildroot%nodejs_sitelib/%name-js
# TypeScript library files
mkdir -p %buildroot%nodejs_sitelib/%name-ts
cp -r generated/typescript/* %buildroot%nodejs_sitelib/%name-ts
# OCaml library files
pushd generated/ocaml
%dune_install
popd

%files
%dir %_datadir/%name
%doc CHANGELOG.md README.md LICENSE
%_datadir/%name/*

%files devel
%dir %_includedir/%name
%_includedir/%name/%oname.h

%files -n python3-module-%oname
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/*

%files -n node-%name-js
%dir %nodejs_sitelib/%name-js
%nodejs_sitelib/%name-js/*

%files -n node-%name-ts
%dir %nodejs_sitelib/%name-ts
%nodejs_sitelib/%name-ts/*

%files -n ocaml-%name-devel -f generated/ocaml/ocaml-files.devel
%files -n ocaml-%name -f generated/ocaml/ocaml-files.runtime

%changelog
* Thu Jun 11 2026 Danil Shein <dshein@altlinux.org> 0.2.6-alt1
- new version

* Thu May 07 2026 Danil Shein <dshein@altlinux.org> 0.2.5-alt1
- new version

* Mon Apr 06 2026 Danil Shein <dshein@altlinux.org> 0.2.4-alt1
- new version

* Mon Jan 19 2026 Danil Shein <dshein@altlinux.org> 0.2.3-alt1
- new version

* Wed Jan 14 2026 Danil Shein <dshein@altlinux.org> 0.2.2-alt1
- changed library license: GPLv3 => LGPLv2.1+ 

* Fri Dec 26 2025 Danil Shein <dshein@altlinux.org> 0.2.1-alt1
- added bash library generation support
- data: removed discontinued branches from active list:
  sisyphus_mipsel, p9_e2k, p9_mipsel, c10f1, c9f1
- ocaml: added active_branches list for iteration over branch names

* Wed Dec 24 2025 Anton Farygin <rider@altlinux.org> 0.2.0-alt1
- Added ocaml-alt-release-matrix library for OCaml

* Tue Aug 26 2025 Danil Shein <dshein@altlinux.org> 0.1.1-alt1
- new version

* Thu Aug 07 2025 Danil Shein <dshein@altlinux.org> 0.1.0-alt1
- new version

* Wed Aug 06 2025 Danil Shein <dshein@altlinux.org> 0.0.4-alt1
- Initial build for ALT.

