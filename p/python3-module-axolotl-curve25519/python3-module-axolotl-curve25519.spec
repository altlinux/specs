%define	 modulename axolotl_curve25519

Name:	 python3-module-axolotl-curve25519
Version: 0.4.1.post2
Release: alt1

Summary: python wrapper for curve25519 library with ed25519 signatures

License: GPL-3.0-only
Group:	 Development/Python3
Url:	 https://github.com/tgalal/python-axolotl-curve25519

Source:	 python-axolotl-curve25519-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev

%description
This is python wrapper for curve25519 library with ed25519 signatures. The C
code was pulled from libaxolotl-android.

%prep
%setup -n python-axolotl-curve25519-%version

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%python3_sitelibdir/%modulename.cpython-*.so
%python3_sitelibdir/python_%modulename-%version-py*.egg-info/

%changelog
* Sun Oct 18 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.4.1.post2-alt1
- Initial build for ALT Sisyphus.

