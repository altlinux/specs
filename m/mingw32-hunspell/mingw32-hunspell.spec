BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:          mingw32-hunspell
Summary:       MinGW Windows spell checker and morphological analyzer library
Version:       1.2.12
Release:       alt1_4
Source0:       http://downloads.sourceforge.net/hunspell/hunspell-%{version}.tar.gz
Group:         System/Libraries
URL:           http://hunspell.sourceforge.net/
License:       LGPLv2+ or GPLv2+ or MPLv1.1

BuildArch:     noarch
BuildRequires: bison
BuildRequires: gettext
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gettext
BuildRequires: mingw32-readline
Requires:      pkgconfig
Source44: import.info

%description
Hunspell is a spell checker and morphological analyzer library and program 
designed for languages with rich morphology and complex word compounding or 
character encoding. Hunspell interfaces: Ispell-like terminal interface using 
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

This is the MinGW build of Hunspell


%package static
Summary:        Static version of the MinGW Windows hunspell library
Requires:       %{name} = %{version}-%{release}
Group:          System/Libraries

%description static
Static version of the MinGW Windows hunspell spell checking library.


%{?_mingw32_debug_package}


%prep
%setup -qn "hunspell-%{version}"

# Some files aren't UTF-8
for i in AUTHORS.myspell; do
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    mv -f $i.new $i
done


%build
%{_mingw32_configure} --enable-static --enable-shared --with-ui --with-readline --enable-threads=win32
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install

# Drop the man pages
rm -rf $RPM_BUILD_ROOT%{_mingw32_datadir}/man

%find_lang hunspell


%files -f hunspell.lang
%doc README README.myspell COPYING COPYING.LGPL COPYING.MPL AUTHORS AUTHORS.myspell license.hunspell license.myspell THANKS
%{_mingw32_bindir}/i586-pc-mingw32-affixcompress
%{_mingw32_bindir}/i586-pc-mingw32-analyze.exe
%{_mingw32_bindir}/i586-pc-mingw32-chmorph.exe
%{_mingw32_bindir}/i586-pc-mingw32-hunspell.exe
%{_mingw32_bindir}/i586-pc-mingw32-hunzip.exe
%{_mingw32_bindir}/i586-pc-mingw32-hzip.exe
%{_mingw32_bindir}/i586-pc-mingw32-ispellaff2myspell
%{_mingw32_bindir}/i586-pc-mingw32-makealias
%{_mingw32_bindir}/i586-pc-mingw32-munch.exe
%{_mingw32_bindir}/i586-pc-mingw32-unmunch.exe
%{_mingw32_bindir}/i586-pc-mingw32-wordforms
%{_mingw32_bindir}/i586-pc-mingw32-wordlist2hunspell
%{_mingw32_bindir}/libhunspell-1.2-0.dll
%{_mingw32_includedir}/hunspell/
%{_mingw32_libdir}/libhunspell-1.2.dll.a
%{_mingw32_libdir}/libhunspell-1.2.la
%{_mingw32_libdir}/libparsers.a
%{_mingw32_libdir}/pkgconfig/hunspell.pc

%files static
%{_mingw32_libdir}/libhunspell-1.2.a


%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt1_4
- initial release by fcimport

