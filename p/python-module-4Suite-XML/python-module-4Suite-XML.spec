Name: python-module-4Suite-XML
Version: 1.0.2
Release: alt3.2.1.1

Summary: An open-source platform for XML processing
License: The 4Suite License
Group: Development/Python

Packager: Kirill Maslinsky <kirill@altlinux.org>

Source: %name-%version.tar
Url: http://4suite.org

BuildRequires(pre): rpm-build-python

%setup_python_module 4Suite-XML

%description
XML tools and libraries for Python: Domlette, XPath, XSLT, XPointer,
XLink, XUpdate.


%package doc
Summary: Documentation for 4Suite XML module
Group: Development/Python
BuildArch: noarch

%description doc
This package contains documentation for 4Suite XML module.


%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_build_install \
    --system \
    --install-docs=%_docdir/%name-%version \
    --install-lib=%python_sitelibdir

rm -rf %buildroot%_libdir/4Suite/

%files
%_bindir/*
%python_sitelibdir/Ft/
%python_sitelibdir/*.egg-info
%_datadir/4Suite/

%files doc
%doc %_defaultdocdir/%name-%version/

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt3.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt3.2.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3.2
- Rebuilt for debuginfo

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3.1
- Rebuilt with python 2.6

* Sat Jul 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.2-alt3
- spec fixes
- package docs separately

* Mon Mar 02 2009 Kirill Maslinsky <kirill@altlinux.org> 1.0.2-alt2
- fixed build
    + place files into %python_sitelibdir to have them n proper
      location on x86_64

* Wed Jun 18 2008 Kirill Maslinsky <kirill@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

