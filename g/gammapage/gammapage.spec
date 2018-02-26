Name: gammapage
Version: 0.5.1
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Monitor Calibration Tool
License: GPLv2+
Group: Graphics

URL: http://www.pcbypaul.com/software/GAMMApage.shtml
Source: http://www.pcbypaul.com/software/dl/gammapage-%version.tar.gz

Requires: xgamma

BuildArch: noarch

# Automatically added by buildreq on Wed Dec 16 2009
BuildRequires: python-devel

%description
A gamma-adjusting utility for your monitor. Able to adjust gamma on the fly and
save settings to be used at each login (on a per-user basis - GAMMApage will
only write to the user's home directory).

%prep
%setup

%build
mv GAMMApage gammapage
subst 's/GAMMApage/gammapage/g' setup.py
python setup.py build

%install
python setup.py install --root=%buildroot

%files
%_bindir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Mon Dec 14 2009 Victor Forsyuk <force@altlinux.org> 0.5.1-alt1
- 0.5.1

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.1
- Rebuilt with python 2.6

* Tue Sep 02 2008 Victor Forsyuk <force@altlinux.org> 0.5-alt1
- Initial build.
