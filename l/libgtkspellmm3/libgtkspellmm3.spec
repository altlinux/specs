# Note: be in sync with gtkspell, see http://gtkspell.sourceforge.net/NEWS
Name: libgtkspellmm3
Version: 3.0.5
Release: alt1

Summary: On-the-fly spell checking for GtkTextView widgets - C++ bindings

License: GPLv2+
Group: System/Libraries
Url: http://gtkspell.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/gtkspell/gtkspellmm/gtkspellmm-%version.tar

# manually removed: python3 ruby ruby-stdlibs
# Automatically added by buildreq on Fri Oct 10 2014
# optimized out: at-spi2-atk fontconfig fontconfig-devel glib2-devel gnu-config libat-spi2-core libatk-devel libatkmm-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcairomm-devel libcloog-isl4 libenchant-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglibmm-devel libgtk+3-devel libpango-devel libpangomm-devel libsigc++2-devel libstdc++-devel libwayland-client libwayland-cursor libwayland-server pkg-config python3-base
BuildRequires: doxygen gcc-c++ glibc-devel graphviz libdb4-devel libgtkmm3-devel libgtkspell3-devel xsltproc

# http://gtkspell.sourceforge.net/NEWS
BuildRequires: libgtkspell3-devel >= 3.0.9

%description
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.

%package devel
Group: Development/Other
Summary: Development files for %name
Requires: %name = %version-%release

%description devel
The %name-devel package provides header and documentation files for
developing C++ applications which use GtkSpell.

%package doc
Group: Documentation
Summary: Documentation for %name
BuildArch: noarch
#Requires: libgtkmm3-doc

%description doc
This package contains the full API documentation for %name.

%prep
%setup -n gtkspellmm-%version

%build
%add_optflags -std=c++11
%configure --disable-static
%make_build

%install
%makeinstall_std
find %buildroot -name "*.la" -exec rm {} \;

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/libgtkspellmm-3.0.so.0*

%files devel
%_includedir/gtkspellmm-3.0
%_libdir/libgtkspellmm-3.0.so
%_pkgconfigdir/gtkspellmm-3.0.pc
%_libdir/gtkspellmm-3.0

%files doc
%doc COPYING
%_datadir/devhelp/books/gtkspellmm-3.0
%_docdir/gtkspellmm-3.0

%changelog
* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.5-alt1
- new version 3.0.5 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt1
- new version 3.0.4 (with rpmrb script)

* Fri Oct 10 2014 Vitaly Lipatov <lav@altlinux.ru> 3.0.3-alt1
- initial build for ALT Linux Sisyphus

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Sandro Mani <manisandro@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Fri Apr 26 2013 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- New upstream release (uses correct GPLv2 license headers)

* Fri Mar 08 2013 Sandro Mani <manisandro@gmail.com> - 3.0.0-1
- Initial package.
