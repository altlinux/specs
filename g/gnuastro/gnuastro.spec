%set_verify_info_method relaxed
#set_verify_elf_method textrel=relaxed
%define sover 15

Name: gnuastro
Version: 0.21
Release: alt1
Summary: GNU Astronomy Utilities
License: GPLv3+
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: Sciences/Other
Url: https://www.gnu.org/software/gnuastro/
Source: https://ftp.gnu.org/pub/gnu/gnuastro/%name-%version.tar.gz
Source2: https://ftp.gnu.org/pub/gnu/gnuastro/%name-%version.tar.gz.sig
Source3: https://akhlaghi.org/public-pgp-key.txt#/%name.keyring
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(wcslib)
Requires: %name-doc curl ghostscript >= 9.10

%description
The GNU Astronomy Utilities (Gnuastro) contains various programs and
library functions for the manipulation and analysis of astronomical
data.

%package -n libgnuastro%sover
Summary: Libraries for the GNU Astronomy Utilities
Group: Sciences/Other
%description -n libgnuastro%sover
Libraries for the manipulation and analysis of astronomical data,
part of the GNU Astronomy Utilities (Gnuastro).

%package devel
Summary: Development files for gnuastro
Requires: libgnuastro%sover = %version
Group: Sciences/Other
%description devel
Development files required for development with GNU Astronomy
Utilities (Gnuastro).

%package doc
Summary: Documentation for the GNU Astromomy Utilities
BuildArch: noarch
Group: Sciences/Other
%description doc
Additional documentation for the GNU Astromomy Utilities.

%package bash-completion
Summary: Bash completion for %name
Group: Shells
Requires: bash-completion %name
BuildArch: noarch

%description bash-completion
Bash command line completion support for %name

%prep
%setup

%build
%autoreconf 
%configure \
	--docdir=%_docdir/%name \
	--disable-static \
	--disable-rpath \
	CPPFLAGS="$(pkg-config cfitsio --cflags)"
%make_build

%install
%makeinstall_std
#find %buildroot -type f -name "*.la" -delete -print
mkdir -p %buildroot/%_datadir/bash-completion/completions
mv -v %buildroot/%_datadir/%name/completion.bash %buildroot/%_datadir/bash-completion/completions/%name

%check

%make_build check


%files
%doc ChangeLog README NEWS THANKS AUTHORS
%config %_sysconfdir/*.conf
%_bindir/*
%_datadir/gnuastro
%_man1dir/*

%files -n libgnuastro%sover
%_libdir/libgnuastro.so.*

%files devel
%_includedir/gnuastro
%_libdir/libgnuastro.so
%_libdir/pkgconfig/*.pc

%files doc
%_infodir/gnuastro.info*.xz
%_infodir/gnuastro-figures

%files bash-completion
%_datadir/bash-completion/completions/%name

%changelog
* Mon Oct 23 2023 Ilya Mashkin <oddity@altlinux.ru> 0.21-alt1
- 0.21

* Sun May 07 2023 Ilya Mashkin <oddity@altlinux.ru> 0.20-alt1
- 0.20

* Sat Oct 29 2022 Ilya Mashkin <oddity@altlinux.ru> 0.19-alt1
- 0.19

* Sat Jul 30 2022 Ilya Mashkin <oddity@altlinux.ru> 0.18-alt1
- 0.18

* Fri Apr 08 2022 Ilya Mashkin <oddity@altlinux.ru> 0.17-alt1
- Build for Sisyphus based on suse spec

* Sun Mar 20 2022 Andreas Stieger <andreas.stieger@gmx.de>
- GNU Astronomy Utilities 0.17 (library 15.0.0):
  * New program astscript-fits-view: Given any number of FITS files
    this script will either open SAO DS9 (for 2D images or 3D
    cubes) or TOPCAT (for tables) to visualize their contents in a
    graphic user interface (GUI).
  * add a set of installed scripts to enable easy estimation and
    subtraction of the extended PSF (astscript-psf-*)
  * Coordinate-related columns in all programs now also accept
    sexagesimal values, not just degrees
  * Columns of FITS tables can now be read in parallel
  * multiple new operations and options
  * Some operations and options were renamed
  * A number of bug fixes
* Mon Oct 11 2021 Andreas Stieger <andreas.stieger@gmx.de>
- GNU Astronomy Utilities 0.16 (library 14.0.0):
  * documentation updates
  * Arithmetic: New operands
    + box-around-ellipse: width and height of the box covering an ellipse
    + au-to-pc: Convert Astronomical Units (AUs) to Parsecs (PCs)
    + pc-to-au: Convert Parsecs (PCs) to Astronomical Units (AUs)
    + ly-to-pc: Convert Light-years (LYs) to Parsecs (PCs)
    + pc-to-ly: Convert Parsecs (PCs) to Light-years (LYs)
    + ly-to-au: Convert Light-years (LYs) to Astronomical Units (AUs)
    + au-to-ly: Convert Astronomical Units (AUs) to Light-years (LYs)
  * CosmicCalculator: warn if the requested redshift is < 0.007
  * MakeCatalog:
    + --areaerror: spatial resolution of image specified by user,
    used in estimating the surface brightness error
    + --sberror: error in measuring the surface brightness
    (mag/arcsec^2)
  * MakeProfiles: New type of profile showing the azimuthal angle
    (in degrees, along the elliptical circumference of fixed radius)
    of each pixel.
  * Match: add support for printing rows that could notbe matched
  * Statistics: add --quantofmean: the quantile of the mean of the
    input dataset
  * --stdintimeout: default value changed from 0.1 seconds to 1.5s
  * MakeProfiles: The default output suffix  is now '_profiles.fits'
  * many bug fixes
- drop gnuastro-cfitsio-version-format-change.patch
* Wed Aug 18 2021 Atri Bhattacharya <badshah400@gmail.com>
- Add gnuastro-cfitsio-version-format-change.patch -- accounts for
  3 number version string for CFITSIO; patch taken from upstream
  commit.
* Wed Jun  2 2021 Andreas Stieger <andreas.stieger@gmx.de>
- GNU Astronomy Utilities 0.15 (library 13.0.0):
  * New programs: astscript-ds9-region, astscript-radial-profile
  * Recognized FITS files even without a FITS suffix
  * --wcslinearmatrix: new option in all programs to select the
    output WCS linear matrix format
  * documentation updates
  * New arithmetic operators
  * --envseed: new option to get random number generator settings
    for the new 'mknoise-sigma' and 'mknoise-poisson' operators
    from the environment for reproducibility
  * New and updated options to multiple operations
  * Extended support for 3d datacubes
  * The default end to a "night" is set to 11:00a.m
  * Bug fixes
  * now supports bash completion
* Sat Jan 30 2021 Andreas Stieger <andreas.stieger@gmx.de>
- GNU Astronomy Utilities 0.14 (library 12.0.0):
  * new program Query ('astquery') to query to external datasets
    and retrieve the resulting datasets from the command-line.
    The package now recommends curl for this purpose.
  * Gnuastro programs will first attempt to write the array in RAM,
    only when it fails will they use a memory-mapped file.
    Directory changes from .gnuastro_mmap to gnuastro_mmap
  * Various documentation updates, extensions and fixes
- remove obsolete texinfo packaging macros
* Sat Sep 12 2020 Andreas Stieger <andreas.stieger@gmx.de>
- GNU Astronomy Utilities 0.13 (library 11.0.0):
  * more relaxed input format for plain-text tables
  * New operations to fill blanks with minimum/maximum of nearest
    neighbors
  * Input can be forced to float by appending '.' or '.0'.
  * New colormap 'sls-inverse' for inverse printing
  * Many new operations to multiple operations, and bug fixes
- includes changes from 0.12:
  * no longer attempt to write memory-mapped files under .gnuastro
    to avoid mixing configuration files with processing data
  * Many new operations to multiple operations, and bug fixes
* Tue Nov 26 2019 Andreas Stieger <andreas.stieger@gmx.de>
- GNU Astronomy Utilities 0.11 (library 9.0.0):
  * documentation updates
  * Updates and extensions to multiple operations
- drop upstreamed patch
  0001-Reference-wcslib-by-correct-name-in-gnuastro.pc-pkgc.patch
* Sun Nov 10 2019 Stefan Brüns <stefan.bruens@rwth-aachen.de>
- Fix wrong automatic pkgconfig(wcs) requires, add
  0001-Reference-wcslib-by-correct-name-in-gnuastro.pc-pkgc.patch
- Drop ghostscript BuildRequires, only needed for running tests
  (not done), the PDF exporter is built unconditionally. At runtime,
  the exporter uses a "gs" executable in PATH, so add a Recommends.
- Add bcond for running tests, keep it disabled by default.
* Sun Nov  3 2019 Andreas Stieger <andreas.stieger@gmx.de>
- GNU Astronomy Utilities 0.10 (library 8.0.0):
  * Report/warn when using arrays memory-mapped to non-volatile
    storage. Users should use --minmapsize to allow use of available
    RAM, --quietmmap' option to disable the messages
  * Various additions and extensions to operators and tools
  * crop now supports 3D datasets (data cubes)
  * documentation updates and bug fixes
- includes changes from 0.9:
  * --checkconfig: print the names and values given to options as
    they are parsed on the command-line or in various configuration
    files
  * Multithreaded operation for many operators
  * Add bash scripts for common higher-level usage
* Fri Dec 28 2018 astieger@suse.com
- update to 0.8:
  * various improvements to input/output handling of all programs
  * Various functional updates and fixes to multiple commands
  * NoiseChisel: New outlier identification algorithm for quantile
    thresholds
* Sun Aug 12 2018 jengelh@inai.de
- Use pkg-config instead of hardcoding the cfitsio path.
- Wrap descriptions consistently.
- Fix RPM group of shared library subpackage.
* Sat Aug 11 2018 astieger@suse.com
- initial package (0.7)
