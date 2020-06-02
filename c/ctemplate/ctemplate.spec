Name: ctemplate
Version: 2.4
Release: alt1
License: BSD-3-Clause
Group: System/Libraries
Summary: HTML template library written in C inspired by perl HTML::Template
URL: http://code.google.com/p/ctemplate
# http://ctemplate.googlecode.com/svn/trunk/
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: python3-base

%description
HTML template library written in C inspired by perl HTML::Template.
Template language has HTML-like tags (tmpl_var, tmpl_if, tmpl_loop, etc.)
Use library to build a variable list and pass it to a template.

%package -n lib%name
Summary: HTML template library written in C inspired by perl HTML::Template
Group: System/Libraries
Provides: google-ctemplate = %EVR
Obsoletes: google-ctemplate < %EVR

%description -n lib%name
HTML template library written in C inspired by perl HTML::Template.
Template language has HTML-like tags (tmpl_var, tmpl_if, tmpl_loop, etc.)
Use library to build a variable list and pass it to a template.

%package -n lib%name-devel
Summary: HTML template library written in C inspired by perl HTML::Template
Group: System/Libraries
Requires: lib%name = %EVR
Provides: %name-devel = %EVR
Provides: google-ctemplate-devel = %EVR
Obsoletes: google-ctemplate-devel < %EVR

%description -n lib%name-devel
HTML template library written in C inspired by perl HTML::Template.
Template language has HTML-like tags (tmpl_var, tmpl_if, tmpl_loop, etc.)
Use library to build a variable list and pass it to a template.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-static=no
%make_build

%install
%makeinstall_std


%files -n lib%name
%doc README.md
%_libdir/*so.*
%_defaultdocdir/*

%files -n lib%name-devel
%_bindir/*
%_libdir/*so
%_includedir/%name
%_pkgconfigdir/*

%changelog
* Tue Jun 02 2020 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1
- New version.
- Fix License tag according to SPDX.

* Wed Jun 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.3-alt1.svn20140319.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.svn20140319
- Version 2.3

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.1
- Fixed headers for build with gcc 4.7

* Tue Nov 13 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2-alt1
- Update to new version

* Mon Apr 16 2012 Evgeny Sinelnikov <sin@altlinux.ru> 2.1-alt1
- Update to new version
- Replace build utilities to devel subpackage
- Set obsolete and conflict to google-ctemplate and google-ctemplate-devel
- Add provide ctemplate-devel by libctemplate-devel for compatibility

* Tue Jan 24 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0-alt1
- Update version
- Add URL and fix license

* Thu Nov 24 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- Build for ALT
