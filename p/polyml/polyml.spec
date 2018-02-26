%def_disable static

Name: polyml
Version: 5.4.1
Release: alt3

Summary: Standard ML implementation
Summary(ru_RU.UTF-8): Реализация Standard ML
License: %lgpl2plus
Group: Development/ML
Url: http://www.polyml.org

Packager: Yuriy Al. Shirokov <yushi@altlinux.org>
Source0: %name-%version.tar

Requires: lib%name = %version
BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Tue May 29 2012
# optimized out: fontconfig libICE-devel libSM-devel libX11-devel libXau-devel libXt-devel libstdc++-devel xorg-printproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ glibc-devel-static imake libXext-devel libgmp-devel libopenmotif-devel mt-st xorg-cf-files

%description
Poly/ML is a full implementation of Standard ML. Poly/ML supports the full version of the language as given in the "Definition of Standard ML (Revised)", generally known as ML97. As well as being extremely fast and efficient implementation of Standard ML Poly/ML provides several additional features. There is a foreign language interface which allows dynamically linked libraries to be loaded and functions within them called from ML. An X-Windows interface using Motif is available. There is also a symbolic debugger for Poly/ML.

%description -l ru_RU.UTF-8
Poly/ML — это быстрая и эффективная реализация языка Standard ML, поддерживающая все возможности стандарта "Definition of Standard ML (Revised)" (ML97). Кроме того, Poly/ML предоставляет разработчику интерфейс для вызова функций, написанных на других языках, библиотеку для создания графических интерфейсов на основе Motif и отладчик.

%package -n lib%name
Summary: Runtime library for PolyML
Group: Development/ML

%description -n lib%name
Runtime library for Poly/ML, a compiler for the Standard ML 

%if_enabled static
%package -n lib%name-static
Summary: Static runtime library for PolyML
Group: Development/ML

%description -n lib%name-static
Static files for Poly/ML runtime library.
%endif

%prep
%setup

%build
# Quick fix for RPATH bug
%autoreconf
%configure --with-x option
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc TODO.txt
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so*

%if_enabled static
%files -n lib%name-static
%_libdir/*.a
%endif

%changelog
* Sat Jun 02 2012 Yuriy Shirokov <yushi@altlinux.org> 5.4.1-alt3
- wrong russian description fixed

* Wed May 30 2012 Yuriy Shirokov <yushi@altlinux.org> 5.4.1-alt2
- spec bug with %_libdir/* fixed

* Sun May 27 2012 Yuriy Shirokov <yushi@altlinux.org> 5.4.1-alt1
- initial build
