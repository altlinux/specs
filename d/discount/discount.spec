%define sover 0

Name: discount
Version: 2.2.7d
Release: alt1

Summary: A implementation of John Gruber's Markdown markup language.
# BSD, BSD-style, BSD-4-Clause-UC ...
License: BSD-style
Group: Text tools
Url: http://www.pell.portland.or.us/~orc/Code/discount/

Source: %name-%version.tar
Source44: %name.watch
Patch: %name-%version-%release.patch
Patch1: %name-2.2.7d-alt-no-ldconfig.patch

Requires: lib%name = %EVR

%description
DISCOUNT is a implementation of John Gruber's Markdown markup language.

%package -n lib%name
Summary: Shared libraries of DISCOUNT
Group: System/Libraries

%description -n lib%name
DISCOUNT is a implementation of John Gruber's Markdown markup language.

This package contains shared libraries of DISCOUNT.

%package -n lib%name-devel
Summary: Development files of DISCOUNT
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
DISCOUNT is a implementation of John Gruber's Markdown markup language.

This package contains development files of DISCOUNT.

%prep
%setup
%patch -p1
%patch1 -p1

%build
# non-GNU configure
%add_optflags %optflags_shared
CFLAGS="%optflags" ./configure.sh \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--shared \
	--pkg-config
%nil
%make

%install
#mkdir -p %buildroot/%_bindir
%make DESTDIR=%buildroot install.everything

%check
LD_LIBRARY_PATH=%buildroot%_libdir %make test


%files
%_bindir/makepage
%_bindir/markdown
%_bindir/mkd2html
%_bindir/theme
%_man1dir/makepage.1*
%_man1dir/markdown.1*
%_man1dir/mkd2html.1*
%_man1dir/theme.1*
%_man7dir/markdown.7*
%_man7dir/mkd-extensions.7*

%files -n lib%name
%_libdir/libmarkdown.so.*

%files -n lib%name-devel
%_includedir/mkdio.h
%_pkgconfigdir/libmarkdown.pc
%_libdir/libmarkdown.so
%_man3dir/*

%changelog
* Thu Aug 31 2023 Yuri N. Sedunov <aris@altlinux.org> 2.2.7d-alt1
- 2.2.7d

* Wed Mar 14 2018 Ildar Mulyukov <ildar@altlinux.ru> 2.2.3a-alt1.git.13.gddf8b6f
- new version

* Sat Sep 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.7-alt1.git20140807
- Version 2.1.7

* Wed Jun 16 2010 Kirill A. Shutemov <kas@altlinux.org> 1.6.5-alt1
- First build for ALT Linux Sisyphus

