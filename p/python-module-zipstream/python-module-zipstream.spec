%def_with python3
%define oname zipstream

Name: python-module-zipstream
Version: 1.1.4
Release: alt1
Summary: ZIP archive generator for Python

License: GPLv3+
Group: Development/Python
Url: https://github.com/allanlei/python-%oname
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests python3-module-nose
%endif
BuildPreReq: python-devel python-module-setuptools-tests python-module-nose
%py_provides %oname

%description
zipstream.py is a zip archive generator based on python 3.3's zipfile.py.
It was created to generate a zip file generator for streaming (ie web apps).

%if_with python3
%package -n python3-module-%oname
Summary: ZIP archive generator for Python3
Group: Development/Python
%py3_provides %oname

%description -n python3-module-zipstream
zipstream.py is a zip archive generator based on python 3.3's zipfile.py.
It was created to generate a zip file generator for streaming (ie web apps).
Python 3 version.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
python3 setup.py test

%files
%doc LICENSE
%doc README.*
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc LICENSE
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 1.1.4-alt1
- Initial build for ALT Linux Sisyphus.
