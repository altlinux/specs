%define oname Paver

Name: python3-module-%oname
Version: 1.3.4
Release: alt1

Summary: Easy build, distribution and deployment scripting

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/Paver

# https://github.com/paver/paver.git
Source: %name-%version.tar
Patch:  2d4279a46da414419c507b05afab49b3478bf75b.patch

BuildRequires(pre): rpm-build-python3

%add_python3_req_skip bzrlib bzrlib.builtins

Conflicts: python-module-Paver
Obsoletes: python-module-Paver

BuildArch: noarch

%description
Paver is a Python-based build/distribution/deployment scripting tool
along the lines of Make or Rake. What makes Paver unique is its
integration with commonly used Python libraries. Common tasks that were
easy before remain easy. More importantly, dealing with your
applications specific needs and requirements is also easy.

%prep
%setup
%patch -p1

# currently there is no bzr module for python-3
rm -f paver/bzr.py

%build
%python3_build

%install
%python3_install

# https://github.com/paver/paver/issues/211
rm -f %buildroot/%python3_sitelibdir/paver/deps/path2.py

%files
%doc *.rst
%_bindir/paver
%python3_sitelibdir/paver
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Fri Jun 10 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.4-alt1
- Automatically updated to 1.3.4.

* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.4-alt2
- Drop python2 support.
- Build without docs.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.4-alt1
- Updated to upstream version 1.2.4.
- Disabled bzr module for python-3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.3-alt1.git20140810.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt1.git20140810.1
- NMU: Use buildreq for BR.

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.git20140810
- Initial build for Sisyphus

