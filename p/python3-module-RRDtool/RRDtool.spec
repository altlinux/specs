%define oname RRDtool

Name: python3-module-%oname
Version: 0.1.15
Release: alt1

Summary: rrdtool bindings for Python
License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/rrdtool/
# https://github.com/commx/python-rrdtool.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: librrd-devel

%py3_provides rrdtool
Conflicts: python-module-rrd python-module-rrdtool

%description
rrdtool binding for Python 2.6+ and 3.3+.

This bindings are based on the original Python rrdtool bindings from
Hye-Shik Chang and are slightly modified to support Python 3.3+ and 2.6+
in the same code base.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.15-alt1
- Version updated to 0.1.15
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.12-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.12-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jan 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.12-alt1
- Updated to upstream version 0.1.12.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20141011.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.git20141011.1
- NMU: Use buildreq for BR.

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141011
- Initial build for Sisyphus

