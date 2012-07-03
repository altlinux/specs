Name: libwebp
Version: 0.1.3
Release: alt1

Summary: Library and tools for the WebP graphics format
License: BSD
Group: System/Libraries

URL: http://webmproject.org/
Source: http://webp.googlecode.com/files/%name-%version.tar.gz

# Automatically added by buildreq on Wed Jul 13 2011
BuildRequires: libjpeg-devel libpng-devel

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package devel
Summary: Development files for libwebp, a library for the WebP format
Group: Development/C
Requires: %name = %version-%release

%description devel
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package tools
Summary: The WebP command line tools
Group: System/Libraries

%description tools
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files tools
%_bindir/*
%_man1dir/*

%changelog
* Mon Jan 09 2012 Victor Forsiuk <force@altlinux.org> 0.1.3-alt1
- 0.1.3

* Wed Jul 13 2011 Victor Forsiuk <force@altlinux.org> 0.1.2-alt1
- Initial build.
