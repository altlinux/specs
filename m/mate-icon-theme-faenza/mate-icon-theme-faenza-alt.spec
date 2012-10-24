%define _libexecdir %_prefix/libexec
Name:           mate-icon-theme-faenza
Version:        1.4.0
Release:        alt1_1.1.1
Summary:        faenza-theme for MATE

Group:          Graphical desktop/Other
License:        GPL
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildArch: 		noarch

BuildRequires:  mate-common

%description
This icon theme uses Faenza and Faience icon themes by ~Tiheum and
some icons customized for MATE by Rowen Stipe.


%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure

%install
make install DESTDIR=$RPM_BUILD_ROOT
# fixing broken symlinks (TODO: upstream it)
# matefaenza/apps/scalable/mate-session-properties.svg -> ../../categories/96/preferences-desktop.svg
# matefaenza/places/scalable/distributor-logo.svg -> /home/rowen/MATE/Icon themes/Faenza MATE/places/scalable/distributor-logo-mate.svg
ln -sf ../../categories/scalable/preferences-desktop.svg \
 %buildroot%_iconsdir/matefaenza/apps/scalable/mate-session-properties.svg
ln -sf distributor-logo-mate.svg \
%buildroot%_iconsdir/matefaenza/places/scalable/distributor-logo.svg


%post
touch --no-create %{_datadir}/icons/matefaenza &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/matefaenza &>/dev/null
fi

%files
%{_datadir}/icons/matefaenza
%{_datadir}/icons/matefaenzadark

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1.1
- Build for Sisyphus

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Tue Aug 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

