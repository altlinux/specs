Name:		spek
Version:	0.8.2
Release:	alt1
Summary:	Acoustic Spectrum Analyser
Group:		Sound
License:	GPLv3
URL:		http://spek.cc/
Source:		%name-%version.tar.xz
Patch:		spek-0.8.2-stdlib.patch

# Automatically added by buildreq on Thu Sep 18 2014
# optimized out: fontconfig gnu-config libavcodec-devel libavutil-devel libcloog-isl4 libgdk-pixbuf libopencore-amrnb0 libopencore-amrwb0 libstdc++-devel libwayland-client libwayland-server perl-Encode perl-XML-Parser pkg-config xz
BuildRequires: gcc-c++ intltool libavformat-devel libwxGTK-devel

%description
Spek helps to analyse your audio files by showing their spectrogram.

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc README*
%_bindir/*
%_man1dir/*
%_desktopdir/*
%_iconsdir/*/*/*/*


%changelog
* Thu Sep 18 2014 Fr. Br. George <george@altlinux.ru> 0.8.2-alt1
- Initial build

