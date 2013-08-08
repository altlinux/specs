Name:		libyui-qt
Version:	2.43.5
Release:	alt1
License:	%lgpl21only or %lgpl3only
Source:		libyui-qt-%{version}.tar
Group:		System/Libraries
Packager:       Andrey Kolotov <qwest@altlinux.org>

BuildPreReq:    rpm-build-licenses

BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	gcc-c++
BuildRequires:	pkg-config

BuildRequires:	libyui-devel >= 3.0.10
BuildRequires:	libqt4-devel
BuildRequires:	doxygen fdupes graphviz texmf-latex-beamer
BuildRequires:  fonts-ttf-core

URL:		http://github.com/libyui/
Summary:	Libyui - Qt User Interface

%description
This package contains the Qt user interface
component for libYUI.


%package -n libyui-qt5

Group:		System/Libraries
Requires:	libyui5
Provides:	libyui-qt = %{version}

Summary:	Libyui - Qt User Interface

%description -n libyui-qt5
This package contains the Qt user interface
component for libYUI.


%package devel

Group:		Development/C++

Requires:	libyui-qt5 = %{version}
Requires:	libyui-devel >= 3.0.10

Summary:	Libyui-qt header files

%description devel
This package contains the Qt user interface
component for libYUI.

This can be used independently of YaST for generic (C++) applications.
This package has very few dependencies.


%package doc

Group:		Documentation

Requires:       libyui-qt5 = %{version}
Requires:       fonts-ttf-core

Summary:        Libyui-qt documentation

%description doc
This package contains the Qt user interface
component for libYUI.

This package provides the documentation. (HTML & PDF)


%prep
%setup -q -n libyui-qt-%{version}


%build

CFLAGS="${CFLAGS:-%optflags}"; export CFLAGS;
CXXFLAGS="${CXXFLAGS:-%optflags}"; export CXXFLAGS;

./bootstrap.sh %{_prefix}

mkdir build
cd build

cmake .. \
	-DPREFIX=%{_prefix} \
	-DDOC_DIR=%{_docdir} \
	-DLIB_DIR=%{_lib} \
	-DINSTALL_DOCS=ON \
	-DCMAKE_BUILD_TYPE=RELEASE

make docs


%install
cd build
%makeinstall_std
install -m0755 -d %buildroot/%{_docdir}/libyui-qt5/
install -m0755 -d %buildroot/%{_libdir}/yui
install -m0644 ../COPYING* %buildroot/%{_docdir}/libyui-qt5/
fdupes -s %buildroot/%_docdir/libyui-qt5

%files -n libyui-qt5
%defattr(-,root,root)
%dir %{_libdir}/yui
%{_libdir}/yui/lib*.so.*
%doc %dir %{_docdir}/libyui-qt5
%doc %{_docdir}/libyui-qt5/COPYING*

%files devel
%defattr(-,root,root)
%dir %{_docdir}/libyui-qt5
%{_libdir}/yui/lib*.so
%{_prefix}/include/yui
%{_libdir}/pkgconfig/libyui-qt.pc
%{_libdir}/cmake/libyui-qt

%files doc
%doc %{_docdir}/libyui-qt5
%exclude %{_docdir}/libyui-qt5/COPYING*

%changelog
* Thu Aug 8 2013 Andrey Kolotov <qwest@altlinux.org> 2.43.5-alt1
- upstream version
