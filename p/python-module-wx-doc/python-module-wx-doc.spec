Name: python-module-wx-doc
Version: 2.8.0.1
Release: alt2.1

Summary: Documentation for the wxWindows/wxPython

License: wxWindows License
Group: Development/Python
Url: http://www.wxpython.org

BuildArch: noarch
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sourceforge.net/sourceforge/wxpython/wxPython-docs-%version.tar.bz2
Patch: %name-2.5.4.1.patch

AutoReqProv: no
Requires: python = %__python_version

Provides: wxPython-doc
Obsoletes: wxPython-doc

BuildRequires: python = %__python_version

%description
The %name package contains documentation for wxWindows %version:
A portable C++ and Python GUI toolkit.

%prep
%setup -n wxPython-%version
#%patch -p0 -b .orig

%install
mkdir -p %buildroot%_bindir
sed -e "s|doc_dir='.'|doc_dir='%_docdir/%name-%version'|g"\
     <docs/viewdocs.py >%buildroot%_bindir/viewdocs.py
chmod 755 %buildroot%_bindir/viewdocs.py
rm -f docs/viewdocs.py #???

# Menu support
mkdir -p %buildroot%_menudir
cat >%buildroot%_menudir/%name <<EOF
?package(%name): \
needs=x11 \
section="Documentation" \
title="wxWindows & wxPython" \
command=viewdocs.py \
icon=documentation_section.png \
longtitle="Documentation for the wxWindows/wxPython"
EOF

%files
%doc docs/*
%_bindir/*
%_menudir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.8.0.1-alt2.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0.1-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.8.0.1-alt1.1
- Rebuilt with python-2.5.

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.8.0.1-alt1
- new version, change Packager
- remove obsoleted patch

* Sat Jun 18 2005 Vitaly Lipatov <lav@altlinux.ru> 2.6.1.0-alt1
- NMU: new version

* Wed Mar 30 2005 Vitaly Lipatov <lav@altlinux.ru> 2.5.4.1-alt1
- NMU: new version
- rebuild with python 2.4

* Fri Mar 26 2004 Oleg Gints <go@altlinux.ru> 2.4.2.4-alt1
- 2.4.2.4
- rebuild with Python23

* Mon Sep 15 2003 Oleg Gints <go@altlinux.ru> 2.4.1.2-alt1
- 2.4.1.2
- rename patch
- fix Requires
- add BuildRequires for build in hasher

* Mon Jan 20 2003 Oleg Gints <go@altlinux.ru> 2.4.0.1-alt1
- first release for ALT
