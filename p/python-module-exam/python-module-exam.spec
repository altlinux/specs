%def_with python3
%define oname exam

Name: python-module-exam
Version: 0.10.6
Release: alt2.1
Summary: Helpers for better testing

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/%oname
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.python.org/packages/c7/bd/c15ce029540bb1b551af83c0df502ba47e019ce7132a65db046ad16b8eda/%oname-%version.tar.gz
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-mock python3-module-nose
%endif
BuildPreReq: python-devel python-module-setuptools python-module-mock python-module-nose
%py_provides %oname

%description
Exam is a Python toolkit for writing better tests. It aims to remove a lot of
the boiler plate testing code one often writes, while still following Python
conventions and adhering to the unit testing interface.

%if_with python3
%package -n python3-module-%oname
Summary: Helpers for better testing
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Exam is a Python toolkit for writing better tests. It aims to remove a lot of
the boiler plate testing code one often writes, while still following Python
conventions and adhering to the unit testing interface.
Python 3 version.
%endif

%prep
%setup -n %oname-%version

%if_with python3
rm -fR ../python3-module-%oname
cp -fR . ../python3-module-%oname
%endif

%build
%python_build

%if_with python3
pushd ../python3-module-%oname
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3-module-%oname
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
python3 setup.py test
%endif

%files
%doc *.rst
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.6-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.10.6-alt2
- srpm build

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 0.10.6-alt1
- Initial build for ALT Linux Sisyphus (Closes: 32334).
