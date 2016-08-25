%define	name	fontconfig-infinality
%define version	1
%define infinality_release	20130126

%define infinality_user 53-infinality-user.conf
%define aliases_default_alt 20-aliases-default-alt.conf
%define aliases_os_alt 41-aliases-os-alt.conf

Summary: Fontconfig configuration meant to be used in conjunction with Freetype patches from http://www.infinality.net.
Name: %{name}
Version: %{version}
Release: alt7.git%{infinality_release}
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
URL: http://www.infinality.net/
Packager: Vladimir Didenko <cow@altlinux.ru>
Provides: fontconfig-infinality
Requires: fontconfig

Source: %name-%version.tar
Source1: 20-aliases-default-alt.conf
Source2: 41-aliases-os-alt.conf

%description
A configurable fontconfig configuration meant to be used in conjunction
with Freetype patches from http://www.infinality.net.  It should drop
cleanly into most existing fontconfig setups.  While this package will
work without infinality patches, much of it is tailored to rendering
when using those patches, and may not look correct otherwise.

%install
%define confdir %{buildroot}/etc/fonts/
%define confinfdir %confdir/infinality
%define docdir %{buildroot}/usr/share/doc/%{name}-%{version}
install -m755 -pd %confdir
install -m755 -pd %docdir
tar xf %SOURCE0 --strip-components 1 -C  %confdir

mv %confinfdir/CHANGELOG %docdir
mv %confinfdir/CHANGELOG.pre_git %docdir
mv %confinfdir/LICENSE %docdir
mv %confinfdir/README %docdir

# Create alt style based on infinality that uses free fonts for replacements
cp %SOURCE1 %confinfdir/conf.src
cp %SOURCE2 %confinfdir/conf.src
%define confavaildir %confinfdir/styles.conf.avail
cp -a %confavaildir/infinality %confavaildir/alt
pushd %confavaildir/alt
    rm -f 20-aliases-default-inf.conf
    rm -f 41-repl-os-inf.conf
    ln -s ../../conf.src/%{aliases_default_alt} %{aliases_default_alt}
    ln -s ../../conf.src/%{aliases_os_alt} %{aliases_os_alt}
popd
rm -f %confinfdir/conf.d
ln -s styles.conf.avail/alt %confinfdir/conf.d

%files
%defattr(-,root,root)
%config %{_sysconfdir}/fonts/infinality
%config %{_sysconfdir}/fonts/conf.avail/50-infinality.conf
%config %{_sysconfdir}/fonts/conf.d/50-infinality.conf
%doc %_docdir/%{name}-%{version}/

%changelog
* Thu Aug 25 2016 Vladimir Didenko <cow@altlinux.org> 1-alt7.git20130126
- don't ban Type-1 fonts (closes: #32427)

* Wed Aug 28 2013 Vladimir Didenko <cow@altlinux.org> 1-alt6.git20130126
- fix user settings overriding

* Fri Jul 26 2013 Vladimir Didenko <cow@altlinux.org> 1-alt5.git20130126
- use aliases instead substitutions in 'alt' style

* Mon Jun 17 2013 Vladimir Didenko <cow@altlinux.org> 1-alt4.git20130126
- new version

* Fri Jan 25 2013 Vladimir Didenko <cow@altlinux.org> 1-alt3.git20121110
- New alt style based on infinality that uses free fonts for replacements

* Thu Dec 11 2012 Vladimir Didenko <cow@altlinux.org> 1-alt2.git20121110
- Don't override user settings

* Thu Dec 11 2012 Vladimir Didenko <cow@altlinux.org> 1-alt1.git20121110
- Alt Linux build

* Thu Nov 20 2011 Infinality <infinality@infinality.net>
- Remove Canwell replacments from local.conf

* Thu Nov 17 2011 Infinality <infinality@infinality.net>
- New version created
