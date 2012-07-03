Name: tinc
Version: 1.0.8
Release: alt2.1.qa1.1

Summary: Virtual Private Network (VPN) daemon that uses tunnelling and encryption to create a secure private network between hosts on the Internet.
Summary(ru_RU.KOI8-R): Небольшой демон для создания шифрованных туннелей и частных виртуальных сетей между хостами в сети Интернет
Summary(uk_UA.KOI8-U): Невеликий демон для створення шифрованих тунел╕в та приватних в╕ртуальних мереж м╕ж хостами в мереж╕ ╤нтернет
Group: System/Servers
License: GPL
Url: http://www.tinc-vpn.org

Source: %url/packages/%name-%version.tar.gz
Source1: %name.init
Source2: %name.sysconfig
Source3: %name.control

PreReq(post,preun): chkconfig

# Automatically added by buildreq on Fri Apr 04 2008
BuildRequires: liblzo2-devel libssl-devel tetex-latex zlib-devel

%description
%name is a Virtual Private Network (VPN) daemon that uses tunnelling
and encryption to create a secure private network between hosts on the
Internet.

%name is Free Software and licensed under the GNU General Public License.
Because the VPN appears to the IP level network code as a normal
network device, there is no need to adapt any existing software. This 
allows VPN sites to share information with each other over the
Internet without exposing any information to others. In addition, %name 
has the following features:

Encryption, authentication and compression
    All traffic is optionally compressed using zlib or LZO, and
    OpenSSL is used to encrypt the traffic and protect it from 
    alteration with message authentication codes and sequence numbers. 
Automatic full mesh routing
    Regardless of how you set up the %name daemons to connect to each 
    other, VPN traffic is always (if possible) sent directly to the 
    destination, without going through intermediate hops. 
Easily expand your VPN
    When you want to add nodes to your VPN, all you have to do is add 
    an extra configuration file, there is no need to start new daemons 
    or create and configure new devices or network interfaces. 
Ability to bridge ethernet segments
    You can link multiple ethernet segments together to work like a 
    single segment, allowing you to run applications and games that 
    normally only work on a LAN over the Internet. 
Runs on many operating systems and supports IPv6
    Currently Linux, FreeBSD, OpenBSD, NetBSD, MacOS/X, Solaris, 
    Windows 2000 and XP platforms are supported. See our section about 
    supported platforms for more information about the state of the
    ports. %name has also full support for IPv6, providing both the 
    possibility of tunneling IPv6 traffic over its tunnels and of 
    creating tunnels over existing IPv6 networks. 

%prep
%setup -q

%build
%configure --prefix=%_usr --sysconfdir=%_sysconfdir \
	--localstatedir=%_var \
	--infodir=%_infodir \
	--mandir=%_mandir \
	--disable-nls \
	--disable-rpath
#	--enable-jumbograms
%make_build
pushd doc
%make pdf
popd

%install
%__mkdir_p %buildroot%_sysconfdir/%name/hosts
%__mkdir_p %buildroot%_initdir
%__mkdir_p %buildroot%_sysconfdir/sysconfig
%make_install DESTDIR=%buildroot install
%__install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
%__install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
%__install -pD -m755 %SOURCE3 %buildroot%_controldir/%name

%pre
%pre_control %name

%post
%post_control %name
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/*
%_man5dir/*
%_man8dir/*
%_infodir/%name.info*
%config %_controldir/%name
%config(noreplace) %_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%attr(750,root,wheel) %dir %_sysconfdir/%name/hosts
%attr(750,root,wheel) %dir %_sysconfdir/%name
%doc AUTHORS ChangeLog COPYING COPYING.README INSTALL README NEWS THANKS doc/sample-config.tar.gz doc/tinc.pdf

%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2.1.qa1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.8-alt2.1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for tinc
  * postclean-05-filetriggers for spec file

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.8-alt2.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Fri Apr 04 2008 Serhii Hlodin <hlodin@altlinux.ru> 1.0.8-alt2
- To reduce init script to LSB

* Wed Jul 04 2007 Serhii Hlodin <hlodin@altlinux.ru> 1.0.8-alt1
- New version
- Fixed some memory and resource leaks
- Made network sockets non-blocking under Windows

* Sun Jan 28 2007 Serhii Hlodin <hlodin@altlinux.ru> 1.0.7-alt2
- Remove --enable-jumbograms

* Tue Jan 23 2007 Serhii Hlodin <hlodin@altlinux.ru> 1.0.7-alt1
- Add control facilities
- Bug fixed version

* Wed Nov 15 2006 Serhii Hlodin <hlodin@altlinux.ru> 2:2.1a15-alt3
- Initial build
