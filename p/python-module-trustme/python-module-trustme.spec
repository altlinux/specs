%define  modulename trustme

Name:    python-module-%modulename
Version: 0.5.0
Release: alt1

Summary: #1 quality TLS certs while you wait, for the discerning tester
License: Apache2 or MIT
Group:   Development/Python
URL:     https://github.com/python-trio/trustme

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
trustme is a tiny Python package that does one thing: it gives you a
fake certificate authority (CA) that you can use to generate fake TLS
certs to use in your tests. Well, technically they're real certs,
they're just signed by your CA, which nobody trusts. But you can trust
it. Trust me.

%package -n python3-module-%modulename
Summary: #1 quality TLS certs while you wait, for the discerning tester
Group: Development/Python3

%description -n python3-module-%modulename
trustme is a tiny Python package that does one thing: it gives you a
fake certificate authority (CA) that you can use to generate fake TLS
certs to use in your tests. Well, technically they're real certs,
they're just signed by your CA, which nobody trusts. But you can trust
it. Trust me.

%prep
%setup -n %modulename-%version
rm -rf ../python3
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
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files -n python3-module-%modulename
%python3_sitelibdir/%{modulename}*

%changelog
* Tue Jan 22 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
