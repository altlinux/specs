Name: osec-controls
Version: 0.1.0
Release: alt1

Summary: Set of control scripts for OSEC configuration
License: GPLv3+
Group: System/Configuration/Other

Requires: /etc/osec/pipe.conf
Requires: /etc/osec/dirs.conf

Source: %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%install

install -pD -m 0755 osec-send %buildroot%_controldir/osec-send
install -pD -m 0755 osec-dirs %buildroot%_controldir/osec-dirs

%files
%_controldir/osec-*

%changelog
* Tue Aug 04 2020 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial version.
