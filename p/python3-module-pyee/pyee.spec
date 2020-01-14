%define oname pyee

Name: python3-module-%oname
Version: 6.0.0
Release: alt1

Summary: A port of node.js's EventEmitter to python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyee/
BuildArch: noarch

# https://github.com/jesusabdullah/pyee.git
Source: %name-%version.tar
Patch0: fix-version-detecting.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest-asyncio python3-module-pytest-runner
BuildRequires: python3-module-sphinx

%py3_provides %oname


%description
pyee supplies an event_emitter object that acts similar to the
EventEmitter that comes with node.js.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description tests
pyee supplies an event_emitter object that acts similar to the
EventEmitter that comes with node.js.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
pyee supplies an event_emitter object that acts similar to the
EventEmitter that comes with node.js.

This package contains documentation for %oname

%prep
%setup
%patch -p1

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

touch version.txt
echo '%version' > version.txt

%build
%python3_build_debug

%install
%python3_install

pushd docs/
%make man
install -d %buildroot%_mandir/man1
mv _build/man/* %buildroot%_mandir/man1/
popd

cp -fR tests/ %buildroot%python3_sitelibdir/%oname/

%check
%make tests

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests/

%files tests
%python3_sitelibdir/%oname/tests/

%files docs
%_mandir/man1/*


%changelog
* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 6.0.0-alt1
- Version updated to 6.0.0
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.8-alt1.git20130806.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1.git20130806
- Initial build for Sisyphus

