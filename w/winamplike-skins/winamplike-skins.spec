%define		skinname winamplike-skins

%define		_skinsdir %_datadir/%skinname
Version:	0.1
Name:		%skinname
Release:	alt1
Summary:	Common folder for winamp-like skins collections
License: 	GPLv2
Group: 		Sound
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source0:	%skinname

BuildArch:	noarch

%description
Common folder for %skinname for mediaplayers compatible
with skins for winamp - XMMS, Audacious, Qmmp and other

%package -n rpm-build-wlskins
Group:		Development/Other
Summary:	RPM helper macros to build %skinname collections

%description -n rpm-build-wlskins
RPM helper macros to build %skinname collections

%install
%__mkdir -p %buildroot%_skinsdir
%__install -Dp -m 0644 %SOURCE0 %buildroot%_sysconfdir/rpm/macros.d/%skinname

%files
%dir %_skinsdir

%files -n rpm-build-wlskins
%_sysconfdir/rpm/macros.d/%skinname

%changelog
* Wed Dec 03 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial
