Name: ctemplate
Version: 2.3
Release: alt1.svn20140319
License: BSD
Group: System/Libraries
Summary: HTML template library written in C inspired by perl HTML::Template
URL: http://code.google.com/p/ctemplate
# http://ctemplate.googlecode.com/svn/trunk/
Source: %name-%version.tar.gz

BuildRequires: gcc-c++

%description
HTML template library written in C inspired by perl HTML::Template.
Template language has HTML-like tags (tmpl_var, tmpl_if, tmpl_loop, etc.)
Use library to build a variable list and pass it to a template.

%package -n lib%name
Summary: HTML template library written in C inspired by perl HTML::Template
Group: System/Libraries
Conflicts: google-ctemplate
Obsoletes: google-ctemplate

%description -n lib%name
HTML template library written in C inspired by perl HTML::Template.
Template language has HTML-like tags (tmpl_var, tmpl_if, tmpl_loop, etc.)
Use library to build a variable list and pass it to a template.

%package -n lib%name-devel
Summary: HTML template library written in C inspired by perl HTML::Template
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Conflicts: google-ctemplate-devel
Obsoletes: google-ctemplate-devel

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
%make_build V=1

%install
%makeinstall_std


%files -n lib%name
%_libdir/*so.*
%_defaultdocdir/*

%files -n lib%name-devel
%_bindir/*
%_libdir/*so
%_includedir/%name
%_pkgconfigdir/*

%changelog
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
