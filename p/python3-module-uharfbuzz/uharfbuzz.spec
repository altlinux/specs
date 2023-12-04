%define oname uharfbuzz

%def_with check

Name:     python3-module-%oname
Version:  0.37.3
Release:  alt1

Summary:  An opinionated HarfBuzz Python binding

License:  Apache-2.0
Group:    Development/Python3
Url:      https://pypi.org/project/uharfbuzz

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++
BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Mon Dec 04 2023 Grigory Ustinov <grenka@altlinux.org> 0.37.3-alt1
- Build new version.

* Fri Sep 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.30.0-alt1
- Initial build for Sisyphus.
- Build with bundled libharfbuzz, because aris@ dont want to enable
  experimental api in "his own" system libharfbuzz, and this package
  uses lots of it. See more here: https://bugzilla.altlinux.org/43094
