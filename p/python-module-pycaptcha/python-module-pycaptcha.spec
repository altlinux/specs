%define version 0.4
%define release alt3

%setup_python_module pycaptcha

Summary: An attempt to rewrite the decimal module in C
Name: %packagename
Version: %version
Release: %release.1
Source: %modulename-%version.tar.bz2
Patch1:  %modulename-%version-alt-fixes.patch.bz2
License: MIT
Group: Development/Python
Url: http://labs.logic.cz/download/pycaptcha/pycaptcha-0.4.tar.gz
Packager: Python Development Team <python at packages.altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Tue Sep 16 2008
BuildRequires: python-devel

Requires: python-module-imaging

%description
This is the PyCAPTCHA package, a collection of Python modules
implementing CAPTCHAs: automated tests that humans should pass,
but current computer programs can't. These tests are often
used for security.

See  http://www.captcha.net for more information and examples.

This project was started because the CIA project, written in
Python, needed a CAPTCHA to automate its user creation process
safely. All existing implementations the author could find were
written in Java or for the .NET framework, so a simple Python
alternative was needed.

%prep
%setup
%patch1 -p1

%build
mkdir -p buildroot

# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record
%python_build_debug \
        install --optimize=2 \
                --root=`pwd`/buildroot \
                --record=INSTALLED_FILES
               
%install
cp -pr buildroot %buildroot
unset RPM_PYTHON

pushd %buildroot%python_sitelibdir/Captcha/data/fonts/vera
for i in Vera*.ttf; do
	rm -f $i
	ln -s %_datadir/fonts/ttf/TrueType-vera/$i .
done
popd

%pre
rm -f %python_sitelibdir/Captcha/data/fonts/vera/Vera*.ttf

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt3.1
- Rebuild with Python-2.7

* Sat Apr 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt3
- Replaced fonts by links to fonts from fonts-ttf-vera (ALT #25317)

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Rebuilt with python 2.6

* Tue Sep 16 2008 Eugine V. Kosenko <maverik@altlinux.ru> 0.4-alt1
- Initial build
