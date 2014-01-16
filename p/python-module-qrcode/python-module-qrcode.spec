%define oname qrcode
%def_with python3

Name: python-module-%oname
Version: 4.0.4
Release: alt1

Summary: Python module to generate QR Codes

License: BSD
Group: Development/Python
Url: https://github.com/lincolnloop/python-qrcode

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/q/qrcode/qrcode-4.0.4.tar.gz
Source: %oname-%version.tar
BuildArch: noarch

BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-distribute 
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%setup_python_module %oname

%description
This module uses image libraries, Python Imaging Library (PIL) by default,
to generate QR Codes.

%if_with python3
%package -n python3-module-%oname
Summary: Python module to generate QR Codes (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This module uses image libraries, Python Imaging Library (PIL) by default,
to generate QR Codes. 
%endif


%prep
%setup -n %oname-%version

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst LICENSE CHANGES.rst
%python_sitelibdir/%oname/
# pure.py requires pymaging module that is not ready for release
%exclude %python_sitelibdir/%oname/image/pure.py
%exclude %python_sitelibdir/*.egg-info
%_man1dir/*
%_bindir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
# pure.py requires pymaging module that is not ready for release
%exclude %python3_sitelibdir/%oname/image/pure.py
%exclude %python3_sitelibdir/*.egg-*
%endif

%changelog
* Thu Jan 16 2014 Vladimir Didenko <cow@altlinux.ru> 4.0.4-alt1
- initial build for Sisyphus
