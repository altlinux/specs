Name: dtc
Version: 1.3.0
Release: alt1

Summary: Device Tree Compiler for Flat Device Trees
License: %gpl2plus
Group: Development/Tools
Url: http://git.jdl.com/gitweb/?p=dtc.git;a=summary

# git://git.jdl.com/software/dtc.git
Source: %name-%version.tar

Packager: Ivan Ovcherenko <asdus@altlinux.org>

BuildPreReq: rpm-build-licenses
BuildPreReq: flex
BuildPreReq: bison
BuildPreReq: texlive-base
BuildPreReq: texlive-latex-extra

%package -n libfdt
Summary: Flat Device Trees manipulation library
Group: System/Libraries

%package -n libfdt-devel
Summary: Flat Device Trees manipulation library - development files
Group: Development/C
Requires: libfdt = %version-%release

%package -n libfdt-doc
Summary: Documentation for Device Tree Compiler for Flat Device Trees 
Group: Development/Other
BuildArch: noarch
Requires: libfdt-devel = %version-%release

%description
Device Tree Compiler, dtc, takes as input a device-tree in a given
format and outputs a device-tree in another format for booting kernels
on embedded systems. Typically, the input format is "dts", a human
readable source format, and creates a "dtb", or binary format as output.

%description -n libfdt
This is a library containing functions for manipulating Flat Device
Trees.

%description -n libfdt-devel
This is a library containing functions for manipulating Flat Device
Trees.
This package contains the files needed for development against libfdt.

%description -n libfdt-doc
This is a library containing functions for manipulating Flat Device
Trees.
his package contains documentation for development against libfdt.

%prep
%setup

%build
%make_build
pushd Documentation
cp manual.txt dtc-manual.txt
latex dtc-paper.tex
dvips dtc-paper.dvi
pdflatex dtc-paper.tex
bzip2 -9 dtc-paper.dvi dtc-paper.ps dtc-paper.pdf dtc-manual.txt dts-format.txt
popd

%install
%makeinstall_std PREFIX=%_usr LIBDIR=%_libdir

%files
%doc README.license
%_bindir/*

%files -n libfdt
%doc README.license
%_libdir/libfdt-%version.so
%_libdir/libfdt.so.*

%files -n libfdt-devel
%doc README.license
%_libdir/libfdt.so
%_includedir/*

%files -n libfdt-doc
%doc README.license Documentation/dtc-paper.dvi.bz2 Documentation/dtc-paper.ps.bz2 Documentation/dtc-paper.pdf.bz2 Documentation/dtc-manual.txt.bz2 Documentation/dts-format.txt.bz2

%changelog
* Mon Dec 24 2012 Ivan Ovcherenko <asdus@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux Sisyphus, v1.3.0-e4b497f

