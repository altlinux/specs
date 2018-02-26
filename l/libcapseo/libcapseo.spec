# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gtkdocize gcc-c++ imlib2-devel libXext-devel libaccounts-glib-devel libfreetype-devel pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) unzip zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define version 0.3.0
%define name libcapseo
%define capseo_version 0.3.0

# Tarfile created using git
# git clone git://gitorious.org/capseo/mainline.git libcapseo
# cd libcapseo
# git-archive --format=tar --prefix=libcapseo-%{capseo_version}/ %{git_version} | bzip2 > libcapseo-%{capseo_version}-%{gitdate}.tar.bz2

%define gitdate 20081031
%define git_version 431a293

%define tarfile %{name}-%{capseo_version}-%{gitdate}.tar.bz2
%define snapshot %{gitdate}git%{git_version}

Summary:        A realtime encoder/decoder library
Name:           libcapseo
Version:        %{capseo_version}
Release:        alt2_0.5.20081031git431a293
License:        GPLv3
Group:          System/Libraries
URL:            http://gitorious.org/projects/capseo/
BuildRequires:  libtool automake autoconf
BuildRequires:  libtheora-devel
BuildRequires:  libogg-devel
BuildRequires:  libX11-devel
BuildRequires:  libGL-devel

# Fedora specific snapshot no upstream release (yet)
Source0:        %{tarfile}
Source44: import.info

%description
Capseo is a realtime video codec being used by libcaptury/captury
for encoding captured video frames in realtime. (think of FRAPS codec).

Applications using capseo currently are libcaptury for encoding
captured data, e.g. currently from third-party OpenGL applications
via captury, the OpenGL video capturing tool.

%package devel
Summary: Files needed for development using %{name}
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Encoding/Decoding tools for capseo
Group: Video
Requires: %{name} = %{version}-%{release}

%description tools
Utilities for capseo

%prep
%setup -q -n %{name}-%{version}
./autogen.sh

%build
%configure --disable-static --enable-theora --disable-examples
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

rm -rf %{buildroot}/%{_libdir}/*.la

%files
%doc AUTHORS COPYING TODO
%{_libdir}/*.so.*

%files tools
%{_bindir}/*

%files devel
%{_includedir}/*.h
%{_libdir}/libcapseo.so
%{_libdir}/pkgconfig/capseo.pc

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_0.5.20081031git431a293
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_0.4.20081031git431a293
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_0.4.20081031git431a293
- initial import by fcimport

