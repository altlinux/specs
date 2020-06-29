%define  modulename doc8

%def_with docs
%def_with check

Name:    python3-module-%modulename
Version: 0.8.1
Release: alt1

Summary: Style checker for sphinx (or other) rst documentation.

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/openstack/doc8

BuildArch: noarch

Source:  %modulename-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-chardet
BuildRequires: python3-module-docutils
BuildRequires: python3-module-restructuredtext_lint >= 0.7
BuildRequires: python3-module-six
BuildRequires: python3-module-stevedore

%if_with docs
BuildRequires: python3-module-sphinx_rtd_theme
%endif

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-nose
%endif

%description
Doc8 is an opinionated style checker for rst_ (with basic support for
plain text) styles of documentation.

%if_with docs
%package doc
Summary: Documentation for %modulename
Group: Development/Documentation

%description doc
Documentation for %modulename.
%endif

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%if_with docs
export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%check
py.test3 -vv

%files
%_bindir/*
%python3_sitelibdir/*

%if_with docs
%files doc
%doc LICENSE html
%endif

%changelog
* Mon Jun 29 2020 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1
- Build new version.
- Add docs.
- Add check.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt2
- Build without python2.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus.
