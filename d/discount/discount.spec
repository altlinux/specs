%define sover 0

Name: discount
Version: 2.1.7
Release: alt1.git20140807

Summary: A implementation of John Gruber's Markdown markup language.
License: BSD
Group: Text tools
Url: http://www.pell.portland.or.us/~orc/Code/discount/

Source: %name-%version.tar

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

%build
# non-GNU configure
%add_optflags %optflags_shared
CFLAGS="%optflags" ./configure.sh \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--enable-all-features
%make SOVER=0

%check
%make test LD_LIBRARY_PATH=%buildroot%_libdir

%install
mkdir -p %buildroot/%_bindir
%make DESTDIR=%buildroot install.everything SOVER=0

%files
%_bindir/*
%_man1dir/*
%_man3dir/*
%_man7dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sat Sep 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.7-alt1.git20140807
- Version 2.1.7

* Wed Jun 16 2010 Kirill A. Shutemov <kas@altlinux.org> 1.6.5-alt1
- First build for ALT Linux Sisyphus

