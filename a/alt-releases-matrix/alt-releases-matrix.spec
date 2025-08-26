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

%define oname alt_releases_matrix

Name: alt-releases-matrix
Version: 0.1.1
Release: alt1

Summary: A comprehensive, cross-language set of constants and definitions related to ALT Linux repositories and distributions
License: GPL-3.0
Group: Development/Other
URL: https://altlinux.space/ALTLinux/alt-releases-matrix
VCS: https://altlinux.space/ALTLinux/alt-releases-matrix.git

BuildArch: noarch

Source: %name-%version.tar
Patch1: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-nodejs
BuildRequires: golang
BuildRequires: rustfmt
BuildRequires: clang-tools
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
Summary: C header-only library from %name
Group: Development/C

%description devel
Package contains a header-only C library with data definitions from from %name.

%package -n python3-module-%oname
Summary: Python library form %name
Group: Development/Python3

%description -n python3-module-%oname
Package contains a Python library with data definitions from from %name.

%package -n node-%name-js
Summary: JavaScript library form %name
Group: Development/Other

%description -n node-%name-js
Package contains a JavaScript library with data definitions from from %name.

%package -n node-%name-ts
Summary: TypeScript library form %name
Group: Development/Other

%description -n node-%name-ts
Package contains a typeScript library with data definitions from from %name.


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

%changelog
* Tue Aug 26 2025 Danil Shein <dshein@altlinux.org> 0.1.1-alt1
- new version

* Thu Aug 07 2025 Danil Shein <dshein@altlinux.org> 0.1.0-alt1
- new version

* Wed Aug 06 2025 Danil Shein <dshein@altlinux.org> 0.0.4-alt1
- Initial build for ALT.

