%define _libexecdir %_prefix/libexec
Summary: 		MATE icon theme
Name: 			mate-icon-theme
Version: 		1.4.0
Release: 		alt1_1.1
URL: 	 		http://mate-desktop.org
Source0: 		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License: 		GPL+
BuildArch: 		noarch
Group: 			Graphical desktop/Other
BuildRequires: 	icon-naming-utils
BuildRequires: 	gettext
BuildRequires: 	intltool
BuildRequires:  mate-common
Requires: 		icon-theme-hicolor

%description
This package contains the default icon theme used by the MATE desktop.

%package legacy
Summary: Old names for icons in mate-icon-theme
Group: Graphical desktop/Other
Requires: mate-icon-theme = %{version}-%{release}

%description legacy
This package contains symlinks to make the icons in mate-icon-theme
available under old names.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static \
	--enable-icon-mapping

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Add scalable directories for symbolic icons
(cd $RPM_BUILD_ROOT%{_datadir}/icons/mate

mkdir -p scalable/actions
mkdir -p scalable/apps
mkdir -p scalable/devices
mkdir -p scalable/emblems
mkdir -p scalable/mimetypes
mkdir -p scalable/places
mkdir -p scalable/status
)

(cd $RPM_BUILD_ROOT%{_datadir}
 echo "%%defattr(-,root,root,-)"
 find icons/mate \( -name gtk-* -or -type f \) -printf "%%%%{_datadir}/%%p\n"
 find icons/mate -type d -printf "%%%%dir %%%%{_datadir}/%%p\n"
) > files.txt

(cd $RPM_BUILD_ROOT%{_datadir}
 echo "%%defattr(-,root,root,-)"
 find icons/mate \( -type l -and -not -name gtk-* \) -printf "%%%%{_datadir}/%%p\n"
) > legacy.txt

%post
touch --no-create %{_datadir}/icons/mate &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/mate &>/dev/null
fi

%post legacy
touch --no-create %{_datadir}/icons/mate &>/dev/null || :

%postun legacy
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/mate &>/dev/null
fi

%files -f files.txt
%doc COPYING AUTHORS
%{_datadir}/pkgconfig/mate-icon-theme.pc

%files legacy -f legacy.txt

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

