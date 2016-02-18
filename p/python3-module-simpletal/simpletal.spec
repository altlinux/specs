Name: python3-module-simpletal
Version: 5.1
Release: alt1.1
Summary: SimpleTAL is an independent implementation of TAL
License: BSD-like
Group: Development/Python3
Url: http://www.owlfish.com/software/simpleTAL/
Source: SimpleTAL-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base
BuildRequires: rpm-build-python3

%description
SimpleTAL is a stand alone Python implementation
of the TAL, TALES and METAL specifications used in Zope.

%prep
%setup -n SimpleTAL-%version

%build
%python3_build_install --optimize=2 --root=buildroot

%install
mkdir -p %buildroot
cp -r buildroot/* %buildroot

%files
%doc *.txt documentation/html
%python3_sitelibdir/*

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 5.1-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1
- Initial build for Sisyphus

