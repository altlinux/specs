%def_with python3

%define modulename rtlsdr

Name: python-module-%modulename
Version: 0.2.7
Release: alt1

Summary: A Python wrapper for librtlsdr (a driver for Realtek RTL2832U based SDR's)
License: GPLv3
Group: Development/Python
URL: https://github.com/roger-/pyrtlsdr

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools python-module-pypandoc

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
BuildRequires: python3-dev python3-module-setuptools python3-module-pypandoc

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
* Sun Mar 18 2018 Anton Midyukov <antohami@altlinux.org> 0.2.7-alt1
- Initial build for Sisyphus
