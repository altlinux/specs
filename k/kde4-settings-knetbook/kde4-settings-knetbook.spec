%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define theme knetbook
%define Theme KNetbook
%define kdeconfdir %_K4sysconfdir/kde4
%define thisconfdir %kdeconfdir/%theme

%define major 0
%define minor 1
%define bugfix 0
Name: kde4-settings-%theme
Version: %major.%minor.%bugfix
Release: alt1

Group: Graphical desktop/KDE
Summary: %Theme - specific KDE settings
License: GPL
Url: http://www.altlinux.ru/

BuildArch: noarch

PreReq(post,preun): alternatives >= 0.2
Requires: kde-common >= 4

Source: %theme-settings-%version.tar

BuildRequires: cmake gcc-c++ kde-common-devel rpm-macros-alternatives

%description
%Theme - specific KDE settings


%prep
%setup -qn %theme-settings-%version


%build
%ifarch x86_64
#echo -e "\n" >> startkde
%endif


%install
mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name <<__EOF__
%kdeconfdir/current	%thisconfdir 60
__EOF__

# configs
mkdir -p %buildroot/%thisconfdir/share/config/
install -m 0644 config/* %buildroot/%thisconfdir/share/config/

# autostart
mkdir -p %buildroot/%thisconfdir/share/autostart/
install -m 0644 autostart/* %buildroot/%thisconfdir/share/autostart/

# startkde
install -m 0755 startkde %buildroot/%thisconfdir/

# startactive modules
mkdir -p %buildroot/%_K4apps/startactive/modules/
install -m 0644 startactive-modules/*.module %buildroot/%_K4apps/startactive/modules/


%files
%config %_altdir/%name
%config %thisconfdir
%_K4apps/startactive/modules/*.module

%changelog
* Wed Jun 26 2013 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
