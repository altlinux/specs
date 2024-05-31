%define oname crochet

Name: python3-module-%oname
Version: 2.1.1
Release: alt1

Summary: Use Twisted anywhere!

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/crochet
VCS: https://github.com/itamarst/crochet

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-twisted-core-test
BuildRequires: python3-module-wrapt
BuildRequires: python3-module-service-identity
BuildRequires: python3-module-sphinx

%py3_requires twisted.internet

%description
Crochet is an MIT-licensed library that makes it easier to use Twisted
from regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with
  Twisted more cleanly from their threaded parts. For example this can
  be useful when using Twisted as a WSGI container.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-module-twisted-core-test

%description tests
Crochet is an MIT-licensed library that makes it easier to use Twisted
from regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with
  Twisted more cleanly from their threaded parts. For example this can
  be useful when using Twisted as a WSGI container.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Crochet is an MIT-licensed library that makes it easier to use Twisted
from regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
  implementation.
* Port blocking code to Twisted more easily, by keeping a backwards
  compatibility layer.
* Allow normal Twisted programs that use threads to interact with
  Twisted more cleanly from their threaded parts. For example this can
  be useful when using Twisted as a WSGI container.

This package contains pickles for %oname.

%prep
%setup

sed -i 's|sphinx-build|&-3|' docs/Makefile

# hotfix for python3.12
sed -i 's/SafeConfigParser/ConfigParser/' versioneer.py
sed -i 's/readfp/read_file/' versioneer.py
# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: %version\)\"/" \
	%oname/_version.py

%build
%python3_build_debug

%install
%python3_install

%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 -m unittest discover -v ||:

%files
%doc *.rst examples docs/_build/html
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%changelog
* Fri May 31 2024 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt1
- Automatically updated to 2.1.1.

* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt4
- Fixed FTBFS.

* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.9.0-alt3
- Build for python2 disabled.

* Fri Mar 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt2
- Updated build dependencies.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt1
- Updated to upstream version.
- Fixed version in egg-info.
- Explicitely stated egg-info including valid version.

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt1
- Updated to upstream version 1.8.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt1.git20150505.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1.git20150505.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20150505
- Initial build for Sisyphus

