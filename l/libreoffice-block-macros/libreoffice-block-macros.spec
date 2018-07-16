Name:     libreoffice-block-macros
Version:  1.0.0
Release:  alt1

Summary:  Blocks any macros in LibreOffice
License:  GPLv3+
Group:    Other
Url:      http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

%description
Blocks any macros in LibreOffice.

%prep
%setup

%install
install -Dm 0644 block-macros.xcd  %buildroot%_libdir/LibreOffice/share/registry/block-macros.xcd
install -Dm 0644 block-macros.xcd  %buildroot%_libdir/LibreOffice-still/share/registry/block-macros.xcd

%files
%_libdir/LibreOffice/share/registry/block-macros.xcd
%_libdir/LibreOffice-still/share/registry/block-macros.xcd

%changelog
* Mon Jul 16 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build in Sisyphus.
