Name: cvtool
Version: 1.0.0
Release: alt3

Summary: A simple image management, viewing, and printing program
License: GPLv2+
Group: Graphics

Url: http://cvtool.sourceforge.net/
Source: http://downloads.sourceforge.net/cvtool/cvtool-%version.tar.bz2

# Automatically added by buildreq on Tue Dec 27 2011 (-bi)
BuildRequires: chrpath libcairo-devel libglew-devel

%description
cvtool, a command line tool that aims to make all of CVL's functionality
available as filters. It integrates well with other tools like netpbm and
pfstools.

%package -n libcvl
Summary: Library for image and data processing using graphics processing units (GPUs)
Group: System/Libraries

%description -n libcvl
CVL is a library for image and data processing using graphics processing
units (GPUs).

It is suitable as a base for GPGPU applications (see http://www.gpgpu.org/).
CVL is based on OpenGL 2.1 and requires the GLEW library.

%package -n libcvl-devel
Summary: Development files of library for image and data processing using GPUs
Group: Development/C
Requires: libcvl = %version-%release

%description -n libcvl-devel
CVL is a library for image and data processing using graphics processing
units (GPUs).

It is suitable as a base for GPGPU applications (see http://www.gpgpu.org/).
CVL is based on OpenGL 2.1 and requires the GLEW library.

%prep
%setup

%build
%configure --disable-static
%make_build LIBS="-lrt -lm -lGL -lGLU -lGLEW -lX11"

%install
%makeinstall_std
chrpath --delete %buildroot%_bindir/cvtool

%files
%_bindir/*
%_man1dir/*
%_infodir/cvtool.info*
%exclude /usr/share/doc

%files -n libcvl
%_libdir/*.so.*

%files -n libcvl-devel
%_includedir/*
%_libdir/*.so
%_infodir/cvl.info*

%changelog
* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 1.0.0-alt3
- Fix RPATH issue.

* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 1.0.0-alt2
- Rebuilt for soname set-versions.
- Fix underlinking with libX11.

* Mon Mar 22 2010 Victor Forsiuk <force@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Jul 06 2009 Victor Forsyuk <force@altlinux.org> 0.2.6-alt1
- 0.2.6
- Fix wrong description of cvtool package.

* Fri Dec 12 2008 Victor Forsyuk <force@altlinux.org> 0.2.5-alt2
- Fix libcairo detect (bug spotted by Alexey Tourbin).
- Remove obsolete ldconfig calls.

* Wed Jul 30 2008 Victor Forsyuk <force@altlinux.org> 0.2.5-alt1
- 0.2.5

* Wed May 21 2008 Victor Forsyuk <force@altlinux.org> 0.2.4-alt1
- 0.2.4

* Thu Jan 24 2008 Victor Forsyuk <force@altlinux.org> 0.2.3-alt2
- Fix wrong URL.

* Mon Jan 21 2008 Victor Forsyuk <force@altlinux.org> 0.2.3-alt1
- Initial build.
