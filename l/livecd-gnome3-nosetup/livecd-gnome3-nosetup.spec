Name: livecd-gnome3-nosetup
Version: 0.1
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

%files
%conf

%changelog
* Mon Oct 27 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (thanks aris@ for the hint)

