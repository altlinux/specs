Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison /usr/bin/flex /usr/bin/import /usr/bin/inkscape /usr/bin/kpsewhich /usr/bin/pandoc /usr/bin/xelatex perl(English.pm) perl(open.pm)
# END SourceDeps(oneline)
BuildRequires: chrpath
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ttfautohint
Version:        1.8.3
Release:        alt1_2
Summary:        Automated hinting utility for TrueType fonts
License:        FTL or GPLv2
URL:            http://www.freetype.org/ttfautohint
Source0:        http://download.savannah.gnu.org/releases/freetype/%{name}-%{version}.tar.gz

BuildRequires:  gcc gcc-c++
BuildRequires:  libfreetype-devel
BuildRequires:  libharfbuzz-devel libharfbuzz-utils
BuildRequires:  qt5-base-devel
Provides:       bundled(gnulib)
Requires:       %{name}-libs = %{version}-%{release}
Source44: import.info

%description
This is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

%package        gui
Group: File tools
Summary:        GUI for %{name} based on Qt
Requires:       %{name}-libs = %{version}-%{release}

%description    gui
%{name} is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

This is a GUI of %{name} based on Qt. 

%package        libs
Group: File tools
Summary:        Library for %{name}

%description    libs
lib%{name} is a library which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

%package        devel
Group: File tools
Summary:        Development files for %{name}-libs
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
lib%{name} is a library which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.


%prep
%setup -q

%build
%ifarch %e2k
# lcc 1.23.12 doesn't do __builtin_mul_overflow_p
# unlike gnulib expects from "gcc5"...
%add_optflags -D__ICC
%endif

%configure --disable-silent-rules --disable-static
%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done



%files
%doc AUTHORS NEWS README THANKS TODO *.TXT
%doc doc/img doc/ttfautohint.html
%doc doc/img doc/ttfautohint.pdf
%doc doc/img doc/ttfautohint.txt
%doc --no-dereference COPYING
%{_bindir}/ttfautohint

%files gui
%doc --no-dereference COPYING
#%{_docdir}/%{name}/
%{_bindir}/ttfautohintGUI

%files libs
%doc --no-dereference COPYING
%{_libdir}/libttfautohint.so.1*

%files devel
%doc --no-dereference COPYING
%{_includedir}/ttfautohint*.h
%{_libdir}/libttfautohint.so
%{_libdir}/pkgconfig/ttfautohint.pc

%changelog
* Sat Dec 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1_2
- merged e2k patch

* Mon Sep 02 2019 Michael Shigorin <mike@altlinux.org> 1.8.2-alt2_2
- E2K: gnulib ftbfs workaround

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_2
- new version

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

