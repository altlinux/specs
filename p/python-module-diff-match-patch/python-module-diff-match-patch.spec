%define oname diff-match-patch
%define pkgname diff_match_patch
%def_with python3

Name: python-module-%oname
Version: 20121119
Release: alt1

Summary: Python diff, match and patch libraries

License: %asl
Group: Development/Python
Url: https://pypi.python.org/pypi/diff-match-patch/
Packager: Vladimir Didenko <cow@altlinux.org>
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python python-module-setuptools
%if_with python3
BuildPreReq: rpm-build-python3 python3-module-setuptools
%endif

%setup_python_module %oname

%description
The Diff Match and Patch libraries offer robust algorithms to perform the
operations required for synchronizing plain text.

%if_with python3
%package -n python3-module-%oname
Summary: Python diff, match and patch libraries
Group: Development/Python3

%description -n python3-module-%oname
The Diff Match and Patch libraries offer robust algorithms to perform the
operations required for synchronizing plain text.
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
%python_sitelibdir/%pkgname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%pkgname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Thu Mar 16 2017 Vladimir Didenko <cow@altlinux.ru> 20121119-alt1
- Initial build for Sisyphus
