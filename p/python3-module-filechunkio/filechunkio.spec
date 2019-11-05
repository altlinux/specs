%define _unpackaged_files_terminate_build 1
%define oname filechunkio

Name: python3-module-%oname
Version: 1.8
Release: alt2

Summary: FileChunkIO represents a chunk of an OS-level file containing bytes data
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/filechunkio/
BuildArch: noarch

Source0: https://pypi.python.org/packages/10/4d/1789767002fa666fcf486889e8f6a2a90784290be9c0bc28d627efba401e/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
FileChunkIO represents a chunk of an OS-level file containing bytes
data. Python 2.6+ is required.

BACKGROUND: I wrote FileChunkIO to upload huge files to Amazon S3 in
multiple parts without having to split them physically upfront (which
requires more time and twice the disk space) or creating in-memory
chunks as StringIO instances.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
FileChunkIO represents a chunk of an OS-level file containing bytes
data. Python 2.6+ is required.

BACKGROUND: I wrote FileChunkIO to upload huge files to Amazon S3 in
multiple parts without having to split them physically upfront (which
requires more time and twice the disk space) or creating in-memory
chunks as StringIO instances.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 %oname/tests.py  -v

%files
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.8-alt2
- disable python2

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6-alt1.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Initial build for Sisyphus

