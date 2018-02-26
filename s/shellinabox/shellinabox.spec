Name: shellinabox
Version: 2.14
Release: alt1

Summary: AJAX based terminal emulator exporting a console to the browser
License: GPLv2
Group: Networking/Remote access

Url: http://www.shellinabox.com
Source0: http://shellinabox.googlecode.com/files/%name-%version.tar.gz
Source1: shellinabox.conf
Source2: shellinabox.init.in
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: zlib-devel openssl-devel

%define runas _shellinaboxd

%description
Shell In A Box implements a web server that can export arbitrary command
line tools to a web based terminal emulator. This emulator is accessible
to any JavaScript and CSS enabled web browser and does not require any
additional browser plugins.

All client-server communications are encrypted, if SSL/TLS certificates
have been installed.

More details are available in the manual page; for configuration,
see also /etc/sysconfig/shellinaboxd (localhost only by default).

%prep
%setup
%configure --bindir=%_sbindir

%build
%make_build

%install
%makeinstall_std
rm -r %buildroot/usr/share/doc
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/shellinaboxd
install -pDm755 /dev/null %buildroot%_initdir/shellinaboxd
sed 's/%%runas/%runas/' < %SOURCE2 > %buildroot%_initdir/shellinaboxd

%pre
/usr/sbin/groupadd -r -f %runas
/usr/sbin/useradd -r -g %runas -d / -s /dev/null \
	-c "Shell in a Box" -n %runas >/dev/null 2>&1 ||:

%post
%post_service shellinaboxd

%preun
%preun_service shellinaboxd

%files
%doc AUTHORS ChangeLog COPYING GPL-2 NEWS README
%doc shellinabox/monochrome.css shellinabox/color.css
%doc shellinabox/black-on-white.css shellinabox/white-on-black.css
%doc demo
%_man1dir/shellinaboxd.1*
%_sbindir/shellinaboxd
%config(noreplace) %_sysconfdir/sysconfig/shellinaboxd
%_initdir/shellinaboxd

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 2.14-alt1
- 2.14

* Mon Feb 14 2011 Michael Shigorin <mike@altlinux.org> 2.10-alt1
- initial build for ALT Linux Sisyphus

* Sun Sep 12 2010 Jochen Wiedmann <jochen.wiedmann@gmail.com> - 2.10-2
- Review by Martin Gieseking, see
  https://bugzilla.redhat.com/show_bug.cgi?id=619228#c1

* Thu Jul 29 2010 Jochen Wiedmann <jochen.wiedmann@gmail.com> - 2.10-1
- Initial build.
