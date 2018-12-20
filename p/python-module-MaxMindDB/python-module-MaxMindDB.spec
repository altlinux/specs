%define  oname MaxMindDB
%define  descr Python MaxMind DB reader extension
Name:    python-module-%oname
Version: 1.4.1
Release: alt1

Summary: %descr
License: ASLv2
Group:   Development/Python
URL:     https://github.com/maxmind/MaxMind-DB-Reader-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: libmaxminddb-devel

Source:  %oname-%version.tar

%description
%descr

%package -n python3-module-%oname
Summary: %descr
Group: Development/Python3

%description -n python3-module-%oname
%descr

%prep
%setup -n %oname-%version
cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%files
%python_sitelibdir/maxminddb
%python_sitelibdir/*.egg-info

%files -n python3-module-%oname
%python3_sitelibdir/maxminddb
%python3_sitelibdir/*.egg-info

%changelog
* Thu Dec 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
