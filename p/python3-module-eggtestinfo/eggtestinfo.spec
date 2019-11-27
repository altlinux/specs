%define _unpackaged_files_terminate_build 1

%define oname eggtestinfo

Name: python3-module-%oname
Version: 0.3
Release: alt4

Summary: Add test information to .egg-info
License: ZPL
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/eggtestinfo

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
This package is a setuptools plugin: it adds a file to the generated
.egg-info directory, capturing the information used by the setup.py test
command when running tests.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt4
- python2 disabled

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt3
- NMU: rebuilt to regenerate dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt2.1
- NMU: Use buildreq for BR.

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added module for Python 3

* Sat Apr 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

