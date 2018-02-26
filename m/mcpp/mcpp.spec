Summary:    Alternative C/C++ preprocessor
Name:       mcpp
Version:    2.7.2
Release:    alt2.3
License:    BSD
Group:      Development/C
Packager:   Evgeny Sinelnikov <sin@altlinux.ru>
Source:     http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:        http://mcpp.sourceforge.net/
Patch0:     mcpp-manual.html.patch

%description
C/C++ preprocessor defines and expands macros and processes '#if',
'#include' and some other directives.

MCPP is an alternative C/C++ preprocessor with the highest conformance.
It supports multiple standards: K&R, ISO C90, ISO C99, and ISO C++98.
MCPP is especially useful for debugging a source program which uses
complicated macros and also useful for checking portability of a source.

Though mcpp could be built as a replacement of GCC's resident
proprocessor or as a stand-alone program without using library build of
mcpp, this package installs only a program named 'mcpp' which links
shared library of mcpp and behaves independent from GCC.

%prep
%setup -q
%patch0 -p0 -b -z.euc-jp

%build
%configure --enable-mcpplib --enable-static
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
make CFLAGS="%optflags"

%install
iconv -f euc-jp -t utf-8 doc-jp/mcpp-manual.html > doc-jp/mcpp-manual-jp.html
%makeinstall_std
rm -rf %buildroot%_docdir/%name

%files
%doc ChangeLog ChangeLog.old LICENSE NEWS README
%_man1dir/*
%_bindir/%name

%package -n libmcpp
Summary:    Alternative C/C++ preprocessor (library build)
Group:      Development/C

%description -n libmcpp
This package provides a library build of mcpp.

%files -n libmcpp
%_libdir/libmcpp.so.*


%package -n libmcpp-devel
Summary:    Alternative C/C++ preprocessor (development package for library build)
Group:      Development/C
Requires:   libmcpp = %version

%description -n libmcpp-devel
Development package for libmcpp.

%files -n libmcpp-devel
%_libdir/libmcpp.so
%_includedir/mcpp_lib.h
%_includedir/mcpp_out.h


%package -n libmcpp-devel-static
Summary:    Alternative C/C++ preprocessor (development static package)
Group:      Development/C
Requires:   libmcpp-devel = %version

%description -n libmcpp-devel-static
Development static package for libmcpp.

%files -n libmcpp-devel-static
%_libdir/libmcpp.a


%package doc
Summary:    Alternative C/C++ preprocessor (manual for library build)
Group:      Documentation

%description doc
This package provides an html manual for mcpp.

%files doc
%doc doc/mcpp-manual.html
%lang(ja) %doc doc-jp/mcpp-manual-jp.html

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.2-alt2.3
- Removed bad RPATH

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.2-alt2.2
- Rebuilt for debuginfo

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 2.7.2-alt2.1
- Rebuilt for soname set-versions.

* Mon Jan 04 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.7.2-alt2
- The following repocop fixes applied:
 * post_ldconfig for libmcpp
 * postun_ldconfig for libmcpp

* Thu Feb 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.7.2-alt1
- Update to release
- Build static library

* Sun Jul 06 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.7.1-alt2
- Fix spec for Sisyphus policy

* Sun Jul 06 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.7.1-alt1
- Initial ALT Linux Sisyphus release

* Tue May 20 2008 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.7.1-1
- Upstream new release.
- Change to library build.
- Devide to 4 packages: mcpp, libmcpp, libmcpp-devel and mcpp-doc.
- Thanks to Mary Ellen Foster for correcting this spec file.

* Sun Mar 24 2008 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.7-2
- Upstream new release.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.6.4-2
- Rebuild for selinux ppc32 issue.

* Thu May 19 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.4-1
- Upstream new release.

* Fri Apr 27 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.3-5
- Apply the new patch (patch1) for mcpp.

* Wed Apr 25 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.3-4
- Change installation of doc/mcpp-manual.html and doc-jp/mcpp-manual.html.

* Tue Apr 24 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.3-3
- Revise many points to adapt to the guideline of Fedora (thanks to
        the review by Mamoru Tasaka):
    use %%dist, %%configure, %%optflags, %%{_datadir}, %%lang(ja),
    convert encoding of mcpp-manual.html to utf-8,
    and others.

* Sat Apr 21 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.3-2
- Replace some variables with macros.
- Rename this spec file.

* Sat Apr 07 2007 Kiyoshi Matsui <kmatsui@t3.rim.or.jp> 2.6.3-1
- First release for V.2.6.3 on sourceforge.
