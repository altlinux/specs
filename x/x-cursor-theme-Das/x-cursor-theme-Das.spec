%define		appsnum 106216
%define		themename Das

Name:		x-cursor-theme-%themename
Version:	20101017
Release:	alt1
Summary:	%themename cursors for Xorg
License:	GPL
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Group:		System/X11
BuildArch:	noarch
Url:		http://xfce-look.org/content/show.php/DasBlack?content=%appsnum
Source0:	%themename.tar.gz
Source1:	%{themename}Black.tar.gz

Patch0:		Das_name_Blue.diff

%description
Das cursors for Xorg

%package -n %{themename}Blue
Summary: %{themename}Blue red icons theme.
Group: System/X11
Provides: %name

%description -n %{themename}Blue
%{themename}Blue X11 Mouse theme

%package -n %{themename}Black
Summary: %{themename}Black red icons theme.
Group: System/X11
Provides: %name

%description -n %{themename}Black
%{themename}Black X11 Mouse theme

%prep
%setup -c -q -n %themename
tar xvzf %SOURCE1
%patch0 -p1

%install
mkdir -p %buildroot%_iconsdir
cp -a Das %buildroot%_iconsdir/%{themename}Blue
cp -a DasBlack %buildroot%_iconsdir/%{themename}Black

%files -n %{themename}Blue
%dir %_iconsdir/%{themename}Blue
%_iconsdir/%{themename}Blue

%files -n %{themename}Black
%dir %_iconsdir/%{themename}Black
%_iconsdir/%{themename}Black

%changelog
* Wed Sep 25 2013 Motsyo Gennadi <drool@altlinux.ru> 20101017-alt1
- initial build for ALT Linux
