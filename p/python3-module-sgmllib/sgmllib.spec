%define oname sgmllib
Name: python3-module-%oname
Version: 1.0.0
Release: alt1.hg20100824.1.1.1
Summary: Py3k port of the old stdlib module
License: BSD
Group: Development/Python3
Url: http://hg.hardcoded.net/sgmllib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/hsoft/sgmllib
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-distribute

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base
BuildRequires: python3-module-setuptools rpm-build-python3

%description
sgmllib was dropped in Python 3. For those depending on it, that's
somewhat unfortunate. This is a quick and dirty port of this old module.
I just ran 2to3 on it and published it. I don't intend to maintain it,
so it might be a good idea to eventually think about finding another
module to use.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc CHANGES README
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.hg20100824.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.hg20100824.1.1
- NMU: Use buildreq for BR.

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.0-alt1.hg20100824.1
- Rebuild with Python-3.3

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20100824
- Initial build for Sisyphus

