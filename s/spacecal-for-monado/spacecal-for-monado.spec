Name:    spacecal-for-monado
Version: 1.1.0
Release: alt1

Summary: A monado powered playspace calibrator for mixed VR tracking origins
License: GPL-3.0-only
Group:   System/Configuration/Hardware
URL:     https://github.com/99oblivius/spacecal-for-monado

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: glib2-devel libcairo-devel libgdk-pixbuf-devel libpango-devel
BuildRequires: libgraphene-devel libcairo-gobject-devel libgtk4-devel
BuildRequires: libadwaita-devel openxr-devel

%description
SpaceCal aligns VR devices from different tracking systems into a single
unified space through the Monado OpenXR runtime. Use your Quest headset
with lighthouse-tracked controllers, Vive trackers, or any mix of
tracking technologies.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install
install -Dm644 data/dev.oblivius.spacecal-for-monado.desktop \
%buildroot%_desktopdir/dev.oblivius.spacecal-for-monado.desktop

install -Dm644 data/dev.oblivius.spacecal-for-monado.svg \
%buildroot%_iconsdir/hicolor/scalable/apps/dev.oblivius.spacecal-for-monado.svg

install -Dm644 data/dev.oblivius.spacecal-for-monado.metainfo.xml \
%buildroot%_datadir/metainfo/dev.oblivius.spacecal-for-monado.metainfo.xml

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/metainfo/*.xml

%changelog
* Thu Jul 30 2026 Sergey Palcheh <minergenon@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
