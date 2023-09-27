%define oname fabio

# [armh]
# [00:01:02]   File "/usr/src/RPM/BUILD/python3-module-fabio-2023.6/build/lib/python3/site-packages/fabio/test/codecs/test_brukerimage.py", line 155, in test_linear
# [00:01:02]     self.assertTrue(error < numpy.finfo(numpy.float32).eps, "Error is %s>1e-7" % error)
# [00:01:02] AssertionError: False is not true : Error is 1.1920929e-07>1e-7
%ifnarch armh
%def_with check
%else
%def_without check
%endif

Name: python3-module-%oname
Version: 2023.6
Release: alt1

Summary: Image IO for fable

License: BSD-3-Clause AND GPL-2.0-or-later AND LGPL-3.0-or-later AND MIT
Group: Development/Python3
URL: https://pypi.org/project/fabio
VCS: https://github.com/silx-kit/fabio

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-Cython
BuildRequires: meson
BuildRequires: python3-module-mesonpy

%if_with check
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-h5py
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-glymur
%endif

%description
FabIO is an I/O library for images produced by 2D X-ray detectors and written
in Python. FabIO support images detectors from a dozen of companies
(including Mar, Dectris, ADSC, Hamamatsu, Oxford), for a total of 30 different
file formats (like CBF, EDF, TIFF) and offers an unified interface to their
headers (as a Python dictionary) and datasets (as a numpy ndarray of integers or
floats)

%prep
%setup

# remove some third-party bundled stuff
rm -rv src/fabio/third_party/_local

%build
%pyproject_build

%install
%pyproject_install

# Dont package tests
rm -rv %buildroot%python3_sitelibdir/%oname/test
rm -rv %buildroot%python3_sitelibdir/%oname/benchmark

%check
python3 run_tests.py

%files
%doc copyright *.rst
%_bindir/densify_Bragg
%_bindir/eiger2cbf
%_bindir/eiger2crysalis
%_bindir/fabio-convert
%_bindir/fabio_viewer
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.0.dist-info

%changelog
* Tue Sep 26 2023 Grigory Ustinov <grenka@altlinux.org> 2023.6-alt1
- Automatically updated to 2023.6.
- Built with check.
- Built without tests.

* Wed Jul 12 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 2023.4.1-alt1.1
- NMU:
     + moved %%python3_sitelibdir/%%oname/benchmark to subpackage with tests
     + ignore requirements to fabio.tests and fabio.benchmark

* Sat Apr 29 2023 Grigory Ustinov <grenka@altlinux.org> 2023.4.1-alt1
- Automatically updated to 2023.4.1.

* Thu Jan 19 2023 Grigory Ustinov <grenka@altlinux.org> 2022.12.1-alt1
- Automatically updated to 2022.12.1.

* Fri Jun 03 2022 Grigory Ustinov <grenka@altlinux.org> 0.14.0-alt1
- Automatically updated to 0.14.0.

* Tue Feb 08 2022 Grigory Ustinov <grenka@altlinux.org> 0.13.0-alt1
- Automatically updated to 0.13.0.

* Thu Aug 12 2021 Grigory Ustinov <grenka@altlinux.org> 0.12.0-alt1
- Automatically updated to 0.12.0.

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt2
- drop BR: libnumpy-devel (it was python2 only package)

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 0.10.2-alt1
- Automatically updated to 0.10.2.

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt2
- Rebuild for python3.7.

* Mon Apr 08 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Updated to latest upstream release (Closes: #36539)
- Disabled build for python-2.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Initial build for ALT.
