Name: tyrquake
Version: 0.71
Release: alt1
Summary: A conservative Quake port
License: GPL3.0
Group: Games/Arcade
Url: https://disenchant.net/tyrquake/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
BuildRequires: ImageMagick-tools
BuildRequires: groff-base
BuildRequires: libGL-devel
BuildRequires: libpulseaudio-devel 
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXxf86vm-devel

ExcludeArch: %ix86

%description
TyrQuake is a port of id Software's  Quake engine  which attempts to
maintain the original look and feel of the game while also providing
support for modern platforms and user created content.

Currently TyrQuake is implemented as five separate programs;  two
NetQuake clients (tyr-quake and tyr-glquake), two Quakeworld clients
(tyr-qwcl and tyr-glqwcl) and a Quakeworld server (tyr-qwsv). The 'gl'
notation indicates the OpenGL accelerated clients and the non-gl ver-
sions use a software-only renderer.

Quake data directories:
=========================
~/.tyrquake/id1/
~/.tyrquake/qw/
#
# systemwide
/usr/share/quake/id1/
/usr/share/quake/qw/
=========================

%prep
%setup

%build
export CFLAGS="%optflags"
%make_build \
  QBASEDIR=%_datadir/quake \
  OPTIMIZED_CFLAGS=N \
  V=1 \
%{?_smp_mflags}

%install
for b in tyr-{glquake,glqwcl,quake,qwcl,qwsv}; do
  install -Dm 0755 bin/$b %buildroot%_bindir/$b
done
install -d %buildroot%_datadir/quake
mkdir -p %buildroot/%_man6dir
install -D -p -m 0644 man/tyrquake.6 %buildroot%_man6dir

%files
%doc gnu.txt
%doc changelog.txt readme.txt readme-id.txt
%_bindir/tyr-*
%_man6dir/*

%changelog
* Tue Dec 13 2022 Artyom Bystrov <arbars@altlinux.org> 0.71-alt1
- initial build for ALT Sisyphus


