%define oname nose2

%def_with python3

Name: python-module-%oname
Version: 0.6.5
Release: alt1.1

Summary: A unittest-based testing framework for python that makes writing and running tests easier

Group: Development/Python
License: LGPL
Url: https://github.com/nose-devs/nose2

BuildArch: noarch

%setup_python_module %oname

Source: %name-%version.tar

BuildRequires: python-module-setuptools python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildRequires: python3-devel python3-module-coverage
%endif

%description
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as much
as is reasonably possible without resorting to too much magic.

%if_with python3
%package -n python3-module-%oname
Summary: A unittest-based testing framework for python3 that makes writing and running tests easier
Group: Development/Python3

%description -n python3-module-%oname
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as much
as is reasonably possible without resorting to too much magic.
%endif

%prep
%setup
sed -i "s|man/man1|share/man/man1|g" setup.py

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

rm -f %buildroot%_bindir/nosetests

%files
%doc AUTHORS README.rst
%_bindir/nose2-2.7
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%_bindir/nose2
%_bindir/nose2-3*
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 22 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.5-alt1
- Initial build in Sisyphus
