%define oname storages

Name: python3-module-%oname
Version: 0.1
Release: alt2

Summary: Storages: Abstract File Storage
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/storages/
# https://github.com/dstufft/storages.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Storages: Abstract File Storage

%prep
%setup

## py2 -> py3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
##

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt1.dev1.git20120719.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.dev1.git20120719.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.dev1.git20120719
- Initial build for Sisyphus

