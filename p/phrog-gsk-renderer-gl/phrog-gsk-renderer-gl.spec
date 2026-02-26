Name: phrog-gsk-renderer-gl
Version: 0.1
Release: alt1
Summary: Add Environment=GSK_RENDERER=gl for phrog.service
License: GPL-3.0-or-later
Group: Other
Url: https://altlinux.org
BuildArch: noarch
Requires: phrog

%description
%summary.

%install
mkdir -p %buildroot%systemd_unitdir/phrog.service.d
cat>%buildroot%systemd_unitdir/phrog.service.d/GSK_RENDERER_gl.conf<<EOF
[Service]
Environment=GSK_RENDERER=gl
EOF

%files
%systemd_unitdir/phrog.service.d/GSK_RENDERER_gl.conf

%changelog
* Wed Feb 25 2026 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
