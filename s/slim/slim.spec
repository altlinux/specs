%define _unpackaged_files_terminate_build 1
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name: slim
Version: 1.3.6
Release: alt4

Summary: SLiM is a graphical, desktop-independent login manager for X11.

License: GPLv2+
Group: System/X11
Url: http://sourceforge.net/projects/slim.berlios/

Source: %name-%version.tar
Source1: %name.init
Source2: %name.pam

Source5: slim.logrotate.d
Source6: slim-tmpfiles.conf
Source7: slim.service

Patch1: CMakeLists.txt.patch
Patch2: slim-add-sessiondir.patch
Patch3: slim_conf.patch
Patch4: slim-1.3.2-selinux.patch
Patch5: slim-gcc11.patch

BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Tue Feb 02 2016
# optimized out: cmake-modules fontconfig fontconfig-devel libICE-devel libSM-devel libX11-devel libXau-devel libXrender-devel libXt-devel libfreetype-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: cmake gcc-c++ libXext-devel libXft-devel libXmu-devel libXrandr-devel libjpeg-devel libpam-devel libpng-devel libsystemd-devel

%description
SLiM (Simple Login Manager) is a graphical, desktop-independent login
manager for X11.

%prep
%setup
%patch1 -p2
%patch2 -p1
%patch3 -p2
%patch4 -p1
%patch5 -p1

%build
%cmake_insource -DUSE_PAM=yes \
	-DBUILD_SHARED_LIBS=no
%make_build

%install
%makeinstall_std
mkdir -p -- %buildroot%_initdir
install -m 0755 -- %SOURCE1 %buildroot%_initdir/%name
install -D -m 0755 -- %SOURCE2 %buildroot%_sysconfdir/pam.d/%name

# install logrotate entry
install -m0644 -D %SOURCE5 %buildroot/%_sysconfdir/logrotate.d/%name
install -p -D %SOURCE6 %buildroot%_sysconfdir/tmpfiles.d/%{name}.conf

mkdir -p %buildroot%_unitdir
install -m 644 %SOURCE7 %buildroot%_unitdir/%{name}.service

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/*
%dir %_datadir/%name/
%_datadir/%name/*
%_man1dir/*
%_unitdir/%{name}.service
%config %_initdir/%name
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/pam.d/%name
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/%name.conf
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/tmpfiles.d/%name.conf

%changelog
* Wed Oct 27 2021 Igor Vlasenko <viy@altlinux.org> 1.3.6-alt4
- picked up
- added logrotate file
- updated .service file
- use /var/run/slim for tmp files

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 1.3.6-alt3
- NMU: fixed build

* Wed Sep 14 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.6-alt2
- add slim-add-sessiondir.patch (Debian #740394)
- fix slim.conf (closes: #32389)

* Mon Apr 18 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.6-alt1
- initial build
