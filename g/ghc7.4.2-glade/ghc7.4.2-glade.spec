%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name glade
%define f_pkg_name glade
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.12.1
Release: alt1
License: LGPL-2.1
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://projects.haskell.org/gtk2hs/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Binding to the glade library.



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils fontconfig fontconfig-devel ghc7.4.2 ghc7.4.2-cairo ghc7.4.2-common ghc7.4.2-gio ghc7.4.2-glib ghc7.4.2-mtl ghc7.4.2-pango ghc7.4.2-transformers glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgmp-devel libgtk+2-devel libpango-devel libwayland-client libwayland-server pkg-config python-base rpm-build-haskell zlib-devel
BuildRequires: ghc7.4.2-alex ghc7.4.2-c2hs ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-gtk ghc7.4.2-happy ghc7.4.2-hscolour gtk2hs-buildtools libglade-devel

%description
This library allows to load externally stored user interfaces into
programs. This allows alteration of the interface without recompilation of
the program.

Note that this functionality is now provided in gtk directly (as of version
2.12 of the gtk+ C lib) by the Graphics.UI.Gtk.Builder module.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all
%hs_pkgconfdir/%f_pkg_name-%version.conf

%changelog
* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 0.12.1-alt1
- Spec created by cabal2rpm 0.20_08
