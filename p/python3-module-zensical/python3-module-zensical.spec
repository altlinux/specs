%define _unpackaged_files_terminate_build 1
%define pypi_name zensical

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.46
Release: alt1

Summary: A modern static site generator by the Material for MkDocs team
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/zensical/
VCS: https://github.com/zensical/zensical

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-maturin

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-markdown
BuildRequires: python3-module-pymdown-extensions
BuildRequires: python3-module-deepmerge
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-tomli
BuildRequires: python3-module-pandas
BuildRequires: python3-module-tabulate
BuildRequires: python3-module-click
BuildRequires: python3-module-lxml
%endif

%description
Write your documentation in Markdown and create a professional static
site for your Open Source or commercial project in minutes - searchable,
customizable, more than 60 languages, for all devices.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE2 .cargo/config.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --import-mode=importlib

%files
%_bindir/zensical
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 01 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.46-alt1
- Updated to 0.0.46.

* Wed May 27 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.43-alt1
- Updated to 0.0.43.

* Wed May 06 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.40-alt1
- Updated to 0.0.40.

* Tue Mar 31 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.30-alt1
- Updated to 0.0.30.

* Thu Mar 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.29-alt1
- Updated to 0.0.29.

* Mon Mar 23 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.28-alt1
- Packaged for ALT Sisyphus.
