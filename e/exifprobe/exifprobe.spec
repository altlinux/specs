Name: exifprobe
Version: 2.0.1
Release: alt1

Summary: Shows the content and structure of cooked or raw digital camera images
License: BSD
Group: Graphics
URL: http://www.virtual-cafe.com/~dhh/tools.d/exifprobe.d/
Source: %url/exifprobe-%version.tar.gz

%description
Exifprobe reads images produced by digital cameras or similar devices and
reports their structure and the auxilliary data and metadata contained
within them. The program understands several image file formats, including
TIFF, JPEG, MRW, CIFF/CRW, JP2/JPEG2000, RAF, and X3F, and will read most
TIFF-derived formats including EXIF, DNG, ORF, CR2, NEF, K25, KDC, and PEF.

%prep
%setup -q

%build
%make_build CFLAGS="-DCOLOR %optflags"

%install
install -d $RPM_BUILD_ROOT{%_bindir,%_man1dir}

%__make install \
    PREFIX=$RPM_BUILD_ROOT%_prefix \
    BINDIR=$RPM_BUILD_ROOT%_bindir \
    MANDIR=$RPM_BUILD_ROOT%_man1dir

%files
%_bindir/*
%_man1dir/*
%doc ABOUT_PIM CAMERA_makes_and_models CREDITS DESCRIPTION MAKER_NOTES

%changelog
* Wed Aug 03 2005 Victor Forsyuk <force@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Tue Jul 12 2005 Victor Forsyuk <force@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Mon Apr 25 2005 Victor Forsyuk <force@altlinux.ru> 1.2.6-alt1
- Initial build.
