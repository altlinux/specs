Name: imule
Version: 1.4.6
Release: alt4.qa1

Summary: P2P file sharing software which connects through the anonymous I2P network
License: GPL
Group: Networking/File transfer

Url: http://echelon.i2p/imule/
Source: %name-%version.tar

Conflicts: aMule
BuildRequires: gcc-c++ zlib-devel libgd2-devel libpng-devel wxGTK-devel flex
BuildRequires: desktop-file-utils

%description
%summary

%prep
%setup

%build
%configure \
        --enable-optimize \
        --disable-debug \
        --disable-webserver \
	--disable-profile \
        --enable-ccache \
	--docdir=%buildroot%_defaultdocdir/%name-%version
%make

%install
%makeinstall
%find_lang imule
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=FileTransfer \
	--add-category=P2P \
	%buildroot%_desktopdir/imule.desktop

%files -f imule.lang
%_bindir/imule
%_bindir/ed2k
%_datadir/applications/*
%_datadir/pixmaps/*
%_mandir/man1/*
%_mandir/*/man1/*
%doc %_defaultdocdir/%name-%version

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.4.6-alt4.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for imule

* Tue Nov 16 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.6-alt4
- Fix building with gcc4.6.

* Mon Oct 18 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.6-alt3
- Build without libbfd-devel and libiberty-devel.

* Fri Oct 15 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.6-alt2
- Add conflict with aMule (Closes: #23874).
- docs/nodes.dat: replaced with fresh version from echelon.i2p.
- Fix docs packaging.

* Tue Aug 10 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.6-alt1
- Initial build for Sisyphus.
