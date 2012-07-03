%define oname fonttools
Name: python-module-%oname
Version: 2.3
Release: alt1.1

Summary: Converts OpenType and TrueType fonts to and from XML

Group: Development/Python
License: LGPL
Url: http://sourceforge.net/projects/fonttools/

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname

%add_python_req_skip Res calldll macfs

Source: http://downloads.sourceforge.net/%oname/%oname-%version.tar

BuildPreReq: rpm-build-compat >= 1.2

# manually removed: python-module-numpy python-modules-email rpm-build-java rpm-build-mono rpm-build-seamonkey
# Automatically added by buildreq on Sun Nov 30 2008
BuildRequires: python-devel python-module-PyXML python-module-ctypes xorg-sdk python-module-numpy 

%description
TTX is a tool to convert OpenType and TrueType fonts to and from
XML. FontTools is a library for manipulating fonts, written in Python. It
supports TrueType, OpenType, AFM and to an extent Type 1 and some
Mac-specific formats.

%prep
%setup -n %oname-%version

# macOS
rm Lib/fontTools/ttLib/test/ttBrowser.py

%build
%python_build

%install
%python_install

%files
%_bindir/ttx
%python_sitelibdir/FontTools/
%python_sitelibdir/FontTools.pth
#%python_sitelibdir/%oname-%version-py%__python_version.egg-info
%_man1dir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1
- updated to 2.3

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt1.1.1
- Rebuild with Python-2.7

* Mon Jul 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.1
- Rebuild with python 2.6

* Sun Nov 30 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Linux Sisyphus
