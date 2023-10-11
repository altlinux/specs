Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison /usr/bin/flex /usr/bin/import /usr/bin/inkscape /usr/bin/kpsewhich /usr/bin/pandoc /usr/bin/xelatex
# END SourceDeps(oneline)
BuildRequires: chrpath
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# RHEL 10 is dropping Qt5
#bcond gui 1
%define with_gui 1

Name:           ttfautohint
Version:        1.8.4
Release:        alt1_7
Summary:        Automated hinting utility for TrueType fonts
License:        FTL or GPL-2.0-only
URL:            http://www.freetype.org/ttfautohint
Source0:        http://download.savannah.gnu.org/releases/freetype/%{name}-%{version}.tar.gz

BuildRequires:  autoconf automake libtool
BuildRequires:  gcc gcc-c++
BuildRequires:  libfreetype-devel
BuildRequires:  libharfbuzz-devel libharfbuzz-gir-devel libharfbuzz-utils
%if %{with gui}
BuildRequires:  qt5-base-devel
%endif
Provides:       bundled(gnulib)
Requires:       %{name}-libs = %{version}-%{release}
Source44: import.info

%description
This is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

%if %{with gui}
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
%endif

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

# drop this hack if --with-doc is enabled
echo %{version} > VERSION
sed -i -e '/dist_man_MANS/d' -e 's/manpages/dist_man_MANS/' frontend/local.mk
autoreconf -fiv

%build
%ifarch %e2k
# lcc 1.23.12 doesn't do __builtin_mul_overflow_p
# unlike gnulib expects from "gcc5"...
%add_optflags -D__ICC
%endif

# doc: requires help2man, ImageMagick, inkscape, pandoc, xelatex, xvfb-run
%configure \
  --disable-silent-rules --disable-static --without-doc \
  %{!?with_gui:--without-qt}
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
%{_mandir}/man1/ttfautohint.1*

%if %{with gui}
%files gui
%doc --no-dereference COPYING
%{_bindir}/ttfautohintGUI
%{_mandir}/man1/ttfautohintGUI.1*
%endif

%files libs
%doc --no-dereference COPYING
%{_libdir}/libttfautohint.so.1*

%files devel
%doc --no-dereference COPYING
%{_includedir}/ttfautohint*.h
%{_libdir}/libttfautohint.so
%{_libdir}/pkgconfig/ttfautohint.pc

%changelog
* Wed Oct 11 2023 Igor Vlasenko <viy@altlinux.org> 1.8.4-alt1_7
- update

* Mon Oct 25 2021 Igor Vlasenko <viy@altlinux.org> 1.8.4-alt1_1
- update to new release by fcimport

* Sat Dec 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1_2
- merged e2k patch

* Mon Sep 02 2019 Michael Shigorin <mike@altlinux.org> 1.8.2-alt2_2
- E2K: gnulib ftbfs workaround

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_2
- new version

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

