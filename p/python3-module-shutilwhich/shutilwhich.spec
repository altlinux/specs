%define _unpackaged_files_terminate_build 1
%define oname shutilwhich

Name: python3-module-%oname
Version: 1.1.0
Release: alt3
Summary: shutil.which for those not using Python 3.3 yet
License: PSF
Group: Development/Python3
Url: https://pypi.python.org/pypi/shutilwhich/
BuildArch: noarch

# https://github.com/mbr/shutilwhich.git
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
A copy & paste backport of Python 3.3's shutil.which function.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt3
- Drop python2 support.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt2
- Rebuilt to fix file permissions.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2.git20130302.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.git20130302
- Added provides %oname

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20130302
- Initial build for Sisyphus

