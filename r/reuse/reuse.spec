%define _unpackaged_files_terminate_build 1
%def_with check

Name: reuse
Version: 5.1.1
Release: alt1

Summary: tool for REUSE copyright and license recommendations
License: Apache-2.0 AND CC0-1.0 AND CC-BY-SA-4.0 AND GPL-3.0-or-later
Group: Development/Python3
URL: https://github.com/fsfe/reuse-tool

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3(poetry)
BuildRequires: python3(poetry.core)
BuildRequires: /usr/bin/poetry
BuildRequires: /usr/bin/sphinx-build
BuildRequires: python3(myst_parser)
BuildRequires: python3(sphinxcontrib.apidoc)

%if_with check
BuildRequires: python3(attrs)
BuildRequires: python3(binaryornot)
BuildRequires: python3(boolean)
BuildRequires: python3(click)
BuildRequires: python3(license-expression)
BuildRequires: python3(debian)
%endif

# FIXME?
#BuildArch: noarch

Source: %name-%version.tar

%description
Managing copyright and licensing is difficult, especially when reusing
software from different projects that are released under various 
different licenses. REUSE was started by the Free Software Foundation 
Europe (FSFE) to provide a set of recommendations to make licensing your
Free Software projects easier. Not only do these recommendations make it
easier for you to declare the licenses under which your works are 
released, but they also make it easier for a computer to understand how
your project is licensed.

This package contains a tool for checking and helping with compliance
with the REUSE recommendations.

%prep
%setup -n %name-%version

%build
%pyproject_build
make -C docs man

%install
%pyproject_install
install -D -m 0644 docs/_build/man/*.1 -t "%{buildroot}%{_man1dir}/"

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%_bindir/%name
%_man1dir/*
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}


%changelog
* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 5.1.1-alt1
- New version 5.1.1.

* Sun Jun 01 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.2-alt1
- Initial build for Sisyphus
