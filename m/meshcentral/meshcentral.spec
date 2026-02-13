%define _unpackaged_files_terminate_build 1

%define mc_user  meshcentral
%define mc_group meshcentral

Name:    meshcentral
Version: 1.1.56
Release: alt1

Summary: A complete web-based remote monitoring and management web site
License: Apache-2.0
Group:   Networking/Remote access
Url:   	 https://meshcentral.com/
Vcs:     https://github.com/Ylianst/MeshCentral.git

Source: %name-%version.tar
Source1: node_modules.tar
Source2: %name.service

BuildArch: noarch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node

%add_verify_elf_skiplist %nodejs_sitelib/%name/agents/*
%add_findreq_skiplist %nodejs_sitelib/%name/agents/*
%add_findprov_skiplist %nodejs_sitelib/%name/agents/*
%add_findreq_skiplist %nodejs_sitelib/%name/node_modules/*
%add_findprov_skiplist %nodejs_sitelib/%name/node_modules/* 

%description
MeshCentral is a full computer management web site. With MeshCentral,
you can run your own web server to remotely manage and control computers
on a local network or anywhere on the internet. Once you get the server started,
create device group and download and install an agent on each computer you want
to manage. A minute later, the new computer will show up on the web site
and you can take control of it. MeshCentral includes full web-based
remote desktop, terminal and file management capability.

%prep
%setup -a 1

%build

%install
#npm install --production

install -d %buildroot%nodejs_sitelib/meshcentral
cp -a \
  *.js package.json sample-config*.json meshcentral-config-schema.json \
  amt agents emails public rdp translate views node_modules \
  %buildroot%nodejs_sitelib/meshcentral/

sed -i 's|require("../meshcentral.js");|require("../meshcentral.js").mainStart();|' bin/meshcentral

install -Dm0755 bin/%name %buildroot%nodejs_sitelib/%name/bin/%name

install -d %buildroot%_bindir
ln -s %nodejs_sitelib/%name/bin/%name %buildroot%_bindir/%name

install -d %buildroot%_sysconfdir/%name
install -Dm0644 sample-config-advanced.json %buildroot%_sysconfdir/%name/config.json

install -d %buildroot%_localstatedir/%name
install -d %buildroot%_localstatedir/%name/data
install -d %buildroot%_localstatedir/%name/files
install -d %buildroot%_localstatedir/%name/backups

install -Dp -m0644 %SOURCE2 %buildroot%_unitdir/%name.service

%pre
getent group %mc_group >/dev/null || groupadd -r %mc_group
getent passwd %mc_user >/dev/null || \
    useradd -r -g %mc_group -s /sbin/nologin \
    -d %_localstatedir/%name -c "MeshCentral service user" %mc_user
exit 0

%post
%post_service %name

%preun
%preun_service %name

%files
%doc *.md LICENSE
%_bindir/%name
%nodejs_sitelib/%name
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/%name/config.json
%attr(0750,%mc_user,%mc_group) %dir %_localstatedir/%name
%attr(0750,%mc_user,%mc_group) %dir %_localstatedir/%name/data
%attr(0750,%mc_user,%mc_group) %dir %_localstatedir/%name/files
%attr(0750,%mc_user,%mc_group) %dir %_localstatedir/%name/backups

%changelog
* Fri Feb 13 2026 Nikita Shmatko <nash@altlinux.org> 1.1.56-alt1
- Initial build for Sisyphus.
