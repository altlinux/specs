Summary: Rutoken plugin for web-browser
Name: rutoken-plugin
Version: 2.8.9.0
Release: alt1
License: Proprietary
URL: https://www.rutoken.ru/products/all/rutoken-plugin/
#Download: https://download.rutoken.ru/Rutoken_Plugin/
Group: Security/Networking
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64

BuildRequires: unzip
BuildRequires: libpcsclite

%description
Rutoken plugin for web-browser.

%prep
%setup

%install
mkdir -p %buildroot%_libdir/browser-plugins
%ifarch %ix86
unzip rutoken-plugin-lin-x86.zip -d %buildroot%_libdir/browser-plugins
%else
unzip rutoken-plugin-lin-x86_64.zip -d %buildroot%_libdir/browser-plugins
%endif

%files
%doc license.ru.html
%_libdir/browser-plugins/*

%changelog
* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.9.0-alt1
- Initial build in Sisyphus
