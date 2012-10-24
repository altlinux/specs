# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(gdk-pixbuf-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary: 	Themes for MATE
Name: 		mate-themes
Version: 	1.4.0
Release: 	alt1_1.1
URL: 		http://pub.mate-desktop.org
Source: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License: 	LGPLv2 and GPLv2
Group: 		Graphical desktop/Other
BuildArch: 	noarch

Requires: 	libgtk-engines-default
Requires: 	mate-icon-theme
Requires: 	libgtk-engine-murrine

BuildRequires: 	autoconf
BuildRequires: 	automake
BuildRequires: 	intltool
BuildRequires: 	gtk2-devel
BuildRequires: 	libtool
BuildRequires: 	gettext
BuildRequires: 	libgtk-engines-devel
BuildRequires: 	icon-naming-utils
BuildRequires: 	mate-common

Patch0: 		mate-themes_rename_Aldabra_to_Aldabras.patch

%description
The mate-themes package contains a collection of desktop themes for MATE.
These themes can change the appearance of application widgets, icons, window
borders, cursors, etc.

%package 	legacy
Summary: 	Old names for icons in mate-themes
Group: 		Graphical desktop/Other
Requires: 	mate-themes = %{version}-%{release}

%description legacy
This package contains symlinks to make the icons in mate-themes
available under old names.

%prep
%setup -q
%patch0 -p1 -b .mate-themes_rename_Aldabra_to_Aldabras
NOCONFIGURE=1 ./autogen.sh

%build
%configure

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# add legacy symlinks
for size in 16x16 22x22 24x24 32x32 48x48 256x256; do
  for context in actions apps devices places status; do
    (cd $RPM_BUILD_ROOT%{_datadir}/icons/Fog/$size
     icon-name-mapping -c $context)
  done
done

# we want to own the icon caches
for dir in $RPM_BUILD_ROOT%{_datadir}/icons/*; do
  touch $dir/icon-theme.cache
done

(cd $RPM_BUILD_ROOT%{_datadir}
 echo "%%defattr(-,root,root,-)"
 find icons/Fog -type l -and -not -name "gtk-\*" -printf "%%%%{_datadir}/%%p\n"
) > legacy.txt


%find_lang %{name}

%post
for icon_theme in Quid Fog ContrastHighLargePrint ContrastHighLargePrintInverse ContrastHigh-SVG ; do
  touch --no-create %{_datadir}/icons/${icon_theme} &> /dev/null || :
done

%postun
if [ $1 -eq 0 ]; then
for icon_theme in Quid Fog ContrastHighLargePrint ContrastHighLargePrintInverse ContrastHigh-SVG ; do
  touch --no-create %{_datadir}/icons/${icon_theme} &> /dev/null || :
done
fi

%files -f  %{name}.lang
%{_datadir}/icons/Quid/
%{_datadir}/icons/Fog/
%{_datadir}/icons/ContrastHigh-SVG/
%{_datadir}/icons/ContrastHighLargePrint/
%{_datadir}/icons/ContrastHigh/
%{_datadir}/icons/ContrastHighInverse/
%{_datadir}/icons/MateLargePrint/
%{_datadir}/icons/ContrastHighLargePrintInverse/
%{_datadir}/icons/mate/icon-theme.cache
%{_datadir}/icons/mate/cursors/
%{_datadir}/themes/ContrastHigh/
%{_datadir}/themes/ContrastHighInverse/
%{_datadir}/themes/ContrastHighLargePrint/
%{_datadir}/themes/ContrastHighLargePrintInverse/
%{_datadir}/themes/Reverse/
%{_datadir}/themes/ContrastLow/
%{_datadir}/themes/ContrastLowLargePrint/
%{_datadir}/themes/PrintLarge/
%{_datadir}/themes/Aldabras/
%{_datadir}/themes/Atantla/
%{_datadir}/themes/AlaDelta/

# themes where the gtk theme is shipped with the engine
%{_datadir}/themes/TraditionalOk/*
%{_datadir}/themes/Quid/*
%{_datadir}/themes/Fog/*

# others
%{_datadir}/themes/Shiny
%{_datadir}/themes/TraditionalOkClassic
%{_datadir}/themes/Simply


%doc AUTHORS COPYING NEWS README

%files legacy -f legacy.txt

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_1
- converted by srpmconvert script

