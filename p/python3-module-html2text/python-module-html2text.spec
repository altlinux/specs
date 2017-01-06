Name: python3-module-html2text
Version: 2016.9.19
Release: alt1

Summary: Converts a page of HTML into clean, easy-to-read plain ASCII text
Group: Development/Python
License: GPLv3+
Url: http://www.aaronsw.com/2002/html2text/
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-module-setuptools-tests

# https://github.com/szepeviktor/html2text.git
Source0: https://pypi.python.org/packages/22/c0/2d02a1fb9027f54796af2c2d38cf3a5b89319125b03734a9964e6db8dfa0/html2text-%{version}.tar.gz

%py3_provides html2text

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-setuptools
BuildRequires: python3-module-pytest rpm-build-python3

%description
html2text is a Python script that convers a page of HTML into clean,
easy-to-read plain ASCII text.  Better yet, that ASCII also happens to
be valid Markdown (a text-to-HTML format).

%prep
%setup -q -n html2text-%{version}

%build
%python3_build

%install
%python3_install

mv %buildroot%_bindir/html2text %buildroot%_bindir/html2text.py3

%check
PYTHONPATH=%buildroot%python3_sitelibdir python3 setup.py test

%files
%_bindir/html2text.py3
%python3_sitelibdir/*

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 2016.9.19-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2014.4.5-alt1.git20140524.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 2014.4.5-alt1.git20140524.1
- NMU: Use buildreq for BR.

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.4.5-alt1.git20140524
- Add initial build for Sisyphus

