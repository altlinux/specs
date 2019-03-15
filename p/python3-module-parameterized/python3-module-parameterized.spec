%define  modulename parameterized

Name:    python3-module-%modulename
Version: 0.7.0
Release: alt1

Summary: Parameterized testing with any Python test framework
License: BSD
Group:   Development/Python3
URL:     https://pypi.org/project/parameterized/

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
