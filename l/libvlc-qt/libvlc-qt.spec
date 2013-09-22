%def_with doc

Name: libvlc-qt
Version: 0.8.0
Release: alt1
Summary: VLC-Qt Library
License: LGPLv3
Group: System/Libraries
URL: http://projects.tano.si/library
Source: %name-%version.tar

BuildRequires: gcc-c++ %{?_with_doc:doxygen}
BuildRequires: cmake >= 2.8.6
BuildRequires: libqt4-devel >= 4.8
BuildRequires: libvlc-devel >= 2.0

%description
VLC-Qt is a free library used to connect Qt and libvlc libraries. It contains
core classes for main media playback and also some GUI classes for faster media
player developement.


%package devel
Summary: Files for development with VLC-Qt Library
Group: Development/C++
Requires: %name = %version-%release

%description devel
VLC-Qt is a free library used to connect Qt and libvlc libraries. It contains
core classes for main media playback and also some GUI classes for faster media
player developement.
This package contains files for development with VLC-Qt Library.


%package doc
Summary: Documentation for development with VLC-Qt Library
Group: Development/Documentation
BuildArch: noarch

%description doc
VLC-Qt is a free library used to connect Qt and libvlc libraries. It contains
core classes for main media playback and also some GUI classes for faster media
player developement.
This package contains HTML documentatio for development with VLC-Qt Library.


%prep
%setup -q


%build
%cmake_insource
%make_build -j1
%{?_with_doc:cd doc && doxygen}


%install
%makeinstall_std
install -pD -m 0644 README.md %buildroot%_docdir/%name-%version/README
install -p -m 0644 AUTHORS CHANGELOG %buildroot%_docdir/%name-%version/
%{?_with_doc:cp -a doc/html %buildroot%_docdir/%name-%version/}


%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/AUTHORS
%_libdir/*.so.*


%files devel
%doc %_docdir/%name-%version/CHANGELOG
%doc %_docdir/%name-%version/README
%_includedir/*
%_pkgconfigdir/*
%_libdir/*.so


%if_with doc
%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/html
%endif


%changelog
* Sun Sep 22 2013 Led <led@altlinux.ru> 0.8.0-alt1
- initial build
