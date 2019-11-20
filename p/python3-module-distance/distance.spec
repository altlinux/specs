%define oname distance

Name: python3-module-%oname
Version: 0.1.3
Release: alt2

Summary: Utilities for comparing sequences
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/Distance/
# https://github.com/doukremt/distance.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
This package provides helpers for computing similarities between
arbitrary sequences. Included metrics are Levenshtein, Hamming, Jaccard,
and Sorensen distance, plus some bonuses. All distance computations are
implemented in pure Python, and most of them are also implemented in C.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing

%python3_build_debug prepare --with-c
%python3_build_debug --with-c

%install
%python3_install --with-c

%files
%doc *.md tests
%python3_sitelibdir/*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.3-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt1.git20131122.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.git20131122.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1.git20131122.1
- NMU: Use buildreq for BR.

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20131122
- Initial build for Sisyphus

