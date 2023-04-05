%define oname imagesize

%def_with check

Name: python3-module-imagesize
Version: 1.4.1
Release: alt1

Summary: Getting image size from png/jpeg/jpeg2000/gif file in pure Python

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/imagesize/
Vcs: https://github.com/shibukawa/imagesize_py

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%description
 It parses image files' header and return image size.

* PNG
* JPEG
* JPEG2000
* GIF
* TIFF
* SVG
* Netpbm
* WebP

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m unittest

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Wed Apr 05 2023 Anton Vyatkin <toni@altlinux.org> 1.4.1-alt1
- New version 1.4.1

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- build python3 module separately, rewrite spec
- new version (1.2.0) with rpmgs script

* Mon May 06 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Build new version.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.7.1-alt1.1
- Rebuild with python3.7.

* Sat Apr 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1
- upstream release 0.7.1 (no changes)

* Thu Apr 21 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1
- Initial build for ALT Sisyphus. (Needed for sphinx-1.4.1.) (ALT#31976)
- The same source is used for both Python{2,3} with a commit from:
  https://github.com/xantares/imagesize_py/tree/py2a3
