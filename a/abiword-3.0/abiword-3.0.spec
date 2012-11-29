%define _name abiword
%define abi_ver 3.0
%define ver_major 2.9
%def_enable spell
%def_without goffice
%def_with champlain
%def_with libical
%def_without eds

Name: %_name-%abi_ver
Version: %ver_major.4
Release: alt1

Summary: Lean and fast full-featured word processor
Group: Office
License: GPL
Url: http://www.abisource.com/

Source: http://www.abisource.com/downloads/abiword/%version/source/%_name-%version.tar.gz

Obsoletes: abisuite, abisuite-koi8, abisuite-cp1251, abisuite-iso8859-8
Conflicts: %_name %_name-light

BuildRequires: gcc-c++ boost-devel
BuildRequires: libgtk+3-devel librsvg-devel libfribidi-devel
BuildRequires: libwpd-devel libwv-devel libgsf-devel bzlib-devel
BuildRequires: libjpeg-devel
%{?_enable_spell:BuildRequires: libenchant-devel}
%{?_with_goffice:BuildRequires: libgnomeoffice0.10-devel}
%{?_with_champlain:BuildRequires: libchamplain-gtk3-devel}
%{?_with_libical:BuildRequires: libical-devel}
%{?_with_eds:BuildRequires: evolution-data-server-devel}

%description
AbiWord is a cross-platform, Open Source Word Processor developed
by the people at AbiSource, Inc. and by developers from around the world.
(http://www.abisource.com)
It is a lean and fast full-featured word processor. It works on Microsoft
Windows and most Unix Systems. Features include:

   * Basic character formatting (bold, underline, italics, etc.)
   * Paragraph alignment
   * Spell-check
   * Import of Word97 and RTF documents
   * Export to RTF, Text, HTML, and LaTeX formats
   * Document Templates
   * Interactive rulers and tabs
   * Styles
   * Unlimited undo/redo
   * Multiple column control
   * Widow/orphan control
   * Find/Replace
   * Images
   and much more...

%package devel
Group: Development/C++
Summary: Headers for Abiword plugins
Requires: %name = %version-%release


%description devel
Headers and pkgconfig support for  Abiword plugin building.
Conflicts: %_name-devel %_name-light-devel

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	--enable-print \
	--enable-plugins \
	--enable-templates \
	--enable-clipart \
	%{subst_enable spell} \
	%{subst_with goffice} \
	%{subst_with champlain} \
	%{subst_with libical} \
	%{?_without_eds:--without-evolution-data-server} \
	--disable-static

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/%_name
%_libdir/lib%_name-%ver_major.so
%dir %_libdir/%_name-%ver_major
%dir %_libdir/%_name-%ver_major/plugins
%_libdir/%_name-%ver_major/plugins/*.so
%_iconsdir/hicolor/*/*/*
%_datadir/%_name-%ver_major
%_desktopdir/%_name.desktop
%_man1dir/*

%exclude %_libdir/abiword-%ver_major/plugins/*.la


%files devel
%_includedir/*
%_pkgconfigdir/*

%changelog
* Thu Nov 29 2012 Yuri N. Sedunov <aris@altlinux.org> 2.9.4-alt1
- first build for Sisyphus

