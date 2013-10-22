Summary: Vargus - the video surveillance program
Name: vargus
Version: 0.9.6
Release: alt1
License: %gpl2plus
Group: Video

Packager: Michael A. Kangin <prividen@altlinux.org>

BuildArch: noarch

Source0: vargus-%version.tar
Source1: vargus-apache2-alt-configs.tar

BuildRequires(pre): rpm-macros-apache2
BuildRequires(pre): rpm-build-licenses
BuildPreReq: apache2-devel
BuildPreReq: rpm-build-webserver-common
BuildPreReq: perl-devel
BuildPreReq: perl-Filesys-Df perl-Proc-Daemon perl-Privileges-Drop perl-DBI perl-Net-Telnet
BuildPreReq: perl-Module-Load perl-Encode perl-File-Sync
BuildPreReq: perl-libnet perl-URI
Requires: MySQL-server avconv mediainfo perl-DBD-mysql xawtv4-common dbus-tools-gui
Requires: vlc-plugin-v4l vlc-plugin-ts vlc-plugin-mpeg2 vlc-plugin-live555 vlc-plugin-h264 
Requires: vlc-plugin-freetype vlc-plugin-ffmpeg vlc-plugin-dbus vlc-mini
Requires: mp4box v4l-utils


%description
Vargus is the video surveillance program which uses the VLC and ffmpeg
as a backends.

%package web
Summary: Web interfaces for %name
Group: Networking/WWW
Requires: %name = %version-%release
Requires: apache2-mod_php5 >= 5 
Requires: apache2-common >= 2.2.0 apache2-base php5-mysql php5-mbstring

%description web
Web interfaces for %name

%prep
%setup -n vargus-%version

%build

%install
%define vargus_user vargus
%define vargus_group vargus
%define vargus_cache %_cachedir/vargus
%define webappdir %webserver_webappsdir/vargus

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_sysconfdir/vargus
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_runtimedir/vargus
mkdir -p %buildroot%vargus_cache
mkdir -p %buildroot%webappdir
mkdir -p %buildroot%webappdir/modules-enabled
mkdir -p %buildroot%perl_vendor_privlib


install -m 0755 vargus.pl %buildroot%_bindir/vargus
install -m 0755 vcodec_copy_helper.pl %buildroot%_bindir/vcodec_copy_helper
install -m 0755 vargus-informer.pl %buildroot%_bindir/vargus-informer
install -m 0755 vargus-get-archive.pl %buildroot%_bindir/vargus-get-archive
install -m 0755 events-collector.pl %buildroot%_bindir/vargus-events
install -m 0755 vargus-simple-setup.pl %buildroot%_sbindir/vargus-simple-setup
install -m 0755 vargus-early-recovery %buildroot%_sbindir/
install -m 0755 vargus-systemd-starter %buildroot%_sbindir/
install -m 0644 vargus*.service %buildroot%_unitdir/
install -m 0644 docs/events-collector.cfg %buildroot%_sysconfdir/vargus/
install -m 0644 docs/get-archive.cfg %buildroot%_sysconfdir/vargus/

cp -r web/* %buildroot%webappdir/
cp -r Vargus %buildroot%perl_vendor_privlib/
mkdir -p %buildroot%perl_vendor_privlib/Vargus/Events

mkdir -p %buildroot%apache2_confdir
pushd %buildroot%apache2_confdir
tar xvSf %SOURCE1
find -name \*.conf |xargs sed -i "s|WEBAPPDIR|%webappdir|"
popd


%pre
%_sbindir/groupadd -r -f %vargus_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %vargus_group -G video -c 'vargus user' \
	-s /dev/null -d %vargus_cache %vargus_user 2>/dev/null ||:

%post
%post_service vargus
%post_service vargus-informer
%post_service vargus-events
%post_service vargus-early-recovery

%post web
%_sbindir/a2chkconfig >/dev/null
%post_service %apache2_dname
exit 0


%preun
%preun_service vargus
%preun_service vargus-informer
%preun_service vargus-events
%preun_service vargus-early-recovery

%postun web
%_sbindir/a2chkconfig >/dev/null
%post_service %apache2_dname
exit 0



%files
%_bindir/vargus*
%_bindir/vcodec_copy_helper
%_sbindir/vargus*
%_unitdir/vargus*
%attr(0750,root,%vargus_group) %dir %_sysconfdir/vargus
%config(noreplace) %_sysconfdir/vargus/*
%attr(0755,%vargus_user,%vargus_group) %dir %_runtimedir/vargus
%attr(0755,%vargus_user,%vargus_group) %dir %vargus_cache
%perl_vendor_privlib/Vargus
%perl_vendor_privlib/Vargus/Events
%doc docs/*

%files web
%dir %webappdir
%webappdir/*
%config %apache2_mods_start/*.conf
%config %apache2_extra_available/*.conf
%config %apache2_extra_start/*.conf


%changelog
* Wed Oct 23 2013 Michael A. Kangin <prividen@altlinux.org> 0.9.6-alt1
- systemd support
- Multiserver configuration support
- use-fqdn option in informer for full-form hostnames
- Improved video fragments handling
- small fixes

* Thu May 05 2013 Michael A. Kangin <prividen@altlinux.org> 0.9.5.4-alt1
- Events support for VargusViewer
- Control channel
- ability to restart object
- Fix restore DB from file
- Fix processing equal sign in the options
- Preprocessor support engine
- vcodec_copy_helper script
- vargus-early-recovery script

* Sat Oct 20 2012 Michael A. Kangin <prividen@altlinux.org> 0.9.5.3-alt1
- Support for remote cameras queries
- Support templates in camera objects
- Fix recovery after incorrect server restart
- Fix events output for cameras with non-standart names

* Sun Sep 23 2012 Michael A. Kangin <prividen@altlinux.org> 0.9.5.2-alt1
- (Re)start httpd daemon during simple setup

* Fri Sep 21 2012 Michael A. Kangin <prividen@altlinux.org> 0.9.5.1-alt1
- Some persistence fixes

* Sat Aug 18 2012 Michael A. Kangin <prividen@altlinux.org> 0.9.5-alt1
- Alerts support
- libav support
- Events enhancements: UDP support, multiple listeners, text preprocessor
- Web interface modules
- Autoconfiguration script


* Mon Jan 23 2012 Michael A. Kangin <prividen@altlinux.org> 0.9.4-alt1
- New postprocess model
- Text events support
- archive and web interface enhancements

* Sun Sep 11 2011 Michael A. Kangin <prividen@altlinux.org> 0.9.3-alt1
- Documentation, informer update

* Sun Sep 11 2011 Michael A. Kangin <prividen@altlinux.org> 0.9.2-alt1
- Informer update

* Sat May 21 2011 Michael A. Kangin <prividen@altlinux.org> 0.9.1-alt1
- 0.9.1

* Thu Apr 07 2011 Michael A. Kangin <prividen@altlinux.org> 0.9-alt1
- Initial release

