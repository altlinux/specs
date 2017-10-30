%def_with python3

%define modulename rtlsdr

Name: python-module-%modulename
Version: 0.2.91
Release: alt1

Summary: A Python wrapper for librtlsdr (a driver for Realtek RTL2832U based SDR's)
License: GPLv3
Group: Development/Python
URL: https://github.com/roger-/pyrtlsdr

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools


BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-m2r
BuildRequires: python-module-mistune
BuildRequires: python-module-docutils

BuildArch: noarch

Source: %name-%version.tar

%description
%summary
Python 2 version

%if_with python3
%package -n python3-module-%modulename
Summary: %summary
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-m2r
BuildRequires: python3-module-mistune
BuildRequires: python3-module-docutils

%description -n python3-module-%modulename
%summary
Python 3 version
%endif

%prep
%setup
rm -rf pyrtlsdr.egg-info
chmod 644 rtlsdr/rtlsdrtcp/base.py

%if_with python3
rm -rf ../python3-module-%modulename
cp -a . ../python3-module-%modulename
pushd ../python3-module-%modulename
find . -name '*.py' | xargs sed -i '1s|^#!.*|#!%_bindir/python3|'
popd
%endif

%build
%if_with python3
pushd ../python3-module-%modulename
%python3_build
popd
%endif

%python_build

%install
%if_with python3
pushd ../python3-module-%modulename
%python3_install
popd
%endif

%python_install

%files
%doc README.md
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%doc README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Dec 28 2018 Anton Midyukov <antohami@altlinux.org> 0.2.91-alt1
- new version 0.2.91

* Mon Mar 26 2018 Anton Midyukov <antohami@altlinux.org> 0.2.7-alt2
- Fix buildrequires

* Sun Mar 18 2018 Anton Midyukov <antohami@altlinux.org> 0.2.7-alt1
- Initial build for Sisyphus
