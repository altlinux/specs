Name: timekpr-next
Version: 0.5.9
Release: alt1
Summary: Keep control of computer usage
Group: Graphical desktop/Other
License: GPL-3.0
URL: https://launchpad.net/timekpr-next

Source: https://launchpad.net/%name/stable/%version/+download/%name-%version.tar.gz

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-devel

%description
Timekpr-nExT is a program that tracks and controls the computer usage of your
user accounts. You can limit their daily usage based on a timed access duration
and configure periods of day when they can or cannot log in.

This may be used for parental control to limit the amount of screen time a
child spends in front of the computer.

Please report any bugs to Timekpr-nExT's bug tracker on Launchpad at:
https://bugs.launchpad.net/timekpr-next

%prep
%setup -q -n %name
sed -i 's|python3/dist-packages|python3/site-packages|g' bin/* client/*.py debian/install resource/server/systemd/timekpr.service server/timekprd.py

%build

%install
# install files
grep -v -e '^#' -e '^$' debian/install | sed -e 's|/$||' -e 's| lib/systemd/| usr/lib/systemd/|g' -e 's|^\(.\+/\)\(.*\) \(.*\)/\?$|mkdir -p %buildroot/\3 ; cp \1\2 %buildroot/\3|g' | sh -

# appdata file
install -Dpm 644 resource/appstream/org.timekpr.%name.metainfo.xml %buildroot%_datadir/metainfo/org.timekpr.%name.metainfo.xml

%find_lang timekpr

%pre
getent group timekpr > /dev/null || /usr/sbin/groupadd -r timekpr

%post
%post_service timekpr

%preun
%preun_service timekpr

%files -f timekpr.lang
%doc debian/changelog debian/copyright
%config(noreplace) %_sysconfdir/timekpr/timekpr.conf
%_bindir/*
%_desktopdir/*.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/polkit-1/actions/*
%_datadir/timekpr
%python3_sitelibdir/timekpr
%_unitdir/*.service
%_sysconfdir/dbus-1/system.d/*
%_sysconfdir/logrotate.d/*
%_sysconfdir/timekpr
%_sysconfdir/xdg/autostart/*
%_datadir/metainfo/*
%_sharedstatedir/timekpr

%changelog
* Sun Jul 05 2026 Andrey Cherepanov <cas@altlinux.org> 0.5.9-alt1
- Initial import to Sisyphus from
  https://copr.fedorainfracloud.org/coprs/johanh/timekpr-next/.
