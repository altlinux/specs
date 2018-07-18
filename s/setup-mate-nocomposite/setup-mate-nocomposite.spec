Name: setup-mate-nocomposite
Version: 0.1
Release: alt2

Summary: set mate windowmanager to non-compositing
License: public domain
Group: Graphical desktop/MATE

BuildArch: noarch

%define filename z-alt-nocomposite.gschema.override
%define conffile %_datadir/glib-2.0/schemas/%filename

%description
%summary
(in case it's unsuitable)

%prep

%build
cat > %filename << EOF
[org.mate.Marco.general]
compositing-manager = false
EOF

%install
install -pDm644 %filename %buildroot%conffile

%files
%config(noreplace) %conffile

%changelog
* Wed Jul 18 2018 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- s/marco/Marco/ (thank you, weird upstream, it was so obvious)

* Wed Jul 18 2018 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on setup-mate-terminal)

