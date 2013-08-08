Name:		libyui-ncurses
Version:	2.44.1
Release:	alt1
License:	%lgpl21only or %lgpl3only
Source:		libyui-ncurses-%{version}.tar
Patch0:		libyui-ncurses-2.44.0-alt-cmake-curses5.9.patch

Group:		System/Libraries
Packager:	Andrey Kolotov <qwest@altlinux.ru>

BuildPreReq:    rpm-build-licenses

BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	gcc-c++
BuildRequires:	pkg-config

BuildRequires:	libyui-devel >= 3.0.4
BuildRequires:	ncurses-devel
BuildRequires:  libncursesw-devel libncurses++-devel
BuildRequires:  doxygen fdupes graphviz texmf-latex-beamer
BuildRequires:	fonts-ttf-core
URL:		http://github.com/libyui/
Summary:	Libyui - Character Based User Interface

%description
This package contains the character based (ncurses) user interface
component for libYUI.


%package -n libyui-ncurses5

Group:		System/Libraries

Requires:	libyui5
Provides:	libyui-ncurses = %{version}
Provides:	yast2-ncurses = 2.42.0
Obsoletes:	yast2-ncurses < 2.42.0
Provides:	yui_backend

Summary:	Libyui - Character Based User Interface

%description -n libyui-ncurses5
This package contains the character based (ncurses) user interface
component for libYUI.


%package devel

Group:		Development/C++

Requires:	libyui-ncurses5 = %{version}
Requires:	glibc-devel
Requires:	libstdc++-devel
Requires:	boost-devel
Requires:	libyui-devel >= 3.0.4
Requires:	ncurses-devel
Requires:       libncursesw-devel

Summary:	Libyui-ncurses header files

%description devel
This package contains the character based (ncurses) user interface
component for libYUI.

This can be used independently of YaST for generic (C++) applications.
This package has very few dependencies.


%package doc

Group:		Documentation

Requires:       libyui-ncurses5 = %{version}
Requires:       fonts-ttf-core

Summary:        Libyui-ncurses documentation

%description doc
This package contains the character based (ncurses) user interface
component for libYUI.

This package provides the documentation. (HTML & PDF)


%prep
%setup -q -n libyui-ncurses-%{version}
%patch0 -p1


%build

CFLAGS="${CFLAGS:-%optflags}"; export CFLAGS;
CXXFLAGS="${CXXFLAGS:-%optflags}"; export CXXFLAGS;

./bootstrap.sh %{_prefix}

mkdir build
cd build

cmake .. \
	-DPREFIX=%{_prefix} \
	-DDOC_DIR=%{_docdir} \
	-DINSTALL_DOCS=ON \
	-DLIB_DIR=%{_lib} \
	-DCMAKE_BUILD_TYPE=RELEASE

make docs


%install
cd build
%make_install DESTDIR=%buildroot install
install -m0755 -d %buildroot/%{_docdir}/libyui-ncurses5/
install -m0755 -d %buildroot/%{_libdir}/yui
install -m0644 ../COPYING* %buildroot/%{_docdir}/libyui-ncurses5/
fdupes -s %buildroot/%_docdir/libyui-ncurses5

%files -n libyui-ncurses5
%defattr(-,root,root)
%dir %{_libdir}/yui
%{_libdir}/yui/lib*.so.*
%doc %dir %{_docdir}/libyui-ncurses5
%doc %{_docdir}/libyui-ncurses5/COPYING*

%files devel
%defattr(-,root,root)
%{_libdir}/yui/lib*.so
%{_prefix}/include/yui
%{_libdir}/pkgconfig/libyui-ncurses.pc
%{_libdir}/cmake/libyui-ncurses
%{_datadir}/libyui

%files doc
%doc %{_docdir}/libyui-ncurses5
%exclude %{_docdir}/libyui-ncurses5/COPYING*

%changelog
* Thu Aug 8 2013 Andrey Kolotov <qwest@altlinux.ru> 2.44.1-alt1
- new upstream version
- fix documentation bug in spec
- added package libyui-ncurses-doc
- package devel without documentation

* Mon Jul 29 2013 Andrey Kolotov <qwest@altlinux.ru> 2.44.0-alt1
- package devel with documentation
- uses curses5.9, must be changed to curses6
- release for AltLinux
