%define oname alsaaudio

Name: python3-module-%oname
Version: 0.11.0
Release: alt1

Summary: Wrapper for accessing the ALSA API from Python

License: PSF
Group: Development/Python3
URL: https://pypi.org/project/pyalsaaudio
VCS: https://github.com/larsimmisch/pyalsaaudio

Source: %name-%version.tar

BuildRequires: libalsa-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
This package contains wrappers for accessing the ALSA API from Python. It
is currently fairly complete for PCM devices and Mixer access. MIDI
sequencer support is low on our priority list, but volunteers are welcome.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/%oname.cpython-*.so
%python3_sitelibdir/py%oname-%version.dist-info

%changelog
* Fri May 31 2024 Grigory Ustinov <grenka@altlinux.org> 0.11.0-alt1
- Automatically updated to 0.11.0.

* Thu May 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.10.0-alt1
- Automatically updated to 0.10.0.

* Sat Sep 17 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.2-alt1
- Build new version.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.4-alt2
- Drop python2 support.

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- build new version

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 26 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt1.1
- Rebuild with Python-3.3

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Verson 0.7 (ALT #27183)
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.1
- Rebuilt with python 2.6

* Fri Jan 09 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- write spec from scratch, new version

* Mon Jan 28 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt2.1.1
- Rebuilt with python-2.5.

* Mon Jan 28 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt2.1
- Remove python version from the package name.

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.1-alt1.1
- Rebuilt with python-2.4.

* Sun Dec 05 2004 Ivan Fedorov <ns@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux
