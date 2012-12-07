Name: ctemplate
Version: 2.2
Release: alt1.1
License: BSD
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Group: System/Libraries
Summary: HTML template library written in C inspired by perl HTML::Template
URL: http://code.google.com/p/ctemplate
Source: http://ctemplate.googlecode.com/files/%name-%version.tar.gz
Patch: ctemplate-2.2-alt-gcc4.7.patch

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
%patch -p2

%build
%autoreconf
%configure
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
