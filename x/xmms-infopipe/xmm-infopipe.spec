Name:		xmms-infopipe
Version:	1.3
Release:	alt1
Summary:	InfoPipe plugin for XMMS
Group:		Sound
License:	GPL
URL:		http://www.beastwithin.org/users/wwwwolf/code/xmms/infopipe.html
Source:		http://www.beastwithin.org/users/wwwwolf/code/xmms/xmms-infopipe-1.3.tar.gz

Requires: xmms >= 1.0.1
BuildPreReq: libxmms-devel >= 1.0.1

# Automatically added by buildreq on Tue Jul 26 2005
BuildRequires: glib-devel gtk+-devel libxmms-devel

%description
%name is a general plugin to use with XMMS 

%define _xmms_general_plugin_dir %(xmms-config --general-plugin-dir)

%prep
%setup -q


%build
########
# makes no sense, but let's leave it here as a reminder
%configure --disable-static
%make_build

%install
make DESTDIR=$RPM_BUILD_ROOT install 

%files
%_xmms_general_plugin_dir/*.so*
%doc AUTHORS ChangeLog README applications/lirc-say.pl applications/xmms-info.php applications/xmms-info.pl

%changelog
* Tue Jul 26 2005 Nick S. Grechukh <gns@altlinux.ru> 1.3-alt1
- initial build for Sisyphus
