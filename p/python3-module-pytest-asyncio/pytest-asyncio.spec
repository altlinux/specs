%define oname pytest-asyncio

Name: python3-module-%oname
Version: 0.10.0
Release: alt1

Summary: Pytest support for asyncio
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/pytest-dev/pytest-asyncio
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_provides %oname


%description
pyee supplies a BaseEventEmitter object that is similar to the EventEmitter
class from Node.js. It also supplies a number of subclasses with added support
for async and threaded programming in python, such as async/await as seen in
python 3.5+.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description tests
pyee supplies a BaseEventEmitter object that is similar to the EventEmitter
class from Node.js. It also supplies a number of subclasses with added support
for async and threaded programming in python, such as async/await as seen in
python 3.5+.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

cp -fR tests tests/ %buildroot%python3_sitelibdir/pytest_asyncio/

%check
%make tests

%files
%doc *.rst LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/pytest_asyncio/tests

%files tests
%python3_sitelibdir/pytest_asyncio/tests


%changelog
* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus

