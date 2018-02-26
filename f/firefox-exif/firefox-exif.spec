%define rname	exif
%define version 1.13
%define release alt2
%define cid 	exif_viewer@mozilla.doslash.org
%define ciddir	%firefox_noarch_extensionsdir/%cid


Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:        View EXIF data in image properties	

License:	GPL
Group:		Networking/WWW
URL:		https://addons.mozilla.org/firefox/3905/


Source0:	%rname.xpi

BuildArch:	noarch

BuildRequires(pre):	rpm-build-firefox unzip
Requires:	%firefox_name >= 2.0

Packager: L.A. Kostis <lakostis@altlinux.org>

%description 	
Extracts and displays the Exchangeable Image File (Exif) data, as stored by
digital still cameras, in both local and remote JPEG images.

%prep
%setup -cT
%__unzip %SOURCE0

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
* Mon Jan 29 2007 L.A. Kostis <lakostis@altlinux.ru> 1.13-alt2
- use unzip without -L due inpredictive results.

* Sun Jan 28 2007 L.A. Kostis <lakostis@altlinux.ru> 1.13-alt1
- Initial build for ALTLinux
- Use russian translation from http://people.mozilla-russia.org/dvdianov/extensions/exif/exif.xpi

