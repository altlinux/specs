# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		coquillo
Version:	2.0.1
Release:	alt1_1
Summary:	Audio Metadata Editor
License:	LGPLv3+
Group:		Sound
Url:		https://github.com/sjuvonen/coquillo
Source0:	https://github.com/sjuvonen/coquillo/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(taglib)
Source44: import.info

%description
Coquillo is a metadata editor, or so-called tagger utility, with which you can
edit tags of many different audio files. Its support includes MP3, Ogg/Vorbis,
FLAC and many others.

%files
%doc BUGS README.md
%doc --no-dereference LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%qmake_qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}


%changelog
* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- update by mgaimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_3
- new version

