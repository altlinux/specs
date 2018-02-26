%define rname	extensiondev
%define version 0.3.0.20060726
%define release alt1.2
%define cid 	\{75739dec-72db-4020-aa9a-6afa6744759b\}
%define ciddir	%firefox_noarch_extensionsdir/%cid


Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:        A suite of tools for extension developers	

License:	GPL
Group:		Networking/WWW
URL:		http://ted.mielczarek.org/code/mozilla/extensiondev/index.html


Source0:	%rname.xpi

BuildArch:	noarch

BuildRequires(pre):	rpm-build-firefox unzip
Requires:	%firefox_name >= 2.0

Packager: L.A. Kostis <lakostis@altlinux.org>

%description 	
The Extension Developer's Extension exists to make life easier for Firefox
extension developers. Testing JavaScript code, prototyping XUL layouts, and
building XPI packages are all made easier by this extension.

%prep
%setup -c

%install
mkdir -p %buildroot/%ciddir
cp -r * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Sun Nov 26 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.0.20060726-alt1.2
- Rebuild for fx 2.0.
- remove obsoleted macros.
- explicitly set buildarch to noarch.

* Wed Sep 27 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.0.20060726-alt1.1
- rebuild for Firefox 1.5.0.7.

* Thu Sep 07 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.0.20060726-alt1
- initial build for ALTLinux.

