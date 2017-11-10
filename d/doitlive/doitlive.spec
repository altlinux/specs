Name:    doitlive
Version: 3.0.2
Release: alt1

Summary: Because sometimes you need to do it live
License: MIT
Group:   Other
URL:     https://github.com/sloria/doitlive

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %name-%version.tar
Patch0: doitlive-3.0.2-alt-open-files-in-utf-8-explicitly.patch

%description
%summary

%prep
%setup -n %name-%version
%patch0 -p1

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Nov 09 2017 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus
