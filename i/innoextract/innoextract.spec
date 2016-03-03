Name:    innoextract
Version: 1.5
Release: alt1

Summary: A tool to extract installers created by Inno Setup
License: Zlib
Url:     http://constexpr.org/innoextract/
# VCS:   https://github.com/dscharrer/innoextract
Group:   Archiving/Compression

Source0: %name-%version.tar

Packager: Andrey Cherepanov <cas@altlinux.org>

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
%makeinstall_std

%files
%doc CHANGELOG LICENSE README.md VERSION
%_bindir/innoextract
%_man1dir/innoextract.*

%changelog
* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- New version

* Mon Feb 29 2016 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1.1
- NMU: rebuild with new boost

* Thu Oct 10 2013 Igor Zubkov <icesik@altlinux.org> 1.4-alt1
- build for Sisyphus

