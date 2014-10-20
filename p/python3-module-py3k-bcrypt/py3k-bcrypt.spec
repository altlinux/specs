%define oname py3k-bcrypt

Name: python3-module-%oname
Version: 0.3
Release: alt1.git20120906
Summary: Python3 port of py-bcrypt
License: BSD
Group: Sciences/Mathematics
Url: http://crd.lbl.gov/~dhbailey/mpdist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/doganaydin/py3k-bcrypt.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3

%py3_provides bcrypt

%description
py3k-bcrypt is an implementation the OpenBSD Blowfish password hashing
algorithm, as described in "A Future-Adaptable Password Scheme" by Niels
Provos and David Mazieres.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc ChangeLog README TODO
%python3_sitelibdir/*

%changelog
* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20120906
- Initial build for Sisyphus

