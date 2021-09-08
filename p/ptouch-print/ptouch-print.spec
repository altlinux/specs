%define oname ptouch

Name:      %oname-print
Version:   1.4.2
Release:   alt1
Summary:   ptouch is a command line tool to print labels on Brother P-Touch printers on Linux.
License:   GPLv3
URL:       https://github.com/clarkewd/ptouch-print
Group:     Graphics
Source:    %name-%version.tar
Source10:  ru.po
Patch10:   ptouch-print-alt-l10n.patch

BuildRequires: libgd3-devel libusb-devel

%description
ptouch is a command line tool to print labels on Brother P-Touch printers on Linux.

%prep
%setup -q
%patch10 -p 1
cp %SOURCE10 po/ru.po

%build
./autogen.sh
%configure
%make

%install
%makeinstall
install -d -m 0755 %buildroot%_man1dir
install -p -m 0644 %name.1 %buildroot%_man1dir/
%find_lang %oname

%files -f %oname.lang
%doc COPYING README AUTHORS
%_bindir/%name
%_man1dir/*

%changelog
* Wed Sep 08 2021 Ivan Razzhivin <underwit@altlinux.org> 1.4.2-alt1
- initial build
