%define	name	fontconfig-infinality
%define version	1
%define infinality_release	20121110

Summary: Fontconfig configuration meant to be used in conjunction with Freetype patches from http://www.infinality.net.  
Name: %{name}
Version: %{version}
Release: alt2.git%{infinality_release}
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
URL: http://www.infinality.net/
Packager: Vladimir Didenko <cow@altlinux.ru>
Provides: fontconfig-infinality
Requires: fontconfig

Source: %name-%version.tar
Source1: 53-infinality-user.conf

%description
A configurable fontconfig configuration meant to be used in conjunction
with Freetype patches from http://www.infinality.net.  It should drop
cleanly into most existing fontconfig setups.  While this package will
work without infinality patches, much of it is tailored to rendering 
when using those patches, and may not look correct otherwise. 

%install
%define confdir %{buildroot}/etc/fonts/
%define docdir %{buildroot}/usr/share/doc/%{name}-%{version}
install -m755 -pd %confdir
install -m755 -pd %docdir
tar xf %SOURCE0 --strip-components 1 -C  %confdir
mv %confdir/infinality/CHANGELOG %docdir 
mv %confdir/infinality/CHANGELOG.pre_git %docdir 
mv %confdir/infinality/LICENSE %docdir 
mv %confdir/infinality/README %docdir 
#52-infinality.conf overrides user settings so restoring them
cp %SOURCE1 %confdir/conf.avail
ln -s ../conf.avail/53-infinality-user.conf %confdir/conf.d/53-infinality-user.conf

%files
%defattr(-,root,root)
%config %{_sysconfdir}/fonts/infinality
%config %{_sysconfdir}/fonts/conf.avail/52-infinality.conf
%config %{_sysconfdir}/fonts/conf.avail/53-infinality-user.conf
%config %{_sysconfdir}/fonts/conf.d/52-infinality.conf
%config %{_sysconfdir}/fonts/conf.d/53-infinality-user.conf
%doc %_docdir/%{name}-%{version}/*

%changelog
* Thu Dec 11 2012 Vladimir Didenko <cow@altlinux.org> 1-alt2.git20121110
- Don't override user settings

* Thu Dec 11 2012 Vladimir Didenko <cow@altlinux.org> 1-alt1.git20121110
- Alt Linux build

* Thu Nov 20 2011 Infinality <infinality@infinality.net>
- Remove Canwell replacments from local.conf

* Thu Nov 17 2011 Infinality <infinality@infinality.net>
- New version created

