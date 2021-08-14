%define oname polib

Name: python3-module-polib
Version: 1.1.1
Release: alt1

Summary: Manipulate, create, and modify gettext files

License: BSD-like
Group: Development/Python3
Url: https://bitbucket.org/izi/polib

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-coverage

%py3_provides %oname

%description
polib is a library to manipulate, create, modify gettext files (pot, po
and mo files). You can load existing files, iterate through it's
entries, add, modify entries, comments or metadata, etc... or create new
po files from scratch.

%prep
%setup
subst 's|coverage|coverage3|' runtests.sh

%build
%python3_build

%install
%python3_install

%check
./runtests.sh

%files
%doc CHANGELOG *.rst
%python3_sitelibdir/*

%changelog
* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- cleanup spec, new version 1.1.1 (with rpmrb script)

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.5-alt1.1.2
- (NMU) rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus

