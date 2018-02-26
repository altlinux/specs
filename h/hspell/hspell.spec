Name: hspell
Version: 1.2
Release: alt1
Summary: A Hebrew spell checker
License: GPLv2
Group: Text tools
Url: http://hspell.ivrix.org.il/
# http://hspell.ivrix.org.il/%name-%version.tar.gz
Source: %name-%version.tar
Patch: hspell-1.2-alt-fixes.patch
Requires: lib%name = %version-%release
BuildRequires: libhunspell-devel hunspell-utils zlib-devel

%description
Hspell is a Hebrew SPELLer and morphological analyzer.  It provides a
mostly spell-like interface (gives the list of wrong words in the input
text), but can also suggest corrections (-c).  It also provides a true
morphological analyzer (-l), that prints all known meanings of a Hebrew
string.

%package common
Summary: Hspell common files
Group: Text tools
BuildArch: noarch

%description common
Hspell is a Hebrew SPELLer and morphological analyzer.
This package contains Hspell common files.

%package data
Summary: Hspell data files
Group: Text tools
BuildArch: noarch
Requires: %name-common = %version-%release

%description data
Hspell is a Hebrew SPELLer and morphological analyzer.
This package contains Hspell data files.

%package -n lib%name
Summary: Hspell shared library
Group: System/Libraries
Requires: %name-common = %version-%release

%description -n lib%name
Hspell is a Hebrew SPELLer and morphological analyzer.
This package contains Hspell shared library.

%package -n lib%name-devel
Summary: Development library and include files for Hspell
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Hspell is a Hebrew SPELLer and morphological analyzer.
This package contains development library and include files.

%package -n hunspell-he
Summary: Hebrew hunspell dictionaries
Group: Text tools
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: hunspell

%description -n hunspell-he
Hebrew hunspell dictionaries.

%prep
%setup
%patch -p1
iconv -f hebrew -t utf8 -o WHATSNEW WHATSNEW

%build
autoconf
%configure --enable-fatverb --enable-linginfo --enable-shared
make STRIP=:
make hunspell

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/myspell
cp -p he.dic %buildroot%_datadir/myspell/he_IL.dic
cp -p he.aff %buildroot%_datadir/myspell/he_IL.aff
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
install -pm644 LICENSE README WHATSNEW %buildroot%docdir/

%files
%_bindir/*
%_man1dir/*

%files common
%docdir/

%files data
%_datadir/%name/

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/lib*.so
%_man3dir/*

%files -n hunspell-he
%_datadir/myspell/*

%changelog
* Mon Apr 02 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Updated to 1.2.

* Fri Jul 15 2011 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Initial release for ALT Linux, based on hspell-1.1-4 from Fedora.
