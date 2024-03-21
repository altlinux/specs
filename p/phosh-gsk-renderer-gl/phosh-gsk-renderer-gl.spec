Name: phosh-gsk-renderer-gl
Version: 0.1
Release: alt1
Summary: Add Environment=GSK_RENDERER=gl for phosh.service
License: GPL-3.0-or-later
Group: Other
Url: https://altlinux.org
BuildArch: noarch
Requires: phosh

%description
%summary.

%install
mkdir -p %buildroot%systemd_unitdir/phosh.service.d
cat>%buildroot%systemd_unitdir/phosh.service.d/GSK_RENDERER_gl.conf<<EOF
[Service]
Environment=GSK_RENDERER=gl
EOF

%files
%systemd_unitdir/phosh.service.d/GSK_RENDERER_gl.conf

%changelog
* Thu Mar 21 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
