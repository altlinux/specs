# vim: set ft=spec: -*- rpm-spec -*-
Name:          foreman-addons
Version:       0.0.1
Release:       alt1
Summary:       Default addons for Foreman
License:       GPLv3
Group:         Development/Ruby
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Requires:      gem(foreman_default_hostgroup)
Requires:      gem(foreman_remote_execution)
Requires:      gem(foreman_ansible)
Requires:      gem(foreman-tasks)
Requires:      gem(smart_proxy_dynflow)

%description
%summary.

%files

%changelog
* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- + defaultly packaged
