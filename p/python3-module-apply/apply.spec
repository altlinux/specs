%define oname apply

Name: python3-module-%oname
Version: 1.5
Release: alt1

Summary: An apply function for Python 2 and 3.
License: BSD
Group: Development/Python3
Url: https://github.com/stefanholek/apply
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
%summary

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %version-%release

%description tests
An apply function for Python 2 and 3.

This package contains tests for %oname.

%package docs
Summary: Docs for %oname
Group: Development/Python3
Requires: %name = %version-%release

%description docs
An apply function for Python 2 and 3.

This package contains docs for %oname.

%prep
%setup

sed -i 's|../bin/sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs html

%files
%doc *.rst LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests/

%files tests
%python3_sitelibdir/%oname/tests/

%files docs
%doc docs/_build/html


%changelog
* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5-alt1
- Initial build.

