%define oname pebble

Name: python3-module-%oname
Version: 4.5.3
Release: alt2

Summary: Threading and multiprocessing eye-candy
License: LGPLv3
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/Pebble/

# https://github.com/noxdafox/pebble.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest /proc

%py3_provides %oname
%py3_requires multiprocessing


%description
Pebble provides a neat API to manage threads and processes within an
application.

%prep
%setup

# fix python version for python3 tests
grep -q 'python -m pytest' ./test/run-tests.sh && \
sed -i 's/python -m pytest/python3 -m pytest/' ./test/run-tests.sh

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
./test/run-tests.sh
%endif

%files
%doc *.rst doc/*.rst
%python3_sitelibdir/*


%changelog
* Thu Jun 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.5.3-alt2
- Fix build.

* Wed Jun 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.5.3-alt1
- Version updated to 4.5.3.

* Mon Jun 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.5.1-alt2
- Failed test on i586 disabled.

* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.5.1-alt1
- Version updated to 4.5.1.

* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.3.7-alt2
- python2 disabled

* Tue Mar 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.7-alt1.git20180228
- Updated to upstream version 4.3.7.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.3.6-alt2.git20171213.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.6-alt2.git20171213
- Updated runtime dependencies.

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.6-alt1.git20171213
- Updated to upstream version 4.3.6.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.8-alt1.git20140910.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.1.8-alt1.git20140910.1
- NMU: Use buildreq for BR.

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.8-alt1.git20140910
- Initial build for Sisyphus

