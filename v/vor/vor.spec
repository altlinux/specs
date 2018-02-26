BuildRequires: gcc-c++
Name:		vor
Version:	0.5.5
Release:	alt1_3
Summary:	Variations on Rockdogders is an 2D space shooter

Group:		Games/Other
License:	GPLv2+
URL:		http://jasonwoof.org/vor
Source0:	http://qualdan.com/%{name}/%{name}-%{version}.tar.bz2
Source1:	vor.desktop

BuildRequires:	libSDL libSDL_mixer libSDL_image libSDL_image-devel libSDL_mixer-devel desktop-file-utils

Patch10:	vor-fix-DSO.patch

Requires:	libSDL libSDL_mixer libSDL_image
Source44: import.info

%description
VoR is a simple, fast-paced action game that will challenge your reflexes. 
It has excellent game-play, great physics, good graphics, and a retro/synthoid 
thumpy beat to help put you in the mood for old-school 2D gaming.

%prep
%setup -q
%patch10 -p0

%build
%configure --prefix=/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

desktop-file-install	\
--dir=%{buildroot}%{_datadir}/applications	\
%{SOURCE1}

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%changelog
* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_3
- converted from Fedora by srpmconvert script

