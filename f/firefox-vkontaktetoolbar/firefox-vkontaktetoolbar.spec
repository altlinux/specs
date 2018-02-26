%define cid	vkontakte.toolbar@uh-zuh.ru
%define ciddir	%firefox_noarch_extensionsdir/%cid

Summary:	VkontakteToolbar extension for Firefox
Name:		firefox-vkontaktetoolbar
Version:	0.6.0
Release:	alt2
Source0:	vkontaktetoolbar-%version.xpi
License:	GPL
Group:		Networking/WWW
URL:		http://vkontakte.ru/club267829
Packager:	Radik Usupov <radik@altlinux.org>
BuildArch:	noarch

BuildRequires(pre):	rpm-build-firefox
BuildRequires:  unzip

%description 
Toolbar for site vkontakte.ru

%prep
%setup -c

%install
%__mkdir_p %buildroot/%ciddir
%__cp -r * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
	[ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Tue Apr 24 2012 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt2
- Build for Firefox 11.0

* Wed Aug 24 2011 Radik Usupov <radik@altlinux.org> 0.6.0-alt1
- New version (0.6.0)

* Mon Aug 01 2011 Radik Usupov <radik@altlinux.org> 0.5.9-alt2
- Rebuild from Mozilla FireFox 5.0

* Wed Apr 13 2011 Radik Usupov <radik@altlinux.org> 0.5.9-alt1
- New version (0.5.9)

* Thu Feb 24 2011 Radik Usupov <radik@altlinux.org> 0.5.8-alt2
- Fixed summary

* Fri Feb 18 2011 Radik Usupov <radik@altlinux.org> 0.5.8-alt1
- Initial build for ALTLinux (Closes: 18431)

