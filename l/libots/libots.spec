%set_automake_version 1.10

Name: libots
Version: 0.5.0
Release: alt4

Summary: A text summarizer
License: GPLv2+
Group: System/Libraries

URL: http://libots.sourceforge.net/
Source: http://dl.sourceforge.net/libots/ots-%version.tar.gz

# Automatically added by buildreq on Tue Jan 25 2011
BuildRequires: docbook-utils glib2-devel gtk-doc libpopt-devel libxml2-devel

%description
Open Text Summarizer is an open source tool for summarizing texts.
It reads a text stream and decides which sentences are important and
which are not.
 
%package devel
Summary: Libraries and include files for developing with libots
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with libots.

%prep
%setup -n ots-%version

%build
touch ./gtk-doc.make
%autoreconf
%configure --disable-gtk-doc --disable-static

# SMP unsafe build :(
%make

%install
%makeinstall_std

%files
%_bindir/ots
%_libdir/*.so.*
%_datadir/ots

%files devel
%doc README
%_libdir/*.so
%_includedir/libots-1
%_pkgconfigdir/*.pc

%changelog
* Tue Jan 25 2011 Victor Forsiuk <force@altlinux.org> 0.5.0-alt4
- Rebuilt for soname set-versions.

* Thu Jul 09 2009 Victor Forsyuk <force@altlinux.org> 0.5.0-alt3
- Fix FTBFS (add libtoolize call, use automake 1.10).

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 0.5.0-alt2
- Remove obsolete ldconfig calls.

* Sun Aug 10 2008 Victor Forsyuk <force@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue May 23 2006 Victor Forsyuk <force@altlinux.ru> 0.4.2-alt3
- Fix FTBFS with gcc4.

* Tue Mar 21 2006 Victor Forsyuk <force@altlinux.ru> 0.4.2-alt2
- Fix linking.

* Fri Jun 10 2005 Victor Forsyuk <force@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Fri Sep 19 2003 AEN <aen@altlinux.ru> 0.4.1-alt1
- based on RH spec
