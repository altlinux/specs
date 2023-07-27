Name: mate-reduced-resource
Version: 0.2
Release: alt1
Summary: Disable compositing and graphical effects for mate
License: GPL
Group: Graphical desktop/MATE
URL: https://www.altlinux.org/Dconf

BuildArch: noarch

Requires: dconf-profile

%description
%summary

%install
mkdir -p %buildroot%_sysconfdir/dconf/db/local.d

cat > %buildroot%_sysconfdir/dconf/db/local.d/01-mate-reduced-resources <<EOF
[org/mate/marco/general]
reduced-resources=true
compositing-manager=false
EOF

%files
%_sysconfdir/dconf/db/local.d/01-mate-reduced-resources

%changelog
* Wed Jul 26 2023 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- do not pack /etc/dconf/profile/user, because it is now provided
  by dconf-profile
- do not run dconf-update, because dconf-profile contain filetrigger
- add Url

* Thu Sep 19 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT
