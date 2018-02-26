Name: toilet
Version: 0.1
Release: alt1

Summary: The Other Implementation's letters
Packager: Pavlov Konstantin <thresh@altlinux.ru>
License: DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
Group: Text tools
Url: http://libcaca.zoy.org

Source: %name-%version.tar.bz2

BuildRequires: libcaca-devel zlib-devel

%description
TOIlet is in its very early development phase. It uses the powerful libcucul
library to achieve various text-based effects. TOIlet implements or plans to
implement the following features:
 * The ability to load FIGlet fonts
 * Support for Unicode input and output
 * Support for colour output
 * Support for various output formats: HTML, IRC, ANSI...

TOIlet also aims for full FIGlet compatibility. It is currently able to load
FIGlet fonts and perform horizontal smushing. 

%prep
%setup -q -n %name-%version

%build
touch INSTALL
touch AUTHORS
%__autoreconf

%configure

%make_build

%install
%make_install DESTDIR="%buildroot" install

%files
%_bindir/toilet
%_datadir/figlet
%_man1dir/toilet.*

%changelog
* Tue Nov 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1-alt1
- 0.1 release.


