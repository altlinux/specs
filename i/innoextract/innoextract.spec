Name:    innoextract
Version: 1.8
Release: alt2

Summary: A tool to extract installers created by Inno Setup
License: Zlib
Url:     http://constexpr.org/innoextract/
# VCS:   https://github.com/dscharrer/innoextract
Group:   Archiving/Compression

Source0: %name-%version.tar
Patch1: %name-%version-alt-boost-compat.patch

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: boost-devel-headers boost-filesystem-devel boost-program_options-devel cmake gcc-c++ liblzma-devel

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using wine.

%prep
%setup -q
%patch1 -p1

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
* Fri Nov 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8-alt2
- Rebuilt with boost-1.71.0.

* Mon Sep 16 2019 Andrey Cherepanov <cas@altlinux.org> 1.8-alt1
- New version.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.7-alt1
- New version.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6-alt1.1
- NMU: rebuilt with boost-1.67.0

* Mon Apr 11 2016 Andrey Cherepanov <cas@altlinux.org> 1.6-alt1
- New version

* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- New version

* Mon Feb 29 2016 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1.1
- NMU: rebuild with new boost

* Thu Oct 10 2013 Igor Zubkov <icesik@altlinux.org> 1.4-alt1
- build for Sisyphus

