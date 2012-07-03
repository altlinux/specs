Name:		chm2pdf
Summary:	CHM to PDF converter
Version:	0.9.1
Release:	alt1
Group:		Office
License:	GPL2
Packager: 	Mikhail Pokidko <pma@altlinux.org>
URL:		http://code.google.com/p/chm2pdf/
Source:		%name-%version.tar
Patch:		%name-%version-%release.patch
BuildArch: noarch

# Automatically added by buildreq on Wed May 21 2008
BuildRequires: python-devel

Requires: libchm-utils htmldoc python-module-pychm

%description
A simple Python script that converts CHM files into PDF files.


%prep
%setup -q
%patch -p1

%build
%python_build

%install
%python_install

%files
%_bindir/*
%python_sitelibdir/chm2pdf-*.egg-info

%changelog
* Thu Jan 26 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.1-alt1
- Update to new release
- Fixed fails to process chm's without table of contents

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt3.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt3.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Mikhail Pokidko <pma@altlinux.org> 0.9-alt3
- Fixed packaging errors.

* Mon May 26 2008 Mikhail Pokidko <pma@altlinux.org> 0.9-alt2
- Fixed dependencies

* Wed May 21 2008 Mikhail Pokidko <pma@altlinux.org> 0.9-alt1
- Initial ALT build


