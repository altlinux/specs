%define shortname ices

Name: ices2
Version: 2.0.1
Release: alt3

Summary: Ices2 - sourcer to use with Icecast2 daemon
Packager: Pavlov Konstantin <thresh@altlinux.ru>
License: GPL
Group: Sound
Url: http://www.icecast.org

Source0: %shortname-%version.tar.bz2
Source1: %name

BuildPreReq: libshout2-devel >= 2.1-alt1.1

BuildRequires: gcc-c++ libalsa-devel libogg-devel libshout2-devel libstdc++-devel libvorbis-devel libxml2-devel pkgconfig zlib-devel

%description
Ices is a streamer for use with icecast2.
This package includes full-featured version of ices2.

%prep
%setup -q -n %shortname-%version

%build
%configure

%make_build

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_sysconfdir
cp conf/*.xml %buildroot%_sysconfdir/
rm -rf %buildroot%_datadir/ices
mv %buildroot%_bindir/%shortname %buildroot%_bindir/%name

#log path
mkdir -p %buildroot%_logdir/%shortname

#init-script
mkdir -p %buildroot%_initdir
install -m755 %SOURCE1 %buildroot%_initdir/%name

%pre
%_sbindir/groupadd -r -f _%shortname &>/dev/null
%_sbindir/useradd -r -g _%shortname -d %_localstatedir/%name -s /dev/null \
        -c "Ices2 pseudo user" -M -n _%shortname &>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc doc/{*.html,*.css}
%config (noreplace) %_sysconfdir/*.xml
%_bindir/%name
%_logdir/%shortname
%_initdir/%name

%changelog
* Fri Aug 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0.1-alt3
- Added init-script (closes #8925).

* Thu Dec 15 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.0.1-alt2
- added ALSA support.
- fixes #8657, thanks Alexander Volkov (alt vladregion ru)

* Mon Mar 14 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.0.1-alt1.1
- rebuilt with libshout2.1-alt1

* Fri Mar 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.0.1-alt1
- 2.0.1 release

* Mon Nov 22 2004 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0-alt2
- Rebuild with new libshout2.

* Wed Oct 20 2004 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0-alt1
- Initial build for Sisyphus

