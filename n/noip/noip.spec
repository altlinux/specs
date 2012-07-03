Summary:	Linux client for the no-ip.com dynamic DNS service
Name:		noip
Version:	2.1.9
Release:	alt2
License:	GPL
Group:		Networking/Other
URL:		http://www.no-ip.com
Source0:	http://www.no-ip.com/client/linux/%name-%version.tar.bz2
Source1:	%name-initscript
Source2:	%name-config
Patch0:		%name-%version-makefile.patch
Patch1:		%name-%version-config-path.patch

%description
This is the No-IP.com Dynamic DNS update client page.

When configured correctly, the client will check your IP address at a
given time interval checking to see if your IP has changed. If your IP
address has changed it will notify No-IP DNS servers and update the IP
corresponding to your No-IP/No-IP+ hostname.

NOTE: You must add hostnames on the website (http://www.no-ip.com)
first before you can have the updater update them.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
mv -f %{name}2.c %{name}.c

%build
perl -pi -e "s/CCFLAGS=.*/CCFLAGS=%optflags/" Makefile

%make PREFIX="%_prefix" BINDIR="%_sbindir" CONFDIR="%_sysconfdir"

%install
%makeinstall_std PREFIX=%_prefix CONFDIR="%_sysconfdir" BINDIR="%_sbindir"

touch %buildroot%_sysconfdir/%name.conf
mkdir -p %buildroot%_initrddir
install -m 600 %SOURCE1 %buildroot%_initrddir/%name

mkdir -p %buildroot%_sysconfdir/sysconfig
install -m 644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

cat > README.alt << EOF
To configure the noip deamon, run noip -C as root.
This command will set the corrects parameters in /etc/noip.conf.
Then you can start the deamon with service noip start
EOF

%post
echo
echo To configure the noip deamon, run noip -C as root.
echo This command will set the correct parameters in /etc/noip.conf.
echo Then you can restart the deamon with "service noip restart".
echo

%files
%doc README.FIRST README.alt
%attr(755,root,root) %_sbindir/*
%attr(744,root,root) %_initrddir/%name
%ghost %config(missingok, noreplace) %_sysconfdir/%name.conf
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/sysconfig/%name


%changelog
* Sun Jun 05 2011 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.9-alt2
- Add options to initscript

* Sun Sep 19 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.9-alt1
- Update to new release

* Sun Jan 27 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.7-alt1
- Initial ALT Linux release

