Name: alt-csp-cryptopro
Version: 0.0.1
Release: alt1

Group: File tools
Summary: CryptoPRO GUI tool
License: GPL-2.0-or-later

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: libprocps-devel
BuildRequires: quazip-qt5-devel
BuildRequires: qt5-tools-devel

%description
CryptoPRO GUI tool

%package kde
Summary: CryptoPRO integration with KDE
Group: File tools
BuildArch: noarch

%description kde
CryptoPRO integration with KDE

%package mate
Summary: CryptoPRO integration with KDE
Group: File tools
BuildArch: noarch

%description mate
CryptoPRO integration with MATE

%prep
%setup

%build
%cmake
%cmake_build

%install
%make install -C BUILD DESTDIR=%buildroot
mkdir -p %buildroot/%_qt5_translationdir/
install -m 0644 BUILD/*.qm %buildroot/%_qt5_translationdir/
%find_lang --with-qt --all-name %name

%files -f %name.lang
%_bindir/alt-csp-cryptopro
%_desktopdir/alt-csp-cryptopro.desktop

%files kde
%_K5srv/ServiceMenus/alt-csp-cryptopro.desktop

%files mate
%_datadir/file-manager/actions/alt-csp-cryptopro.desktop

%changelog
* Fri Dec 04 2020 Oleg Solovyov <mcpain@altlinux.org> 0.0.1-alt1
- Initial build

