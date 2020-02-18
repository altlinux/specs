%define _unpackaged_files_terminate_build 1
%define oname lexicon

%def_with check

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: Powerful Python dict subclass(es) providing aliasing & attribute access
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/bitprophet/lexicon

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-six
%endif


%description
Lexicon is a simple Python 2.6+ and 3.3+ compatible collection of dict subclasses
providing extra power.

%package tests
Summary: Tests for %oname.
Group: Development/Python3
%py3_requires %oname

%description tests
Lexicon is a simple Python 2.6+ and 3.3+ compatible collection of dict subclasses
providing extra power.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

install -d %buildroot%python3_sitelibdir/%oname/tests
cp -fR tests/* %buildroot%python3_sitelibdir/%oname/tests

%check
%__python3 setup.py test

%files
%doc LICENSE README.md CHANGES
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%oname/tests/

%files tests
%python3_sitelibdir/%oname/tests/


%changelog
* Tue Feb 18 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt1
- Initial build.

