%define rname	print_preview
%define version 0.7.1.4
%define release alt1
%define cid 	\{a1f99b9c-30d3-4848-a646-afd282011a72\}
%define ciddir	%firefox_noarch_extensionsdir/%cid


Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:        Creates a Print Preview toolbar button and context menu item

License:	GPL
Group:		Networking/WWW
URL:		http://www.snide.com/freesoftware/


Source0:	printpreview-%version.xpi
Source1:	%rname-chrome.manifest

BuildArch:	noarch

BuildRequires(pre):	rpm-build-firefox unzip
Requires:	%firefox_name >= 2.0

Packager: L.A. Kostis <lakostis@altlinux.ru>

%description 	
Creates a Print Preview toolbar button and context menu item.

%prep
%setup -c
subst 's/maxVersion>3\.5\./maxVersion>17.0./g' install.rdf

%install
%__mkdir_p %buildroot/%ciddir
%__cp -r * %buildroot/%ciddir
%__cp -a %SOURCE1 %buildroot/%ciddir/chrome.manifest

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Wed Dec 19 2012 Andrey Cherepanov <cas@altlinux.org> 0.7.1.4-alt1
- New version 0.7.1.4

* Mon Nov 27 2006 L.A. Kostis <lakostis@altlinux.ru> 0.6.1.1-alt1
- Initial build for Sisyphus.

