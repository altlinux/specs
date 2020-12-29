Name:       python3-module-pikepdf
Version:    2.2.4
Release:    alt1
License:    MPL-2.0
URL:        https://github.com/pikepdf/pikepdf
Summary:    A Python library for reading and writing PDF files
Group:      Development/Python
Source:     pikepdf-%version.tar.gz
Patch:      pikepdf-nodep.patch
Requires:   libpoppler-gir

# Automatically added by buildreq on Tue Dec 29 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libstdc++-devel python-modules python2-base python3 python3-base python3-dev python3-module-cffi python3-module-cryptography python3-module-openssl python3-module-paste python3-module-pkg_resources python3-module-six sh4
BuildRequires: gcc-c++ libqpdf-devel python3-module-pip python3-module-pybind11 python3-module-setuptools python3-module-sphinxcontrib python3-module-toml
BuildRequires: python3-module-wheel python3-module-setuptools_scm

%description
pikepdf is based on QPDF, a powerful PDF manipulation and repair library.
Python + QPDF = "py" + "qpdf" = "pyqpdf", which looks like a dyslexia test.
Say it out loud, and it sounds like "pikepdf".

%prep
%setup -n pikepdf-%version
%patch -p2

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*pikepdf*

%changelog
* Tue Dec 29 2020 Fr. Br. George <george@altlinux.ru> 2.2.4-alt1
- Initial build for ALT

