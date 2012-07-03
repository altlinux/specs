Name: udis86
Version: 1.7
Release: alt1

Summary: Disassembler for x86 and x86-64
License: BSD
Group: Development/Other

URL: http://udis86.sourceforge.net/
Source: http://download.sourceforge.net/udis86/%name-%version.tar.gz

# Automatically added by buildreq on Wed Oct 06 2010
BuildRequires: gcc-c++

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

%build
%configure
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
%_includedir/*

%changelog
* Sun Oct 31 2010 Victor Forsiuk <force@altlinux.org> 1.7-alt1
- Initial build.
