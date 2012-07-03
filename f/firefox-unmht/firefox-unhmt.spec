%define rname	unmht
%define cid	\{f759ca51-3a91-4dd1-ae78-9db5eee9ebf0\}
%define ciddir 	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	5.7.2
Release:	alt1
Summary:	Extension to view and save MHT files with Mozilla Firefox

License:	MPL/GPL/LGPL
Group:		Networking/WWW	
Url:		http://www.unmht.org/unmht/en_index.html

Source0:	%rname-%version.xpi

BuildArch:	noarch
BuildRequires:	rpm-build-firefox unzip

Packager: Sergey Kurakin <kurakin@altlinux.org>

%description 
UnMHT extension allow you to view MHT (MHTML, RFC2557) web archive
format files in Mozilla Firefox, and save complete web pages,
inluding text and graphics, into a single MHT file.

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
* Fri Nov 25 2011 Sergey Kurakin <kurakin@altlinux.org> 5.7.2-alt1
- 5.7.2: native compatiblility with Firefox 9

* Wed Oct 12 2011 Sergey Kurakin <kurakin@altlinux.org> 5.7.1-alt1
- 5.7.1: native compatiblility with Firefox 7

* Sat Sep  3 2011 Sergey Kurakin <kurakin@altlinux.org> 5.7.0-alt1
- 5.7.0: native compatiblility with Firefox 6

* Wed Aug 24 2011 Andrey Cherepanov <cas@altlinux.org> 5.6.9-alt3
- Build with Firefox 6.0

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 5.6.9-alt2
- Update maxVersion according to AMO.

* Tue Apr  5 2010 Sergey Kurakin <kurakin@altlinux.org> 5.6.9-alt1
- 5.6.9: includes compatiblility with Firefox 4

* Sat Feb 20 2010 Sergey Kurakin <kurakin@altlinux.org> 5.5.2-alt1
- 5.5.2: compatiblility with Firefox 3.6

* Tue Dec 22 2009 Sergey Kurakin <kurakin@altlinux.org> 5.4.0-alt1
- 5.4.0

* Wed Jun 10 2009 Sergey Kurakin <kurakin@altlinux.org> 5.2.5-alt1
- initial build for AltLinux Sisyphus
