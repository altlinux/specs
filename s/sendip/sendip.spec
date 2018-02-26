Name: sendip
Version: 2.5
Release: alt4

Summary: A command line tool to allow sending arbitrary IP packets
License: GPL
Group: Networking/Other

Url: http://www.earth.li/projectpurple/progs/sendip.html
Source: http://www.earth.li/projectpurple/files/%name-%version.tar.gz
Patch0: sendip-2.5-alt-makefile.patch
#Patch1: sendip-2.5-alt-warnings.patch
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

%description
A command line tool to send arbitrary IP packets. It has a large number of
command line options to specify the content of every header of a NTP, BGP,
RIP, RIPng, TCP, UDP, ICMP, or raw IPv4 or IPv6 packet.  It also allows any
data to be added to the packet.

%prep
%setup -q
%patch0 -p1
#%%patch1 -p1

%build
%make LIBDIR=%_libdir/%name

%install
%make PREFIX=%buildroot/usr \
	MANDIR=%buildroot%_man1dir \
	LIBDIR=%buildroot%_libdir/%name install

%files
%_man1dir/%name.1*
%_bindir/%name
%_libdir/%name/*.so
%dir %_libdir/%name
%doc VERSION README CHANGES TODO contrib

%changelog
* Tue Jun 06 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 2.5-alt4
- Build without -Werror

* Mon Mar 20 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 2.5-alt3
- Fixed build with --as-needed

* Thu Feb 16 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 2.5-alt2
- Fix building for x86_64

* Tue Feb 14 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 2.5-alt1
- Initial build for Sisyphus (adopted spec from Mike Ricketts <mike at
  earth.li>)
