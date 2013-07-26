Name:		libyui
Version:	3.0.9
Release:	alt1
License:	%lgpl21only or %lgpl3only
Source:		libyui-%{version}.tar
Group:		System/Libraries
Packager:	Andrey Kolotov <qwest@altlinux.ru>

BuildPreReq:	rpm-build-licenses

BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	gcc-c++
BuildRequires:	pkg-config
BuildRequires:  doxygen fdupes graphviz texmf-latex-beamer
BuildRequires:	fonts-ttf-core

URL:		http://github.com/libyui/
Summary:	GUI-abstraction library

%description
This is the user interface engine that provides the abstraction from
graphical user interfaces (Qt, Gtk) and text based user interfaces
(ncurses).

Originally developed for YaST, it can now be used independently of
YaST for generic (C++) applications. This package has very few
dependencies.

%package -n libyui5

Group:		System/Libraries

Provides:	yast2-libyui = 2.42.0
Obsoletes:	yast2-libyui < 2.42.0

Summary:	Libyui - GUI-abstraction library

%description -n libyui5
This is the user interface engine that provides the abstraction from
graphical user interfaces (Qt, Gtk) and text based user interfaces
(ncurses).

Originally developed for YaST, it can now be used independently of
YaST for generic (C++) applications. This package has very few
dependencies.


%package devel

Group:		Development/C++

Requires:	libyui5 = %{version}
Requires:	glibc-devel
Requires:	libstdc++-devel
Requires:	boost-devel
Requires:	fonts-ttf-core

Summary:	Libyui header files

%description devel
This is the user interface engine that provides the abstraction from
graphical user interfaces (Qt, Gtk) and text based user interfaces
(ncurses).

Originally developed for YaST, it can now be used independently of
YaST for generic (C++) applications. This package has very few
dependencies.

This can be used independently of YaST for generic (C++) applications.
This package has very few dependencies and provides the documentation
(HTML & PDF).

%prep
%setup -q -n libyui-%{version}


%build

./bootstrap.sh

CFLAGS="${CFLAGS:-%optflags}"; export CFLAGS;
CXXFLAGS="${CXXFLAGS:-%optflags}"; export CXXFLAGS;

mkdir build
cd build

cmake .. \
	-DPREFIX=%{_prefix} \
	-DDOC_DIR=%{_docdir} \
	-DLIB_DIR=%{_lib} \
	-DCMAKE_BUILD_TYPE=RELEASE

make docs


%install
cd build
%makeinstall_std
install -m0755 -d %buildroot/%{_docdir}/libyui5/
install -m0755 -d %buildroot/%{_libdir}/yui
install -m0644 ../COPYING* %buildroot/%{_docdir}/libyui5/
fdupes -s %buildroot/%_docdir/libyui5


%files -n libyui5
%defattr(-,root,root)
%dir %{_libdir}/yui
%dir %{_datadir}/libyui
%{_libdir}/lib*.so.*
%doc %dir %{_docdir}/libyui5
%doc %{_docdir}/libyui5/COPYING*

%files devel
%defattr(-,root,root)
%dir %{_docdir}/libyui5
%{_libdir}/lib*.so
%{_prefix}/include/yui
%{_libdir}/pkgconfig/libyui.pc
%{_libdir}/cmake/libyui
%{_datadir}/libyui/buildtools
%doc %{_docdir}/libyui5
%exclude %{_docdir}/libyui5/COPYING*

%changelog
* Fri Jul 26 2013 Andrey Kolotov <qwest@altlinux.ru> 3.0.9-alt1
- package devel with documentation
- release for AltLinux
