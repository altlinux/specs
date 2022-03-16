Name: minidlna
Version: 1.3.1
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
mkdir -p %buildroot%_cachedir/%name

%find_lang %name

%pre
/usr/sbin/groupadd -r -f _minidlna &>/dev/null ||:
/usr/sbin/useradd -r -g _minidlna -d %_cachedir/%name -s /dev/null \
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

%_sbindir/minidlnad
%_man5dir/minidlna.conf.5*
%_man8dir/minidlnad.8*

%dir %attr(0770,root,_minidlna) %_cachedir/%name

%changelog
* Wed Mar 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- 1.3.1 released

* Thu Dec 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Thu Jun 14 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1 released

* Wed Jun 28 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

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
