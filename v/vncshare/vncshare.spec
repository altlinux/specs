Name:           vncshare
Version:        0.01
Release:        alt1
Summary:        VNC shared screens infrastructure
Group:          Networking/Remote access
Source:         %name-%version.tar
BuildArch:      noarch
License:        MIT
VCS:            https://altlinux.space/george/vncshare

Requires:       /usr/bin/vncserver

%description
%summary.

%prep
%setup

%install
for F in VNC*; do install -D $F %buildroot%_bindir/$F; done

%files
%doc *.md
%_bindir/*


%changelog
* Tue Jul 29 2025 Fr. Br. George <george@altlinux.org> 0.01-alt1
- Initial build for ALT
