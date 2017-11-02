%def_enable Werror

Name:		vor
Version:	0.5.7
Release:	alt1

Summary:	Variations on Rockdogders is an 2D space shooter

Group:		Games/Other
License:	GPLv2+
Url:		http://jasonwoof.org/vor

Source0:	%name-%version.tar
Source1:	vor.desktop

BuildRequires: libSDL libSDL_mixer libSDL_image libSDL_image-devel
BuildRequires: libSDL_mixer-devel desktop-file-utils gcc-c++
BuildRequires: netpbm povray

Requires: libSDL libSDL_mixer libSDL_image

%description
VoR is a simple, fast-paced action game that will challenge your reflexes.
It has excellent game-play, great physics, good graphics, and a retro/synthoid
thumpy beat to help put you in the mood for old-school 2D gaming.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

desktop-file-install --dir=%{buildroot}%{_datadir}/applications	%SOURCE1

%files
%doc COPYING README
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/%name

%changelog
* Thu Nov 02 2017 Grigory Ustinov <grenka@altlinux.org> 0.5.7-alt1
- Build new version.
  Change spec and remove patch.

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_3
- converted from Fedora by srpmconvert script
