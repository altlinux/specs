%define origname pmw

Name:           python-module-%origname
Version:        1.3.2
Release:        alt3.1
Summary:        Toolkit for building high-level compound widgets
Group:          Development/Python
License:        BSD
URL:            http://pmw.sourceforge.net
Source:         http://downloads.sourceforge.net/pmw/Pmw.1.3.2.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-licenses
%setup_python_module Pmw
%py_provides Pmw

%description
Pmw (Python megawidgets) is a toolkit for building high-level compound widgets
in Python using the Tkinter module.

%prep
%setup -n %origname

%build
pushd src
sed -i \
	-e 's/\(import\ re\)gsub/\1/' \
	-e "s/regsub\.gsub('import\ Pmw\\\>/re.sub(r'import Pmw\\\b/" \
	-e "s/regsub\.gsub('INITOPT\ \=\ Pmw/re.sub(r'INITOPT = Pmw\\\/" \
	-e "s/regsub\.gsub('\\\<Pmw/re.sub(r'\\\bPmw/" \
	-e "s/regsub\.gsub('import\ PmwLogicalFont/re.sub(r'import PmwLogicalFont/" \
	-e "s/regsub\.gsub('PmwLogicalFont/re.sub(r'PmwLogicalFont\\\/" \
	Pmw/Pmw_1_3/bin/bundlepmw.py
%python_build
popd

%install
pushd src
%python_install --optimize=2
popd

%files
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.2-alt3.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt3
- Rebuilt with python 2.6

* Sun Jul 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt2
- Rebuild as noarch package

* Tue Mar 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus

