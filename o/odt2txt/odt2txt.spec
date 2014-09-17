Name: odt2txt
Version: 0.4
Release: alt2.git20140608
Summary: Extract text from OpenDocument Text files
License: %gpl2only
Group: Text tools
URL: http://stosberg.net/%name
# https://github.com/dstosberg/odt2txt.git
Source: %name-%version.tar

# Automatically added by buildreq on Tue Nov 06 2007
BuildRequires: zlib-devel
BuildRequires: rpm-build-licenses
BuildPreReq: libzip-devel

%description
%name extracts the text out of OpenDocument Texts. It is small, fast
and portable, can output the document in your console encoding, and has
very few external dependencies.


%prep
%setup


%build
%make_build HAVE_LIBZIP=1 \
	CFLAGS="%optflags -DHAVE_LIBZIP=1 $(pkg-config libzip --cflags)"


%install
%if 1
%makeinstall_std PREFIX=%_prefix HAVE_LIBZIP=1 \
	CFLAGS="%optflags -DHAVE_LIBZIP=1 $(pkg-config libzip --cflags)"
%else
install -D -m 0755 {,%buildroot%_bindir/}%name
install -D -m 0644 {,%buildroot%_man1dir/}%name.1
%endif


%files
%doc *.md
%_bindir/*
%_man1dir/*


%changelog
* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2.git20140608
- Snapshot from git

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Aug 20 2008 Led <led@altlinux.ru> 0.4-alt1
- 0.4

* Tue Nov 06 2007 Igor Zubkov <icesik@altlinux.org> 0.3-alt1
- build for Sisyphus (spec from Dag Wieers repos)

* Mon Jun 25 2007 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Updated to release 0.3.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Updated to release 0.2.

* Sat Dec 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
