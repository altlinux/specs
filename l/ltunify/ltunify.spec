Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ltunify
URL:            https://lekensteyn.nl/logitech-unifying.html
Version:        0.1
Release:        alt1_13
License:        GPLv3+
Summary:        Command line utility for Logitech Unifying Receiver
Source:         https://git.lekensteyn.nl/ltunify/snapshot/ltunify-0.1.tar.gz

Requires:       unifying-receiver-udev

BuildRequires:  gcc
Source44: import.info
%description
ltunify allows pairing, unpairing, and listing information about devices
uses a Logitech Unifying Receiver.

%prep
%setup -q
chmod -x hidraw.c
# Remove line in Makefile that overrides CFLAGS from command line. Ugh.
sed -i -e 's/^override.*$//' Makefile

%build
%make_build CFLAGS="%{optflags}"

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 %{name} %{buildroot}%{_bindir}
install -p -m0755 read-dev-usbmon %{buildroot}%{_bindir}
install -p -m0755 usbmon.awk %{buildroot}%{_bindir}

%files
%doc README.txt registers.txt
%{_bindir}/%{name}
%{_bindir}/read-dev-usbmon
%{_bindir}/usbmon.awk

%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_13
- new version

