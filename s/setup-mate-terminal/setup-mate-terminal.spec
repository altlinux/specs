Name: setup-mate-terminal
Version: 0.1
Release: alt1

Summary: set mate terminal's colour scheme to something sane
License: public domain
Group: Graphical desktop/MATE

BuildArch: noarch

%define filename z-alt-terminal.gschema.override
%define conffile %_datadir/glib-2.0/schemas/%filename

%description
%summary
(in case it's almost black-on-black)

%prep

%build
cat > %filename << EOF
[org.mate.terminal.profile]
use-theme-colors = false
foreground-color = "#000000000000"
background-color = "#FFFFFFFFDDDD"
background-type = "solid"
EOF

%install
install -pDm644 %filename %buildroot%conffile

%files
%config(noreplace) %conffile

%changelog
* Thu Mar 15 2018 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (thanks cas@ for the file)

