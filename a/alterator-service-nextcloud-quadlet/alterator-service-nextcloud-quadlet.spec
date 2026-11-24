Name: alterator-service-nextcloud-quadlet
Version: 0.2
Release: alt1

Summary: Rootless Podman Quadlets for the Alterator Nextcloud service
License: GPL-2.0-or-later
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-service-nextcloud-quadlet

BuildArch: noarch
Source: %name-%version.tar

Requires: podman >= 5
Requires: systemd

%description
Immutable p11-based Quadlets, PostgreSQL and Redis runtime adaptations, and
user systemd cron units for alterator-service-nextcloud on p11 and Sisyphus.

%prep
%setup -q

%install
asset_root=%buildroot%_datadir/alterator-service-nextcloud-quadlet

install -p -m 0755 -D container/postgresql-entrypoint.sh \
    "$asset_root/container/postgresql-entrypoint.sh"
install -p -m 0644 -D container/redis.conf \
    "$asset_root/container/redis.conf"

for source in quadlet/*.container quadlet/*.pod quadlet/*.volume; do
    install -p -m 0644 -D "$source" \
        "$asset_root/quadlet/${source##*/}"
done
for source in systemd/user/*; do
    install -p -m 0644 -D "$source" \
        "%buildroot%_userunitdir/${source##*/}"
done

%files
%_datadir/alterator-service-nextcloud-quadlet
%_userunitdir/alterator-nextcloud-cron.service
%_userunitdir/alterator-nextcloud-cron.timer

%changelog
* Tue Aug 18 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.2-alt1
- Install cron units only in the standard systemd user unit directory.

* Mon Aug 17 2026 Evgenii Sozonov <arzdez@altlinux.org> 0.1-alt1
- Initial package.
