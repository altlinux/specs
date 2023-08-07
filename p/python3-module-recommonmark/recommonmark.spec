%define _unpackaged_files_terminate_build 1
%global pypi_name recommonmark

# test suite is failing https://github.com/readthedocs/recommonmark/issues/219
# upstream will not fix it.
%def_without check
Name: python3-module-%pypi_name
Version: 0.7.1
Release: alt1

Summary: A markdown parser for docutils
License: MIT
Group: Development/Python3
Url: https://github.com/readthedocs/recommonmark
BuildArch: noarch

Packager: L.A. Kostis <lakostis@altlinux.ru>

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(commonmark)
BuildRequires: python3(docutils)
BuildRequires: python3(sphinx)
BuildRequires: python3(sphinx_rtd_theme)
%endif

Conflicts: python-module-recommonmark

%description
A docutils-compatibility bridge to CommonMark.
This allows you to write CommonMark inside of Docutils & Sphinx projects.

Warning: recommonmark is now deprecated. Please use python3-module-myst-parser instead.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/%pypi_name/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 07 2023 L.A. Kostis <lakostis@altlinux.ru> 0.7.1-alt1
- 0.7.1.
- package is still needed until llvm migrate to myst_parser.
- .spec: modernize.
- put a note about project deprecation in favour of myst_parser.

* Tue May 19 2020 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1.2
- NMU: conflicts with python-module-recommonmark due to executables.

* Tue Feb 11 2020 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1.1
- NMU: rebuild with python3-module-commonmark.

* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.0-alt1
- Version updated to 0.6.0
- porting on python3.

* Mon Feb 04 2019 L.A. Kostis <lakostis@altlinux.ru> 0.5.0-alt0.1
- Initial build for ALTLinux.
