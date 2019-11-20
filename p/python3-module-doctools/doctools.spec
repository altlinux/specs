%define oname doctools

Name: python3-module-%oname
Version: 0.2.2
Release: alt2

Summary: Docblock manipulation utilities
License: BSD3
Group: Development/Python3
Url: https://pypi.python.org/pypi/doctools/
# https://github.com/awagner83/doctools.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest-cov

%py3_provides %oname


%description
doctools - python docblock manipulation utilities.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
sed -i 's|py\.test|py.test3|' runtests.sh
./runtests.sh

%files
%doc LICENSE *.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1.git20110902.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.2-alt1.git20110902.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20110902.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20110902
- Initial build for Sisyphus

