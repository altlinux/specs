%def_with python3
%define oname exam

Name: python-module-exam
Version: 0.10.6
Release: alt1
Summary: Helpers for better testing

License: MIT
Group: Development/Python
Url: https://github.com/fluxx/exam
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests python3-module-mock python3-module-nose
%endif
BuildPreReq: python-devel python-module-setuptools-tests python-module-mock python-module-nose
%py_provides %oname

%description
Exam is a Python toolkit for writing better tests. It aims to remove a lot of
the boiler plate testing code one often writes, while still following Python
conventions and adhering to the unit testing interface.

%if_with python3
%package -n python3-module-%oname
Summary: Helpers for better testing
Group: Development/Python
%py3_provides %oname

%description -n python3-module-%oname
Exam is a Python toolkit for writing better tests. It aims to remove a lot of
the boiler plate testing code one often writes, while still following Python
conventions and adhering to the unit testing interface.
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
* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 0.10.6-alt1
- Initial build for ALT Linux Sisyphus (Closes: 32334).
