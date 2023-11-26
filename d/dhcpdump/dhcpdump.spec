# Spec file for dhcpdump utility

Name: dhcpdump

Version: 1.9
Release: alt1

Summary: DHCP packet dumper

License: %bsdstyle
Group: Networking/Other
URL: https://github.com/bbonev/dhcpdump
#URL: http://www.mavetju.org/unix/dhcpdump-man.php
#URL: http://www.mavetju.org/download/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

AutoReqProv: yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Nov 26 2023
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error perl perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-parent perl-podlators python-modules python2-base python3 python3-base python3-dev sh5
BuildRequires: libpcap-devel perl-Pod-Usage

%description
dhcpdump package provides a tool for visualization of DHCP
packets to analyze DHCP server responses.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
mkdir -p -- %buildroot{%_sbindir,%_man8dir}
install -m 0755 -- %name %buildroot%_sbindir/
install -m 0755 -- %name.8 %buildroot%_man8dir/

%files
%doc CONTACT LICENSE CHANGES
%_sbindir/%name
%_man8dir/*

%changelog
* Sun Nov 26 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.9-alt1
- New version
- Update upstream URL

* Sun Jan 20 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.8-alt3
- fix usage message (Closes: #22651)

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.8-alt2
- fix build with perl 5.12

* Wed Oct 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.8-alt1
- Initial build

