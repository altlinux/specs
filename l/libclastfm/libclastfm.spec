%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name:		libclastfm
Version:	0.5
Release:	alt3.git20130316
Summary:	Unofficial C-API for the Last.fm web service

Group:		System/Libraries
License:	GPLv2+
URL:		http://liblastfm.sourceforge.net
Source0:	%name-%version.tar

BuildRequires: libcurl-devel

%description
%name is an unofficial C-API for the Last.fm web service
written with libcurl. libclastfm supports much more than
basic scrobble submission. You can send shouts, fetch album covers
and much more.

%package devel
Summary: Development files for %{name}
Group:	 Development/C
Requires: %name = %version-%release

%description devel
This package contains the development files for %{name}.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog NEWS
%_libdir/*.so.*

%files devel
%_includedir/clastfm.h
%_libdir/*.so
%_pkgconfigdir/libclastfm.pc

%changelog
* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 0.5-alt3.git20130316
- NMU: fixed build with LTO

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.git20130316
- New snapshot

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.5-alt1.git.968af0ab.qa1
- NMU: rebuilt for updated dependencies.

* Fri Apr 20 2012 Egor Glukhov <kaman@altlinux.org> 0.5-alt1.git.968af0ab
- Initial build for Sisyphus

* Sun Mar 06 2011 Matias De lellis <mati86dl@gmail.com> 0.4-1
- Libclastfm 0.4 - Initial release.
