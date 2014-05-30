Name: mintlocale
Version: 1.1.6
Release: alt2

Summary: Language selection tool for Cinnamon
License: GPLv2+
Group: Graphical desktop/GNOME

Url: https://github.com/linuxmint/mintlocale
Source0: %name-%version.tar
Source1: org.%name.policy

BuildArch: noarch

Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-python
BuildPreReq: rpm-build-gir
BuildRequires: gobject-introspection 

%description
Language selection tool for Cinnamon

%prep
%setup -n %name-%version
%patch0 -p1

# move python modules to /usr/share
mv usr/lib/linuxmint usr/share
sed -i -e 's@/usr/lib@/usr/share@g' usr/bin/mintlocale \
    usr/share/linuxmint/mintLocale/mintLocale.py

%build

%install
install -m 0755 -d %buildroot%{_prefix}/
cp -Rp usr %buildroot
chmod +x %buildroot%_bindir/mintlocale-set-default-locale

#install polkit files
install -m 0755 -d %buildroot%{_datadir}/polkit-1/actions/
install -D -p -m 0644 %{SOURCE1} %buildroot%{_datadir}/polkit-1/actions/

%files
%_bindir/mintlocale
%_bindir/mintlocale-set-default-locale
%_datadir/applications/mintLocale.desktop
%_datadir/linuxmint/mintLocale
%_datadir/polkit-1/actions/org.mintlocale.policy

%doc debian/copyright

%changelog
* Fri May 30 2014 Vladimir Didenko <cow@altlinux.org> 1.1.6-alt2
- add support for /etc/syconfig/i18n

* Thu May 29 2014 Vladimir Didenko <cow@altlinux.org> 1.1.6-alt1
- initial build
