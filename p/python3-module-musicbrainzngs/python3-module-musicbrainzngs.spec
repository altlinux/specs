%define modname musicbrainzngs

Name: python3-module-%modname
Version: 0.7.1
Release: alt2

Summary: Python bindings for the MusicBrainz NGS and the Cover Art Archive webservices
Group: Development/Python3
License: BSD-2-Clause and ISC
Url: https://pypi.python.org/pypi/%modname
Source: https://pypi.io/packages/source/m/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description
This Python 3 module implements webservice bindings for the Musicbrainz NGS
site, also known as /ws/2 and the Cover Art Archive.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/%modname/
%doc README.rst COPYING PKG-INFO
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Thu Aug 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt2
- python3-only build

* Thu Jan 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1
- made python2 module optional

* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- first build for Sisyphus

