%def_without docs

Name: dtc
Version: 1.4.1
Release: alt1

Summary: Device Tree Compiler for Flat Device Trees
License: %gpl2plus
Group: Development/Tools
Url: https://git.kernel.org/cgit/utils/dtc/dtc.git

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses
BuildRequires: flex bison
%if_with docs
BuildRequires: texlive-base texlive-latex-extra
%endif

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
%if_with docs
pushd Documentation
latex dtc-paper.tex
dvips dtc-paper.dvi
pdflatex dtc-paper.tex
bzip2 -9 dtc-paper.dvi dtc-paper.ps dtc-paper.pdf
popd
%endif

%install
%makeinstall_std PREFIX=%_usr LIBDIR=%_libdir

%files
%doc README.license
%doc Documentation/manual.txt
%doc Documentation/dts-format.txt
%_bindir/*

%files -n libfdt
%doc README.license
%_libdir/libfdt-%version.so
%_libdir/libfdt.so.*

%files -n libfdt-devel
%doc README.license
%_libdir/libfdt.so
%_includedir/*

%if_with docs
%files -n libfdt-doc
%doc README.license
%doc Documentation/dtc-paper.dvi.bz2
%doc Documentation/dtc-paper.ps.bz2
%doc Documentation/dtc-paper.pdf.bz2
%endif

%changelog
* Fri Feb 06 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1 released

* Wed Dec 25 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released

* Thu Dec 27 2012 Ivan Ovcherenko <asdus@altlinux.org> 1.3.0-alt2
- Increase package version due the ugly correlation with package version
  in the FC AutoImports repository.

* Mon Dec 24 2012 Ivan Ovcherenko <asdus@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux Sisyphus, v1.3.0-e4b497f
