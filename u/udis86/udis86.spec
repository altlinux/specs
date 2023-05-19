%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: udis86
Version: 1.7.2
Release: alt2

Summary: Disassembler for x86 and x86-64
License: BSD
Group: Development/Other

URL: http://udis86.sourceforge.net/
Source: http://download.sourceforge.net/udis86/%name-%version.tar.gz

Patch0: udis86-1.7.2-pkgconfig.patch

# Automatically added by buildreq on Wed Oct 06 2010
BuildRequires: gcc-c++
BuildRequires: python3

%description
Udis86 is an easy-to-use minimalistic disassembler library for the x86 and
x86-64 instruction set architectures. The primary intent of the design and
development of udis86 is to aid software development projects that entail
binary code analysis.

%package -n lib%{name}-devel-static
Summary: Disassembler library for the x86 and x86-64 instruction set architectures
Group: System/Libraries

%description -n lib%{name}-devel-static
Disassembler library for the x86 and x86-64 instruction set architectures.

%package -n lib%{name}-devel
Summary: Disassembler library for the x86 and x86-64, development files
Group: Development/C
Requires: lib%{name}-devel-static = %version-%release

%description -n lib%{name}-devel
Disassembler library for the x86 and x86-64 instruction set architectures.

%package doc
Summary: Documentation for x86 and x86-64 disassembler
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for x86 and x86-64 disassembler.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --with-python=%__python3
%make_build

%install
%makeinstall_std docdir=%_docdir/%name-%version

%files
%_bindir/*

%files doc
%_docdir/%name-%version

%files -n lib%{name}-devel-static
%_libdir/*.a

%files -n lib%{name}-devel
%_pkgconfigdir/%name.pc
%_includedir/*

%changelog
* Sun May 14 2023 Roman Alifanov <ximper@altlinux.org> 1.7.2-alt2
- add pkgconfig and remove noarch for devel subpackage

* Fri Nov 12 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.7.2-alt1
- 1.7.2

* Fri Oct 29 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.7-alt2
- NMU: FTBFS: build with LTO.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.7-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Oct 31 2010 Victor Forsiuk <force@altlinux.org> 1.7-alt1
- Initial build.
