%define modulename graph

Name: python3-module-%modulename
Version: 1.8.1
Release: alt2

Summary: library for working with graphs in Python
License: MIT
Group: Development/Python3
Url: http://code.google.com/p/python-graph/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
Provides: python3-module-pygraph


%description
This software provides a suitable data structure for
representing graphs and a whole set of important algorithms.

%if_with python3
%package -n python3-module-%modulename
Summary: library for working with graphs in Python 3
Group: Development/Python3

%description -n python3-module-%modulename
This software provides a suitable data structure for
representing graphs and a whole set of important algorithms.
%endif

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
pushd core
%python3_build
popd
pushd dot
%python3_build
popd

%install
pushd core
%python3_install
popd
pushd dot
%python3_install
popd

touch %buildroot%python3_sitelibdir/pygraph/__init__.py

# TODO: split to subpackages "core" and "dot"

%files
%doc  Changelog README
%python3_sitelibdir/pygraph
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*.pth


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.8.1-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.8.1-alt1.1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.1-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1.1.1
- NMU: Use buildreq for BR.

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.8.1-alt1.1
- Rebuild with Python-3.3

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Version 1.8.1
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.0-alt2.1
- Rebuild with Python-2.7

* Tue May 18 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7.0-alt2
- Provide python2.6(pygraph).

* Thu May 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus.

