Name: mintlocale
Version: 1.4.3
Release: alt1

Summary: Language selection tool for Cinnamon
License: GPLv2+
Group: Graphical desktop/GNOME

Url: https://github.com/linuxmint/mintlocale
Source0: %name-%version.tar
Source1: org.%name.policy

BuildArch: noarch

Patch: %name-%version-%release.patch

Requires: iso-flag-png

BuildPreReq: rpm-build-python
BuildPreReq: rpm-build-gir
BuildRequires: gobject-introspection

%description
Language selection tool for Cinnamon

%prep
%setup -n %name-%version
%patch0 -p1

%build

%install
install -m 0755 -d %buildroot%{_prefix}/
cp -Rp usr %buildroot

rm -f %buildroot%_bindir/add-remove-locales \
  %buildroot%_datadir/applications/%{name}-im.desktop \
  %buildroot%_prefix/lib/linuxmint/mintlocale/synaptic-install-packages \
  %buildroot%_prefix/lib/linuxmint/mintlocale/add.py \
  %buildroot%_prefix/lib/linuxmint/mintlocale/install_remove.py

#install polkit files
install -m 0755 -d %buildroot%{_datadir}/polkit-1/actions/
install -D -p -m 0644 %{SOURCE1} %buildroot%{_datadir}/polkit-1/actions/

echo 'LANG=$locale' > %{buildroot}%{_datadir}/linuxmint/mintlocale/templates/default_locale.template

%files
%_bindir/mintlocale
%_bindir/set-default-locale
%_prefix/lib/linuxmint
%_datadir/applications/%{name}.desktop
%_datadir/linuxmint
%_datadir/polkit-1/actions/org.mintlocale.policy

%doc debian/copyright debian/changelog

%changelog
* Wed May 23 2017 Vladimir Didenko <cow@altlinux.org> 1.4.3-alt1
- new version

* Fri May 30 2014 Vladimir Didenko <cow@altlinux.org> 1.1.6-alt2
- add support for /etc/syconfig/i18n

* Thu May 29 2014 Vladimir Didenko <cow@altlinux.org> 1.1.6-alt1
- initial build
