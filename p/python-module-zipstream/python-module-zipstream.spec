%def_with python3
%define oname zipstream

Name: python-module-zipstream
Version: 1.1.4
Release: alt2.1
Summary: ZIP archive generator for Python

License: GPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/%oname
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.python.org/packages/1a/a4/58f0709cef999db1539960aa2ae77100dc800ebb8abb7afc97a1398dfb2f/%oname-%version.tar.gz
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-nose
%endif
BuildRequires: python-devel python-module-setuptools python-module-nose
%py_provides %oname

%description
zipstream.py is a zip archive generator based on python 3.3's zipfile.py.
It was created to generate a zip file generator for streaming (ie web apps).

%if_with python3
%package -n python3-module-%oname
Summary: ZIP archive generator for Python3
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-zipstream
zipstream.py is a zip archive generator based on python 3.3's zipfile.py.
It was created to generate a zip file generator for streaming (ie web apps).
Python 3 version.
%endif

%prep
%setup -n %oname-%version

%if_with python3
rm -fR ../python3-module-%oname-%version
cp -fR . ../python3-module-%oname-%version
%endif

%build
%python_build

%if_with python3
pushd ../python3-module-%oname-%version
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3-module-%oname-%version
%python3_install
popd
%endif

%check
python setup.py test

%if_with python3
pushd ../python3-module-%oname-%version
python3 setup.py test
popd
%endif

%files
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.4-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 22 2017 Anton Midyukov <antohami@altlinux.org> 1.1.4-alt2
- srpm build

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 1.1.4-alt1
- Initial build for ALT Linux Sisyphus.
