# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(gdk-pixbuf-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary: 	Extra gtk-2/3 themes for gtk based desktops
Name: 		mate-themes-extras
Version: 	1.7.11
Release: 	alt2_2

# upstream is located at github, but links from tag releases doesn't match copied link in
# web-browser, in result fedora-rewiew-tool will fail.
# so i decided to release on fedorapeople to have a valid download link
# There are different releases for GTK3 versions in f18, f19 and f20
URL: 		https://github.com/NiceandGently/mate-themes-extras-5
Source0:	http://raveit65.fedorapeople.org/Mate/SOURCE/%{name}-5-%{version}.tar.xz

License: 	LGPLv2 and GPLv2
Group: 		Graphical desktop/MATE
BuildArch: 	noarch

Requires: 	libgtk-engine-murrine
Requires: 	libgtk3-engine-unico
Requires: 	icon-theme-faience
Requires: 	x-cursor-themes-dmz
Requires: 	gnome-themes-standard-data
Requires: 	libgtk-engine-smooth
Requires: libgtk3-engine-adwaita gnome-themes-standard-data
Requires:   mate-icon-theme
Requires:   gnome-icon-theme
Requires:   icon-themes-gnome-colors

BuildRequires: 	gtk2-devel
BuildRequires: 	mate-common
BuildRequires:  hardlink

# for obsoleting external Repo versions f18 and f19
Obsoletes: mate-themes-extras-3 < %{version}-%{release}
Obsoletes: mate-themes-extras-4 < %{version}-%{release}
Source44: import.info

%description
The mate-themes-extras package contains a collection of GTK2/3 desktop
themes for all gtk based desktops.
These themes can change the appearance of application widgets, icons,
window borders, cursors, etc.
This package is optimized for GTK3-3.10.x for f20, GTK3-3.8.x for f19
and GTK3-3.6.x for f18.
Theme list: Blue-Submarine, Cologne, DeLorean-Dark, Faience, Faience-Ocre,
Gnome-Cupertino, Gnome-Cupertino-Mint, GnomishBeige, Green-Submarine,
Smoothly, Smoothly-Black, Zukitwo-Dust, Zukitwo-Brave, Zukitwo-Human,
Zukitwo-Illustrious, Zukitwo-Noble, Zukitwo-Wine, Zukitwo-Wise.

%prep
%setup -q -n %{name}-5-%{version}

%build
%configure \
    --enable-Blue-Submarine \
	--enable-Cologne \
    --enable-DeLorean-Dark \
	--enable-Faience \
	--enable-Faience-Ocre \
	--enable-Gnome-Cupertino \
	--enable-Gnome-Cupertino-Mint \
    --enable-GnomishBeige \
    --enable-Green-Submarine \
    --enable-Smoothly \
    --enable-Smoothly-Black \
	--enable-Zukitwo-Dust \
	--enable-Zukitwo-Brave \
	--enable-Zukitwo-Colors \
	--enable-Zukitwo-Human \
	--enable-Zukitwo-Illustrious \
	--enable-Zukitwo-Noble \
	--enable-Zukitwo-Wine \
	--enable-Zukitwo-Wise

make %{?_smp_mflags}

%install
%{makeinstall_std}

# remove unecessaries non-executable-scripts to avoid rpmlint errors
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/Faience-Ocre/gtk-3.0/render-assets.sh
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/Faience-Ocre/gtk-3.0/render-assets-dark.sh
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/Faience/gtk-3.0/render-assets.sh
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/Faience/gtk-3.0/render-assets-dark.sh

# save space by linking identical images
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Blue-Submarine
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Cologne
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/DeLorean-Dark
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Gnome-Cupertino
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Gnome-Cupertino-Mint
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/GnomishBeige
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Green-Submarine
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Faience
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Faience-Ocre
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Smoothly
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Smoothly-Black
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Zukitwo-Colors
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Zukitwo-Brave
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Zukitwo-Dust
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Zukitwo-Human
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Zukitwo-Illustrious
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Zukitwo-Noble
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Zukitwo-Wine
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/themes/Zukitwo-Wise


%files
%doc AUTHORS COPYING README ChangeLog
%{_datadir}/themes/Blue-Submarine/
%{_datadir}/themes/Cologne/
%{_datadir}/themes/DeLorean-Dark/
%{_datadir}/themes/Faience/
%{_datadir}/themes/Faience-Ocre/
%{_datadir}/themes/Gnome-Cupertino/
%{_datadir}/themes/Gnome-Cupertino-Mint/
%{_datadir}/themes/GnomishBeige/
%{_datadir}/themes/Green-Submarine/
%{_datadir}/themes/Smoothly/
%{_datadir}/themes/Smoothly-Black/
%{_datadir}/themes/Zukitwo-Colors/
%{_datadir}/themes/Zukitwo-Brave/
%{_datadir}/themes/Zukitwo-Dust/
%{_datadir}/themes/Zukitwo-Human/
%{_datadir}/themes/Zukitwo-Illustrious/
%{_datadir}/themes/Zukitwo-Noble/
%{_datadir}/themes/Zukitwo-Wine/
%{_datadir}/themes/Zukitwo-Wise/


%changelog
* Thu Feb 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.7.11-alt2_2
- dropped gtk3-themes-xfce4 dependency (closes: #30764)

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.11-alt1_2
- new fc release

