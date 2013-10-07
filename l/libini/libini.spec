
Name:           libini
Version:        1.1.10
Release:        alt1

Summary:        INI file parser library
License:        GPL
Group:          System/Libraries
URL:            http://libini.sourceforge.net/

Source:         %{name}-%{version}.tar.gz
Patch0:		fix-readInt-bug-types.i.patch
Patch1:		link-with-tcl-library.patch

BuildRequires:  gcc-c++ tcl-devel chrpath

%description
An INI file parser library that can read, edit and create large INI
files.  Usable under Microsoft Windows, DOS, Linux, etc. Supported
languages are C, C++, Visual Basic, Java, TCL, Perl, Python, etc
(DLL and SWIG capable).

Support for non standard comments, anonymous sections and autoparsing
of data lists.

%package devel
Summary:        Development headers and libraries for %{name}
Group:          Development/C++

%description devel
This package includes the header and library files necessary
for developing applications to use %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p2

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
# Fix RPATH
chrpath -d %buildroot%_libdir/libtclini.so.1.0.10

%files
%doc AUTHORS COPYING ChangeLog README TODO
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Oct 07 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.10-alt1
- Initial build in Sisyphus

