Name: pyneighborhood-settings-desktop 
Version: 0.1
Release: alt1
BuildArch: noarch

Source:%name-%version.tar


Summary: pyneighborhood settings for Desktop version
License: GPL
Group: System/Configuration/Other
Packager: Anton V. Boyarshiniv <boyarsh@altlinux.org>

Requires: etcskel


%description
pyneighborhood settings  for Desktop version


%prep
%setup -q


%install
mkdir -p %buildroot/etc/skel/.pyNeighborhood
install -m 644 .pyNeighborhood/* %buildroot/etc/skel/.pyNeighborhood/

%files
/etc/skel/.pyNeighborhood
/etc/skel/.pyNeighborhood/*


%changelog
* Thu Oct 11 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build



