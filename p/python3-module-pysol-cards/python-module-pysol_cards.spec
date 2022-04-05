%define  oname pysol_cards

Name:    python3-module-pysol-cards
Version: 0.14.2
Release: alt1

Summary: Python library for dealing cards like PySol FC, MS Freecell/Freecell Pro, or PySol legacy

License: MIT
Group:   Development/Python3
URL:     https://github.com/shlomif/pysol_cards

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

%description
The pysol-cards python modules allow the python developer to generate
the initial deals of some PySol FC games. It also supports PySol legacy
deals and Microsoft FreeCell / Freecell Pro deals.

%prep
%setup
find -name "*.py" | xargs subst 's|random2|random|'
find -name "*.txt" | xargs subst 's|random2|random|'

%build
export PBR_VERSION=%version
%python3_build

%install
export PBR_VERSION=%version
%python3_install
%python3_prune

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 0.14.2-alt1
- new version 0.14.2 (with rpmrb script)

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt1
- build python3 module separately

* Sun Jun 14 2020 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- New version.

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 0.8.18-alt1
- Initial build for Sisyphus.
