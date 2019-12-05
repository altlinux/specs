%define oname hotqueue

Name:       python3-module-%oname
Version:    0.2.7
Release:    alt2

Summary:    Simple library that allows to use Redis as a message queue.
License:    MIT
Group:      Development/Python3
Url:        https://github.com/richardhenry/hotqueue
BuildArch:  noarch

Source:     %name-%version-%release.tar
Patch:      hotqueye-alt-docs.patch
Patch1:     hotqueye-alt-setuptools.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
HotQueue is a Python library that allows you to use Redis as a message
queue within your Python programs.

%prep
%setup
%patch -p1
%patch1 -p1

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%files
%doc REQUIREMENTS LICENSE README.rst docs/_build/html
%python3_sitelibdir/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.7-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.7-alt1.git20120412.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.7-alt1.git20120412.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1.git20120412.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt1.git20120412
- Version 0.2.7
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.3-alt1.1
- Rebuild with Python-2.7

* Thu Jan 20 2011 Mikhail Pokidko <pma@altlinux.org> 0.2.3-alt1
- initial build

