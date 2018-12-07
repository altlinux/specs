%define  modulename restructuredtext_lint

Name:    python-module-%modulename
Version: 1.2.1
Release: alt1

Summary: reStructuredText linter
License: Unlicense
Group:   Development/Python
URL:     https://github.com/twolfson/restructuredtext-lint

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-docutils >= 0.11

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-docutils >= 0.11

BuildArch: noarch

Source: %modulename-%version.tar.gz

%description
%summary

%package -n python3-module-%modulename
Summary: reStructuredText linter
Group: Development/Python3

%description -n python3-module-%modulename
%summary

%prep
%setup -n %modulename-%version
cp -fR . ../python3

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
%python_sitelibdir/*

%files -n python3-module-%modulename
%_bindir/*
%python3_sitelibdir/*

%changelog
* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
