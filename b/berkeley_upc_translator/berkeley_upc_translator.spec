%set_verify_elf_method unresolved=relaxed

Name: berkeley_upc_translator
Version: 2.14.2
Release: alt1
Summary: Berkeley Unified Parallel C (UPC) Translator
License: BSD
Group: Development/C
Url: http://upc.lbl.gov/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: gcc-c++ csh

%description
Berkeley Unified Parallel C (UPC) Translator.

%prep
%setup

%build
%make

%install
%makeinstall_std PREFIX=%buildroot%_libdir/%name

%files
%doc LICENSE.TXT README
%_libdir/%name

%changelog
* Wed Jul 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.2-alt1
- Version 2.14.2

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.0-alt1
- Version 2.14.0

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.2-alt1
- Version 2.12.2

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.1-alt1
- Version 2.12.1

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt2
- Rebuilt for debuginfo

* Thu Dec 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1
- Version 2.12.0

* Sun Sep 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10.2-alt1
- Initial build for Sisyphus

