Name: jpegpixi
Version: 1.1.1
Release: alt1.qa1

Summary: Command line tool to fix bad pixels in digital photos
Group: Graphics
License: GPL
URL: http://www.zero-based.org/software/jpegpixi/

Source: http://www.zero-based.org/software/jpegpixi/jpegpixi-%version.tar.gz

# Automatically added by buildreq on Fri Apr 07 2006
BuildRequires: libjpeg-devel

%description
"Jpegpixi" is short for "JPEG pixel interpolator". It is a command-line
utility which interpolates pixels in JFIF images (commonly refered to as
"JPEG images"). This is useful to correct images from a digital camera
with CCD defects.

%prep
%setup -q

%build
%configure
%make

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS
%_bindir/*
%_man1dir/*

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Apr 07 2006 Victor Forsyuk <force@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed Jun 15 2005 Victor Forsyuk <force@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Wed Oct 06 2004 Victor Forsyuk <force@altlinux.ru> 1.0.1-alt1
- Initial build for Sisyphus.
