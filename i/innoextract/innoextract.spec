Name: innoextract
Version: 1.4
Release: alt1.1

Summary: A tool to extract installers created by Inno Setup
License: Zlib
Url: http://constexpr.org/innoextract/
Group: Archiving/Compression

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Thu Oct 10 2013
# optimized out: boost-devel cmake-modules libstdc++-devel pkg-config python-base
#BuildRequires: boost-devel-headers boost-filesystem-devel boost-program_options-devel cmake doxygen gcc-c++ graphviz liblzma-devel python-module-distribute python-module-zope
BuildRequires: boost-devel-headers boost-filesystem-devel boost-program_options-devel cmake gcc-c++ liblzma-devel

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using wine.

%prep
%setup -q

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%files
%doc CHANGELOG LICENSE README.md VERSION
%_bindir/innoextract
%_man1dir/innoextract.*

%changelog
* Mon Feb 29 2016 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1.1
- NMU: rebuild with new boost

* Thu Oct 10 2013 Igor Zubkov <icesik@altlinux.org> 1.4-alt1
- build for Sisyphus

