Name: celluloid-csd-disabled
Version: 0.2
Release: alt1
Summary: Disable client-side decorations and dark-theme for celluloid
License: GPL
Group: Graphical desktop/Other
Url: https://www.altlinux.org/Dconf

BuildArch: noarch

Requires: dconf-profile

%description
%summary

%install
mkdir -p %buildroot%_sysconfdir/dconf/db/local.d

cat > %buildroot%_sysconfdir/dconf/db/local.d/01-celluloid-csd-disabled <<EOF
[io/github/celluloid-player/celluloid]
csd-enable=false
dark-theme-enable=false
EOF

%files
%_sysconfdir/dconf/db/local.d/01-celluloid-csd-disabled

%changelog
* Wed Jul 26 2023 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- do not pack /etc/dconf/profile/user, because it is now provided
  by dconf-profile
- do not run dconf-update, because dconf-profile contain filetrigger
- add Url

* Mon Dec 23 2019 Dmitry Terekhin <jqt4@altlinux.org> 0.1-alt1
- Initial build for ALT
