%define _unpackaged_files_terminate_build 1
%define oname gearbox

Name: python3-module-%oname
Version: 0.2.2
Release: alt1

Summary: Toolkit born as a PasteScript replacement for the TurboGears2 web framework

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/gearbox

# https://github.com/TurboGears/gearbox.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-cliff
BuildRequires: python3-module-tempita
BuildRequires: python3-module-PasteDeploy
BuildRequires: python3-module-html5lib
BuildRequires: python3-module-hupper

%py3_provides %oname
%py3_requires cliff tempita paste.deploy

%description
gearbox is a paster command replacement for TurboGears2. It has been
created during the process of providing Python3 support to the
TurboGears2 web framework, while still being backward compatible with
the existing TurboGears projects.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%doc *.rst

%changelog
* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt1
- Automatically updated to 0.2.1.

* Sat Oct 26 2019 Grigory Ustinov <grenka@altlinux.org> 0.1.1-alt3
- Build without python2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.7-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20150205
- Initial build for Sisyphus

