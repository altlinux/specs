Name:    doitlive
Version: 3.0.3
Release: alt2

Summary: Because sometimes you need to do it live
License: MIT
Group:   Other
URL:     https://github.com/sloria/doitlive

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%add_findreq_skiplist  %python3_sitelibdir/%name/ipython.py
%add_findprov_skiplist %python3_sitelibdir/%name/ipython.py

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
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Sep 15 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.3-alt2
- Updated provides and requires due to prompt_toolkit update.

* Thu Mar 01 2018 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.3-alt1
- new version 3.0.3

* Thu Nov 09 2017 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus
