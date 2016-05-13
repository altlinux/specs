Name: livecd-gnome3-setup-done
Version: 0.3
Release: alt1

Summary: disable initial setup tool (gnome-3.14+)
License: public domain
Group: System/Configuration/Other

Url: http://en.altlinux.org/regular
BuildArch: noarch
AutoReqProv: no

%define conf %_sysconfdir/skel/.config/gnome-initial-setup-done

%description
%summary
(as some livecds have set up the environment already).

%prep

%build

%install
install -Dm644 /dev/null %buildroot%conf

%preun
# just removing skel file is too late for the first user
# created by livecd-install process, for example
find /home -maxdepth 2 -mindepth 2 -name .config -type d |
	while read i; do
		[ -d "$i/dconf" ] || rm -f "$i/gnome-initial-setup-done"
	done

%files
%conf

%changelog
* Thu May 12 2016 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- renamed from setup-gnome3-done to livecd-gnome3-setup-done
  so it's autoremoved by livecd-install
- remove the flag files for just-created users
  (who haven't logged into a gnome3 session yet)

* Fri Nov 28 2014 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- renamed livecd-gnome3-nosetup to setup-gnome3-done
  as it should survive installation

* Mon Oct 27 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (thanks aris@ for the hint)

