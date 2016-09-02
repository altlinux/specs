Name: minidlna
Version: 1.1.6
Release: alt1

Summary: DLNA AV Media Server
License: GPLv2
Group: System/Servers
Url: http://sourceforge.net/projects/minidlna/

Source: %name-%version-%release.tar

BuildRequires: libjpeg-devel libexif-devel libid3tag-devel libogg-devel
BuildRequires: libvorbis-devel libflac-devel libsqlite3-devel
BuildRequires: libavcodec-devel libavformat-devel libavutil-devel

%description
%summary

%prep
%setup
sed -i '/user=/ s,^.\+$,user=_minidlna,' minidlna.conf

%build
%autoreconf
%configure --with-os-url='http://www.altlinux.org'
%make_build

%install
%makeinstall_std
install -pm0644 -D minidlna.conf %buildroot%_sysconfdir/minidlna.conf
install -pm0644 -D minidlna.conf.5 %buildroot%_man5dir/minidlna.conf.5
install -pm0644 -D minidlnad.8 %buildroot%_man8dir/minidlnad.8
install -pm0755 -D minidlna.init %buildroot%_initdir/minidlna
install -pm0644 -D minidlna.sysconfig %buildroot%_sysconfdir/sysconfig/minidlna
install -pm0644 -D minidlna.service %buildroot%_unitdir/minidlna.service
install -pm0644 -D minidlna.tmpfiles %buildroot%_tmpfilesdir/minidlna.conf
mkdir -p %buildroot%_cachedir/%name %buildroot%_runtimedir/%name

%find_lang %name

%pre
/usr/sbin/groupadd -r -f _minidlna &>/dev/null ||:
/usr/sbin/useradd -r -g _minidlna -d %_runtimedir/%name -s /dev/null \
    -c "minidlna service" -M -n _minidlna &>/dev/null ||:

%post
%post_service minidlna

%preun
%preun_service minidlna

%files -f %name.lang
%doc AUTHORS COPYING NEWS README
%config(noreplace) %_sysconfdir/minidlna.conf
%config(noreplace) %_sysconfdir/sysconfig/minidlna

%_initdir/minidlna
%_unitdir/minidlna.service
%_tmpfilesdir/minidlna.conf

%_sbindir/minidlnad
%_man5dir/minidlna.conf.5*
%_man8dir/minidlnad.8*

%dir %attr(0770,root,_minidlna) %_cachedir/%name
%dir %attr(0770,root,_minidlna) %_runtimedir/%name

%changelog
* Fri Sep 02 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.6-alt1
- 1.1.6 released

* Fri Feb 06 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.4-alt1
- 1.1.4 released

* Sun May 18 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.2-alt2
- rebuilt with libav10

* Thu Mar 20 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.2-alt1
- 1.1.2 released

* Tue Jan 14 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt1
- 1.1.1 released

* Sat Aug 17 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- initial
