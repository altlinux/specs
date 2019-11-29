%define oname zipstream

Name: python3-module-zipstream
Version: 1.1.4
Release: alt3

Summary: ZIP archive generator for Python
License: GPLv3+
Group: Development/Python3
Url: https://pypi.python.org/pypi/%oname
BuildArch: noarch

Source: https://pypi.python.org/packages/1a/a4/58f0709cef999db1539960aa2ae77100dc800ebb8abb7afc97a1398dfb2f/%oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose

%py3_provides %oname


%description
zipstream.py is a zip archive generator based on python 3.3's zipfile.py.
It was created to generate a zip file generator for streaming (ie web apps).

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.4-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.4-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 22 2017 Anton Midyukov <antohami@altlinux.org> 1.1.4-alt2
- srpm build

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 1.1.4-alt1
- Initial build for ALT Linux Sisyphus.
