%def_disable static

Name: librfxcodec
Version: 0.1.0
Release: alt1.git20150921

Summary: fast jpeg2000 codec compatible with MS RDP servers and xrdp

License: Apache2
Group: System/Libraries
Url: https://github.com/neutrinolabs/librfxcodec/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: nasm,chrpath

Packager: L.A. Kostis <lakostis@altlinux.ru>

%package -n %name-devel
Summary: %name development environment
Group: Development/C
Requires: %name = %version-%release

%package -n %name-devel-static
Summary: %name static development environment
Group: Development/C
Requires: %name-devel = %version-%release

%description
This is a fast jpeg2000 codec compatible with MS RDP servers and xrdp.

Assembly code in critial parts to maximize speed.

%description -n %name-devel
This package contains all files which are needs to compile programs using
the %name library.

%description -n %name-devel-static
This package contains libraries which are needs to compile programs statically
linked against %name library.

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
# unfortunately, asm code have EXEC stack status (
%set_verify_elf_method stack=relaxed
%makeinstall
chrpath -d %buildroot{%_libdir/*.so,%_bindir/*}

%files
%_bindir/*
%_libdir/*.so.*
%doc readme.txt

%files -n %name-devel
%_includedir/*
%_libdir/*.so

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Sep 21 2015 L.A. Kostis <lakostis@altlinux.ru> 0.1.0-alt1.git20150921
- inital build for ALTLinux.
