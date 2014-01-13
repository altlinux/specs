Name:          libzim
Version:       1.0
Release:       alt1
Summary:       Library for reading/writing ZIM files

License:       GPLv2+
Group:         System/Libraries
URL:           http://openzim.org/wiki/Main_Page

Source0:       http://www.openzim.org/download/zimlib-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: liblzma-devel

%description
The zimlib is the standard implementation of the ZIM specification. It
is a library which implements the read and write method for ZIM files.
Use zimlib in your own software - like reader applications - to make
them ZIM-capable without the need having to dig too much into the ZIM
file format. zimlib is written in C++. It also includes the binaries
zimsearch and zimdump, for directly searching and viewing ZIM file
contents.

%package  devel
Summary:  Development files for %{name}
Group:    Development/Other
Requires: %name = %version-%release

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n zimlib-%version

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING 
%_bindir/zimdump
%_bindir/zimsearch
%_libdir/*.so.*

%files devel
%_includedir/zim/
%_libdir/*.so

%changelog
* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Import to ALT Linux from Fedora
