%define rname	exit_button_firefox
%define cid 	\{94B08592-E5B4-45ff-A0BE-C1D975458688\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		firefox-exit_button
Version:	0.4.1
Release:	alt6

Summary:	Toolbar button to exit Firefox.

License:	GPL
Group:		Networking/WWW
URL:		http://www.linnhe.net/firefox/extensions.html

Packager:	Sergey Shilov <hsv@altlinux.ru>
Source0:	%rname-%version-fx.xpi


BuildArch:	noarch

BuildRequires(pre):	rpm-build-firefox
BuildRequires: 		unzip
Requires:		%firefox_name >= 2.0

%description 	
Exit Button Firefox plugin - adds a correspond button to Firefox toolbar.

%prep
%setup -c

%install
%__mkdir_p %buildroot/%ciddir
%__cp -r * %buildroot/%ciddir
sed -r -i \
    -e 's,<em:maxVersion>3\.0b5pre</em:maxVersion>,<em:maxVersion>7\.\*</em:maxVersion>,g' \
    %buildroot/%ciddir/install.rdf

%files
%ciddir

%changelog
* Tue Oct 18 2011 Sergey Shilov <hsv@altlinux.org> 0.4.1-alt6
- Rebuild for Firefox 7.0

* Wed Aug 24 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt5
- Rebuild for Firefox 6.0 

* Sun Jul 31 2011 Sergey Shilov <hsv@altlinux.org> 0.4.1-alt4
- Firefox 5.* comptibility fix.

* Sun May 1 2011 Sergey Shilov <hsv@altlinux.org> 0.4.1-alt3
- Initial build for Sisyphus.
