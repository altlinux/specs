Name: polkit-rule-mobile
Version: 0.1
Release: alt1
Summary: Rules for polkit to allow mobile features
License: GPLv3+
Group: Other
Url: https://altlinux.org/Polkit
BuildArch: noarch
Requires: polkit

%description
%summary.

%install
mkdir -p %buildroot/%_datadir/polkit-1/rules.d
cat>%buildroot/%_datadir/polkit-1/rules.d/60-mobile.rules<<EOF
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.ModemManager1.Contacts" ||
        action.id == "org.freedesktop.ModemManager1.Device.Control" ||
        action.id == "org.freedesktop.ModemManager1.Location" ||
        action.id == "org.freedesktop.ModemManager1.Messaging" ||
        action.id == "org.freedesktop.ModemManager1.Time" ||
        action.id == "org.freedesktop.ModemManager1.USSD" ||
        action.id == "org.freedesktop.ModemManager1.Voice" ||
        action.id == "org.freedesktop.NetworkManager.settings.modify.system")
    {
        return polkit.Result.YES;
    }
});
EOF

%files
%_datadir/polkit-1/rules.d/60-mobile.rules

%changelog
* Thu Aug 17 2023 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
