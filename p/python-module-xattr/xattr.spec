%define  oname xattr
%define  descr Python wrapper for extended filesystem attributes

Name:    python-module-%oname
Version: 0.9.7
Release: alt1

Summary: %descr

License: MIT
Group:   Development/Python
URL:     https://github.com/xattr/xattr

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-cffi
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-cffi

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
pushd %buildroot%_bindir
for i in $(ls); do
        mv $i $i.py2
done
popd

pushd ../python3
%python3_install
popd

%files
%_bindir/%oname.py2
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info

%files -n python3-module-%oname
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Wed Dec 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.7-alt1
- Build new version 0.9.7.

* Thu Dec 27 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.6-alt1
- Initial build for Sisyphus.
