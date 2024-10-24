%define _unpackaged_files_terminate_build 1
%define u7s_admin_usr u7s-admin
%define u7s_admin_grp u7s-admin
%define kubernetes_grp kube
%define _libexecdir %_prefix/libexec
%define u7s_admin_homedir %_localstatedir/%u7s_admin_usr

Name: podsec
Version: 1.2.2
Release: alt1

Summary: Set of scripts for Podman Security
License: GPLv2+
Group: Development/Other
Url: https://github.com/alt-cloud/podsec
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): libsystemd-devel
BuildRequires(pre): ronn

Requires: nginx
Requires: docker-registry
Requires: pinentry-common

%description
This package contains utilities for:
- setting the most secure container application access policies
  (directory /etc/containers/)
- installation of a registry and a web server for access to image signatures
- creating a user with rights to create docker images, signing them and
  placing them in the registry
- creating users with rights to run containers in rootless mode
- downloading docker images from the oci archive, placing them
  on the local system, signing and placing them on the registry
- deploying a rootless kubernetes cluster

%package k8s
Summary: Set of scripts for Kubernetes Security
Group: Development/Other
Requires: cri-tools

%description k8s
This package contains utilities for:
- deploying a rootless kubernetes cluster
- cluster node configurations

%package k8s-rbac
Summary: Set of scripts for Kubernetes RBAC
Group: Development/Other

%description k8s-rbac
This package contains utilities for
- creating RBAC users
- generation of certificates and configuration files for users
- generating cluster and usual roles and binding them to users

%package inotify
Summary: Set of scripts for security monitoring
Group: Development/Other
Requires: trivy
Requires: trivy-server

%description inotify
A set of scripts for  security monitoring by systemd timers
to monitor and identify security threats

%package dev
Summary: Set of scripts for podsec developers
Group: Development/Other

%description dev
A set of scripts for developers

%package icinga
Summary: %name-inotify monitoring templates for Icinga 2
Group: Monitoring
Requires: nagwad-icinga-templates >= 0.11.2

%description icinga
Monitoring templates for Icinga 2 defining services to monitor
various Podsec events.

%package nagios
Summary: %name-inotify monitoring templates for Nagios
Group: Monitoring
Requires: nagwad-nagios-templates >= 0.11.2

%description nagios
Monitoring templates for Nagios defining services to monitor
various Podsec events.

%prep
%setup

%build
%make_build

%install
%makeinstall_std unitdir=%_unitdir modulesloaddir=%_modules_loaddir

# JSON templates are packaged using %%doc:
rm -fv %buildroot%_datadir/doc/podsec/podsec-icinga2.json

%pre
groupadd -r -f podman >/dev/null 2>&1 ||:
groupadd -r -f podman_dev >/dev/null 2>&1 ||:

%pre k8s
groupadd -r -f %u7s_admin_grp  2>&1 ||:
useradd -M -r -g %u7s_admin_grp -d %u7s_admin_homedir -G %kubernetes_grp,systemd-journal,podman \
    -c 'usernet user account'  %u7s_admin_usr  2>&1 ||:
mkdir -p %u7s_admin_homedir
# merge usernetes & podman graphroot
mkdir -p %u7s_admin_homedir/.local/share/usernetes/containers 2>&1 ||:
cd %u7s_admin_homedir/.local/share
if [ -d containers ]; then mv containers containers.old; rm -rfv containers.old; fi
ln -sf usernetes/containers . 2>&1 ||:
cd %u7s_admin_homedir/.local/share/usernetes/containers
chown -R %u7s_admin_usr:%u7s_admin_grp %u7s_admin_homedir

%post inotify
%post_systemd podsec-inotify-check-containers.service
%post_systemd podsec-inotify-check-kubeapi.service

%preun inotify
%preun_systemd podsec-inotify-check-containers.service
%preun_systemd podsec-inotify-check-kubeapi.service

%post k8s
%post_systemd  u7s.service

%preun k8s
%preun_systemd u7s.service

%files
%dir %_mandir/ru/man1
%dir %_sysconfdir/nagwad/
%_datadir/locale/ru/LC_MESSAGES/podsec.mo
%_mandir/ru/man1/podsec-create-imagemakeruser.1.xz
%_mandir/ru/man1/podsec-create-podmanusers.1.xz
%_mandir/ru/man1/podsec-create-policy.1.xz
%_mandir/ru/man1/podsec-create-services.1.xz
%_mandir/ru/man1/podsec-load-sign-oci.1.xz
%_mandir/man1/podsec-create-imagemakeruser.1.xz
%_mandir/man1/podsec-create-podmanusers.1.xz
%_mandir/man1/podsec-create-policy.1.xz
%_mandir/man1/podsec-create-services.1.xz
%_mandir/man1/podsec-load-sign-oci.1.xz
%config(noreplace) %_sysconfdir/nagwad/podsec.sed
%dir %_sysconfdir/podsec
%dir %_libexecdir/podsec
%dir %_localstatedir/podsec
%_bindir/podsec-functions
%_bindir/podsec-get-platform
%_bindir/podsec-load-sign-oci
%_bindir/podsec-policy-functions
%defattr (0700,root,root, -)
%_bindir/podsec-create-imagemakeruser
%_bindir/podsec-create-podmanusers
%_bindir/podsec-create-policy
%_bindir/podsec-create-services


%files k8s
%_datadir/locale/ru/LC_MESSAGES/podsec-k8s.mo
%_bindir/podsec-u7s-kubeadm
%_bindir/podsec-u7s-functions
%_unitdir/u7s.service
%_unitdir/user@.service.d/delegate.conf

%config %_modules_loaddir/u7s.conf
%dir %_mandir/ru/man1
%_mandir/ru/man1/podsec-u7s-kubeadm.1.xz
%_mandir/man1/podsec-u7s-kubeadm.1.xz
%_userunitdir/kubelet.service
%_userunitdir/rootlesskit.service

%defattr (0700,%u7s_admin_usr,%u7s_admin_grp, 0700)
%dir %_sysconfdir/podsec/u7s
%dir %_sysconfdir/podsec/u7s/audit
%dir %_sysconfdir/podsec/u7s/config
%dir %_sysconfdir/podsec/u7s/config/cni_net.d
%dir %_sysconfdir/podsec/u7s/config/flannel
%dir %_sysconfdir/podsec/u7s/config/flannel/cni_net.d
%dir %_sysconfdir/podsec/u7s/config/flannel/etcd
%dir %_sysconfdir/podsec/u7s/config/kubeadm-configs
%dir %_sysconfdir/podsec/u7s/env
%dir %_sysconfdir/podsec/u7s/manifests/
%dir %_sysconfdir/podsec/u7s/manifests/kube-flannel
%dir %_sysconfdir/podsec/u7s/manifests/kube-flannel/*
%dir %_sysconfdir/podsec/u7s/manifests/kube-flannel/*/*
%dir %_sysconfdir/podsec/u7s/manifests/kube-flannel/*/*/*

%dir %u7s_admin_homedir
%dir %u7s_admin_homedir/.local
%dir %u7s_admin_homedir/.local/share
%dir %u7s_admin_homedir/.local/share/usernetes
%dir %u7s_admin_homedir/.local/share/usernetes/containers

%dir %_localstatedir/podsec/u7s
%dir %_localstatedir/podsec/u7s/etcd
%dir %_localstatedir/podsec/u7s/log
%dir %_localstatedir/podsec/u7s/log/kubeapi
%dir %_libexecdir/podsec/u7s
%dir %_libexecdir/podsec/u7s/bin

%_libexecdir/podsec/u7s/bin/kubeadm
%_libexecdir/podsec/u7s/bin/u7sinit.sh
%_libexecdir/podsec/u7s/bin/crio.sh
%_libexecdir/podsec/u7s/bin/init-crio.sh
%_libexecdir/podsec/u7s/bin/_kubeadm.sh
%_libexecdir/podsec/u7s/bin/_kubelet.sh
%_libexecdir/podsec/u7s/bin/rootlessctl
%_libexecdir/podsec/u7s/bin/systemctl
%_libexecdir/podsec/u7s/bin/u7s-start-stop.sh
%_libexecdir/podsec/u7s/bin/kubeadm.sh
%_libexecdir/podsec/u7s/bin/kubelet.sh
%_libexecdir/podsec/u7s/bin/nsenter_u7s
%_libexecdir/podsec/u7s/bin/rootlesskit.sh

%defattr (0600,%u7s_admin_usr,%u7s_admin_grp, -)
%config %_sysconfdir/podsec/u7s/config/kubeadm-configs/InitClusterConfiguration.yaml
%config %_sysconfdir/podsec/u7s/config/kubeadm-configs/InitConfiguration.yaml
%config %_sysconfdir/podsec/u7s/config/kubeadm-configs/JoinClusterConfiguration.yaml
%config %_sysconfdir/podsec/u7s/config/kubeadm-configs/JoinConfiguration.yaml
%config %_sysconfdir/podsec/u7s/config/kubeadm-configs/JoinControlPlaneConfijuration.yaml
%config %_sysconfdir/podsec/u7s/config/kubeadm-configs/KubeletConfiguration.yaml
%config %_sysconfdir/podsec/u7s/config/kubeadm-configs/KubeProxyConfiguration.yaml
%config %_sysconfdir/podsec/u7s/env/u7s_flags
%config %_sysconfdir/podsec/u7s/env/u7s_images
%config %_sysconfdir/podsec/u7s/manifests/coredns.yaml
%config %_sysconfdir/podsec/u7s/manifests/kube-flannel/*/*/*/kube-flannel.yml
%config %_sysconfdir/podsec/u7s/config/cni_net.d/99-loopback.conf
%config %_sysconfdir/podsec/u7s/audit/policy.yaml
%config %_sysconfdir/podsec/u7s/config/flannel/etcd/coreos.com_network_config
%config %_sysconfdir/podsec/u7s/config/env
%config %_sysconfdir/podsec/u7s/config/ENV
%config %_sysconfdir/podsec/u7s/config/flannel/cni_net.d/10-flannel.conflist

%files k8s-rbac
%_datadir/locale/ru/LC_MESSAGES/podsec-k8s-rbac.mo
%_bindir/podsec-k8s-rbac-bindrole
%_bindir/podsec-k8s-rbac-create-kubeconfig
%_bindir/podsec-k8s-rbac-create-remoteplace
%_bindir/podsec-k8s-rbac-create-user
%_bindir/podsec-k8s-rbac-functions
%_bindir/podsec-k8s-rbac-get-userroles
%_bindir/podsec-k8s-rbac-unbindrole
%dir %_mandir/ru/man1
%_mandir/ru/man1/podsec-k8s-rbac-bindrole.1.xz
%_mandir/ru/man1/podsec-k8s-rbac-create-kubeconfig.1.xz
%_mandir/ru/man1/podsec-k8s-rbac-create-remoteplace.1.xz
%_mandir/ru/man1/podsec-k8s-rbac-create-user.1.xz
%_mandir/ru/man1/podsec-k8s-rbac-get-userroles.1.xz
%_mandir/ru/man1/podsec-k8s-rbac-unbindrole.1.xz
%_mandir/man1/podsec-k8s-rbac-bindrole.1.xz
%_mandir/man1/podsec-k8s-rbac-create-kubeconfig.1.xz
%_mandir/man1/podsec-k8s-rbac-create-remoteplace.1.xz
%_mandir/man1/podsec-k8s-rbac-create-user.1.xz
%_mandir/man1/podsec-k8s-rbac-get-userroles.1.xz
%_mandir/man1/podsec-k8s-rbac-unbindrole.1.xz

%files inotify
%dir %_mandir/ru/man1
%_mandir/ru/man1/podsec-inotify-build-invulnerable-image.1.xz
%_mandir/ru/man1/podsec-inotify-check-containers.1.xz
%_mandir/ru/man1/podsec-inotify-check-images.1.xz
%_mandir/ru/man1/podsec-inotify-check-kubeapi.1.xz
%_mandir/ru/man1/podsec-inotify-check-policy.1.xz
%_mandir/ru/man1/podsec-inotify-check-vuln.1.xz
%_mandir/man1/podsec-inotify-build-invulnerable-image.1.xz
%_mandir/man1/podsec-inotify-check-containers.1.xz
%_mandir/man1/podsec-inotify-check-images.1.xz
%_mandir/man1/podsec-inotify-check-kubeapi.1.xz
%_mandir/man1/podsec-inotify-check-policy.1.xz
%_mandir/man1/podsec-inotify-check-vuln.1.xz
%_unitdir/podsec-inotify-check-containers.service
%_unitdir/podsec-inotify-check-images.service
%_unitdir/podsec-inotify-check-images.timer
%_unitdir/podsec-inotify-check-kubeapi-mail.service
%_unitdir/podsec-inotify-check-kubeapi-mail.timer
%_unitdir/podsec-inotify-check-kubeapi.service
%_unitdir/podsec-inotify-check-policy.service
%_unitdir/podsec-inotify-check-policy.timer
%_unitdir/podsec-inotify-check-vuln.service
%_unitdir/podsec-inotify-check-vuln.timer

%_bindir/podsec-inotify-functions
%_datadir/locale/ru/LC_MESSAGES/podsec-inotify.mo
%_bindir/podsec-inotify-build-invulnerable-image
%_bindir/podsec-inotify-check-vuln

%defattr (0500,root, root, -)
%_bindir/podsec-inotify-check-containers
%_bindir/podsec-inotify-check-images
%_bindir/podsec-inotify-check-kubeapi
%_bindir/podsec-inotify-check-policy

%files dev
%dir %_mandir/ru/man1
%_mandir/man1/podsec-k8s-save-oci.1.xz
%_mandir/ru/man1/podsec-k8s-save-oci.1.xz
%_mandir/man1/podsec-save-oci.1.xz
%_mandir/ru/man1/podsec-save-oci.1.xz
%defattr (0400,%u7s_admin_usr,%u7s_admin_grp, -)
%_bindir/podsec-save-oci
%_bindir/podsec-k8s-save-oci

%files icinga
%doc podsec-inotify/monitoring/podsec-icinga2.json
%config(noreplace) %_sysconfdir/icinga2/conf.d/podsec.conf

%files nagios
%config(noreplace) %_sysconfdir/nagios/templates/podsec-services.cfg
%config(noreplace) %_sysconfdir/nagios/nrpe-commands/podsec-commands.cfg

%changelog
* Thu Oct 24 2024 Alexey Kostarev <kaf@altlinux.org> 1.2.2-alt1
- Add kube group to user u7s-admin.
- Optimized podsec.spec by using defattr.
- Removed unnecessary Requires from podsec.spec.
- Changed control for newuidmap, newgidmap from public to podmanonly.

* Thu Oct 17 2024 Alexey Kostarev <kaf@altlinux.org> 1.2.1-alt1
- Removed man files from podsec*/man.
- Adden generation man files to Makefile.

* Thu Oct 17 2024 Alexey Kostarev <kaf@altlinux.org> 1.2.0-alt1
- Created english md-catalogs podsec*/md/en.
- Created russian md-catalogs podsec*/md/ru.
- Moved russian md-files to podsec*/md/ru.
- Translated russion md-files to english md-files in podsec*/md/en.
- Created russian man-catalogs podsec*/man/ru.
- Created english man-catalogs podsec*/man/en.
- Removed russiian man pages.
- Generated Russian and English man pages based on Russian and English md files.
- Debugged podsec/bin/podsec-create-policy.

* Wed Oct 16 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.11-alt1
- Added localization files to podsec.spec.
- Added localization files to Makefile.
- Added localization of the podsec-inotify package.
- Added localization of the podsec-k8s-rbac package.
- Added localization of the podsec-k8s package.
- Added localization of the podsec package.

* Fri Oct 11 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.10-alt1
- Removed dependencies from the podsec-k8s package since the kubernetes version is determined when deploying the cluster.
- Changed owners, access right of dirs, executable, configurations and usual files.
- Moved installation of the kube group for a user u7s-admin from podsec.spec to the installKubeadm function after deploying kubernetes packages.
- Removed unused script podsec-k8s-create-master.

* Sat Oct 05 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.9-alt1
- Moved resetting PATH from profiles to bin/podsec-u7s-functions.
- Added dirs of u7s-admin user to SPEC.
- Added dependency on nagwad-service to SPEC.
- Change access mode to 0700 on ~u7s-admin/.local/... dirs tree.
- Change access mode to 0700 on /usr/libexec/podsec/u7s/bin/*.sh scripts.

* Sat Oct 05 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.8-alt5
Change access mode 0700 to ~u7s-admin/.local/..., /usr/libexec/podsec/u7s/bin/*.sh  dirs and files.

* Thu Oct 03 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.8-alt4
- Moved resetting PATH from profiles to bin/podsec-u7s-functions.
- Added dependency on nagwad-service to SPEC.
- Added to SPEC dirs of u7s-admin user.

* Tue Oct 01 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.8-alt3
- Added dir /etc/nagwad to SPEC

* Mon Sep 30 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.8-alt2
- Added owners to /etc/podsec/u7s

* Mon Sep 30 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.8-alt1
- Added podsec-inotify-build-.* template to /etc/nagwad/podsec.sed (thnx gritsynin@ivk.ru)

* Mon Sep 30 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.7-alt3
- Removed user u7s-admin files from spec.
- Replaced files templates with a list of files.
- Replaced -M (--no-create-home) flag to -m (--create-home) in command useradd
- Added flag -k /etc/skel () in command useradd

* Thu Sep 26 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.7-alt2
- Finished translation records of changelog to past simple.

* Wed Sep 25 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.7-alt1
- Adjusted changelog of podsec.spec to comply with recommendations.
- Added support for loading additional images into the archive.

* Tue Sep 17 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.6-alt5
- Changed algorithm for checking the access policy to registries.

* Fri Aug 23 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.6-alt4
- Fixed syntax of podsec-icinga2.json (thx Makeenkov Alexander).
- Clarified and corrected some wording in the descriptions of Nagios and Icinga events.
- Removed erroneous definition of members from the "nagwad-podsec" block of the servicegroup type.

* Wed Aug 21 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.6-alt3
- Corrected documentation for podsec-inotify scripts.
- The configuration files and monitoring templates changed in accordance with changes in podsec/nagwad/podsec.sed.

* Tue Aug 06 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.6-alt2
- Added support for multiple buckets in nagwad template - one for each podsec-inotify script.
- Corrected documentation on trivy.local domain support for c10f platform.
- Added psmisk (command fuser) dependency to package podsec-inotify.

* Sun Jul 28 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.6-alt1
- Rewritten script podsec-inotify-check-containers.
- Updated man's.

* Thu Jul 11 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.5-alt2
- Added SyslogIdentifier to all services.

* Mon Jul 01 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.5-alt1
- Changed the format of outputting system messages via logger - script name as a tag.

* Mon Jul 01 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.4-alt1
- Completed integration of podsec-inotify scripts with nagwad, icigna2, nagios.
- Renamed podsec templates for Icinga 2 and Nagios.
- Added host template "podsec-host".
- Fixed "d-nagwad-podsec" service definition.

* Mon Jul 01 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.3-alt1
- Improved podsec-inotify-check-kubeapi for correct logging.

* Fri Jun 28 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.2-alt1
- Merged rootless usernetes container catalog with podman.

* Fri Jun 28 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.1-alt1
- Changed nagwad-icigna, nagwad-nagios monitoring configuration files to support a single podsec bucket.

* Thu Jun 27 2024 Alexey Kostarev <kaf@altlinux.org> 1.1.0-alt1
- Changed message format and output format in sed template, set of 6 nagwad buckets podsec-inotify-* reduced to 1 podsec.

* Wed Jun 26 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.14-alt2
- Created universal sed template for nagwad and moved to podsec package.
- Removed podsec-nagwad package.

* Wed Jun 26 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.14-alt1
- Merged manowar branch.
- Added podsec-nagwad, podsec-nagwad-icinga, podsec-nagwad-nagios packages] (thnx @manowar).

* Tue Jun 25 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.13-alt1
- Configured scripts that use tryvy to analyze images.
- Added trivy.local to information messages and documentation.
- Added podsec-inotify/bin/podsec-inotify-build-invulnerable-image script to podsec-inotify package.
- Fixed for podsec-inotify scripts that were found in shellcheck.
- Specified the /bin/bash interpreter in the script header.
- Added the trivy server to regitry.local registry.
- Added the trivy.local domain to /etc/hosts to work with the cluster trivy server.

* Wed Jun 19 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.12-alt2
- Changed priorities of system messages according to syslog.
- Set correct enfFile when calling podsec-u7s-functions in the root user environment.
- In podsec-inotify/bin/podsec-inotify-build-invulnerable-image added image removal in case of unsuccessful trivy completion.

* Mon Jun 17 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.12-alt1
- Added usrmerge support.

* Wed Jun 05 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.11-alt1
- Fixed specification merge errors.
- Fixed documentation.
- Improved script exit codes for correct operation in systemd/timers.
- Added -M Email flag to scripts, if present, the final message is sent by mail to the specified user.
- Fixed BUG when generating flannel images (only loaded by default amd64).
- Eliminate situations of incorrect address transfer in checkNetCrossing.
- Fixed BUG for fannel-cni-plugin.
- Removed dependency on negios.

* Tue May 28 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.10-alt10
- Fixed BUG when generating flannel images (only amd64 were loaded by default).

* Wed May 22 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.10-alt9
- Eliminated situations of incorrect address transfer in checkNetCrossing.
- Fixed BUG for fannel-cni-plugin.
- Removed dependency on negios.

* Sat Apr 27 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.10-alt8
- Removed IP address configuration code in 50-bridge.conf.
- Removed cni_net.d/50-bridge.conf to avoid setting the address 10.88.0.1 for cni0.
- Formed pairs flannel, flannel-cni-plugins from the tree of files kube-flannel.yml.
- Added support for U7S_CNINET, intersection analysis networks crossing, bug fixes.
- Added functions: getCniVersion, checkNetCrossing.
- Fixed for /podsec-inotify-check-vuln - incorrect analysis of HIGH level errors:.
- Fixed platform detection error for c10f2.
- Added apt-get update command.
- Fixed podsec-load-sign-oci bug when working with "foreign" images.

* Thu Apr 18 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.10-alt7
- Added superuser (root) control when calling kubead@podsec-k8s, podsec-k8s-save-oci.
- If minor versions of kubeadm match, crio are not installed.
- Fixed BUGs.

* Tue Apr 09 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.10-alt6
- Switch to preloading images via skopeo.
- Added support for correct formation of the image archive.
- Modified podsec-k8s-save-oci, podsec-save-oci to use the getKuberImages function.
- Added extraction of the u7s_images code into a separate getKuberImages() function.
- Added support for the ability to write images to the archive from the local cache.
- Optimized the algorithm for removing and installing kuber packages.
- Removed unnecessary dependencies.
- Removed the dependency on the crio package, automatic detection of the latest available image tags flannel, flannel-cni-plugin, cert-manager-controller-* and loading them.
- Added features:.
+ In the absence of the requested kuber image tags in the registrar and the presence of the U7S_SETAVAILABLEIMAGES=yes environment variable, loading the latest patch version of coredns images, pause, etcd, kube-controller-manager, kube-apiserver, kube-proxy, kube-scheduler.
+ Automatically detect the latest available image tags flannel, flannel-cni-plugin, cert-manager-controller-* and download them.
+ If the requested kuber-image tags are missing from the registrar and the environment variable U7S_SETAVAILABLEIMAGES=yes is present, download the latest patch version of the coredns, pause, etcd, kube-controller-manager, kube-apiserver, kube-proxy, kube-scheduler images.
+ Install U7S_KUBEVERSION if there is none based on the latest version in the registrar.
- Added in-depth analysis of the installed kubernetes version.
- Optimized flag analysis.

* Fri Mar 01 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.10-alt5
- To eliminate circular dependencies, the platform detection function sisyphus, p10, c10 was moved from the podsec-k8s package to the podsec package.
- Moved pause image settings from podsec to podsec-k8s.

* Mon Feb 26 2024 Alexey Shabalin <shaba@altlinux.org> 1.0.10-alt4
- Fixed useradd u7s-admin.
- Fixed package podsec-inotify-*.
- Add support archiving the kubernetes version specified in the U7S_KUBEVERSION environment variable.
- Fixed a bug with a dependency on /etc/kubernetes/kubelet.

* Fri Feb 23 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.10-alt3
- Upgraded the default kubernetes version from 1.26.9 to 1.26.11.
- Fixed conflict with /usr/lib/nagios/plugins/.
- Added support for packing additional images in podsec-k8s-save-oci.

* Wed Jan 31 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.10-alt2
- Added permissions to .config, ,local.
- Included in k8s package .?? directories and files.

* Tue Nov 07 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.10-alt1
- Added support for installing minor versions of kubernetes packages if none are specified.
- Updated MANs.
- Removed podsec-inotify-check-vuln service, switch to trivy service (server).
- Trivy-server service launch added to podsec-inotify-server-trivy service if there is a local vulnerability database /var/lib/trivy/db/trivy.db.
- Removed min_kube_minor_version from podsec.spec.
- Removed kubernetes-x.y.z-client dependency from podsec-k8s-rbac.
- Added dependencies to podsec-k8s-rbac.
- Added earlier installation of packages.
- Corrected formation of subcommands contents.
- Corrected replacement port 80 to 81 in /etc/hosts.
- Corrected processing of FLAG_control_plane_endpoint for join.
- Added U7S_ALTREGISTRY variable.
- Updated flannel* versions.
- Optimized of podsec-u7s-kubeadm code.
- Moved u7s_flags to usernetes/env/.
- Edited the default version of certmanager.
- Improvements to the correct definition of the list and version of kuber images.
- Adding U7S_KUBEADFLAGS variable containing all additional kubeadm flags.
- Added analysis and processing of flags.
- Added support for flags via getopt.
- Documented kubeadm flags in /docs/kubead/README.md.
- Added request for deletion of the /var/lib/podsec/u7s/etcd directory if it exists during init and join.
- Updated platform detection for sisyphus.
- Added more accurate automatic detection of environment variables U7S_PLATFORM, U7S_KUBEVERSION.
- Documented kubeadm flags in /docs/kubeadm/README.md.
- Moved tuneAudit after CNI startup, restart services after tuneAudit.
- Removed u7s.target and its dependencies.
- Replaced u7s.target with /usr/libexec/podsec/u7s/bin/.
- Added kubernetes-crio dependency.
- Added kubernetes$kubeVersion-crio installation, kubernetes-crio dependency.
- Removed dependencies on kubernetes1.26-*, added dependency on kubernetes1.26-common.
- Updated dependencies on versioned packages min_kube_minor_version.
- Added replacement in u7s-images the list of images with a call to kubeadm config images list.
- Added config, version flags to kubeadm.
- Added apt-get install command to replace the kubernetes and cri-o packages specified in the U7S_KUBEVERSION variable.
- Removed dependencies on kubernetes-master, kubernetes-node, flannel, etcd, there are images for this.
- Added the ability to specify U7S_PLATFORM.

* Mon Oct 30 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.9-alt1
- Added the ability to generate an image archive both before and after installing kuber.
- Added uUsing envFile during initialization after its creation instead of setRegistry.
- Added universalization of the registrar name in podsec-save-oci.
- Added the setRegistryName function.
- Added new the U7S_REGISTRY generation algorithm, names images.
- Added formation of correct image and flannel names when working with a standard registrar.
- The transition from the configuration by the distribution type (k8s-p10, k8s-c10f1) to the configuration by the kubernetes version was carried out, its inclusion in the platform.
- Added kubernetesVersion to config init file.
- Fixed dev/null error.
- Fixed error in flannel image version for p10.
- Added redirecting connection errors when restarting kubeapi-server to /dev/null.
- Fixed error output text in podsec-load-sign-oci.
- Added English README.md.
- Documentation in README.md has been improved with a link to https://www.altlinux.org/Rootless_kubernetes.
- Eliminated of "hanging" 10.96.x.x cluster addresses on tap interfaces.

* Tue Sep 26 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.8-alt1
- Removed static cluster addresses 10.96.x.x and variable U7S_TAPIP storing this address.
- Removed allocation of static cluster IP addresses 10.96.x.x on interfaces.

* Thu Sep 21 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.7-alt1
- Removed fuse group.
- Fixed syntaxis.
- Separates work with /etc/cni/net.d for flannel and calico.
- Added run CNI-pligins after kubeadm finishes on initMaster.
- Fixed: print a newline character after the info log.
- Corrected documentation.
- Added support for heterogeneous clusters (RoolFullLess).
- Removes fuse group.
- Added start CNI-pligins after kubeadm finishes on initMaster.
- Added additional calico ports.
- Added port forwarding 5473 for calico.
- Added configure the mount mode for correct calico operation.
- Adjusted pod-network-cidr flag analysis.
- Moved /etc/kubernetes/manifests/, audit to /etc/podsec/u7s/manifests/ to save manifests after kubeadm reset.
- Added configure the mount mode for correct calico operation.
- Added environment variable U7S_CNI_PLUGIN=flannel|calico.
- Adjusted pod-network-cidr flag analysis.
- Moved /etc/kubernetes/manifests/, audit to /etc/podsec/u7s/manifests/ to save manifests after kubeadm reset.
- Fixed: make corrections to the abstracts.
- Fixed: print a newline character after the info log.
- Optimized commits.
- Removed dependency on vixie-cron, added mans to podsec-inotify.
- Created LICENSE.
- Correct documentation.
- Added LICENSE.
- Merged edits from Alexander Stepchenko's shift into podsec-u7s-kubeadm (thnx Alexander Stepchenko).
- Fixed usage message, debug level detection, and command line arguments handling.
- Added scripts and timers replacing the corresponding crontabs scripts.
- Removed cron scripts.
- Added scripts and timers replacing the corresponding crontabs scripts.
- Implemented support for heterogeneous clusters (RoolFullLess).

* Tue Jul 25 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.6-alt1
- Removed dependency on vixie-cron, added man's to podsec-inotify.
- Fixed: forward positional arguments to the native kubeadm.
- Fixed: exit when command line arguments are incorrect.
- Fixed: properly check debug level (0 <= debugLevel <= 9).
- Fixed: remove option `-n` of `echo` to have a newline character at the end of line.
- Removed cron scripts.
- Added scripts and timers replacing the corresponding crontabs scripts.
- Added U7S_REGISTRY_PLATFORM environment variable.
- Replaced the remaining registry.local with U7S_REGISTRY in scripts.
- Added creation of the podman group in podman-k8s.
- Removed u7s-admin belonging to the fuse group due to the absence of this group.

* Sat Jul 15 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.5-alt1
- Added implementation of the ability to install kuber from registrars other than registry.local (registry.altlinux.ru, ...).
- Removed code implemented in usernetes/bin/_kubeadm.sh from podsec.spec.
- Set the U7S_REGISTRY variable and its value in InitClusterConfiguration.yaml, JoinClusterConfiguration.yaml.
- Corrected syntax errors found during testing.
- Updated roadmap-20230601.md.

* Mon Jun 19 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.4-alt1
- Set the _CONTAINERS_ROOTLESS_UID, _CONTAINERS_USERNS, _CONTAINERS_USERNS_CONFIGURED environment variables in the crio runtime for correct environment detection execution.
- The logic of podsec-inotify-check-vuln has been changed - when called from root, rootless, rootfull images are checked, when called from a regular USER - only his images.
- Added writes mail if there are any threats HIGH > Low to podsec-inotify-check-vuln.
- Regenerated man pages.
- Documented directories have been moved to docs.
- Edited documentation.
- Formeted README.md.
- Added roadmap.
- Added support for archiving signed images by removing signatures.
- Added checking the installed platform when loading and deploying.
- Changed the flannel version to 0.21.4.

* Fri May 26 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.3-alt1
- podsec for two platforms is combined into one.
- Added translation of scripts for automatic platform detection and image configuration.
- Added translation of scripts for configuration on the current platform - k8s-c10f1, k8s-p10.

* Fri May 26 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.2-alt1
- Changed flannel version to 0.21.4.

* Fri May 26 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.1-alt1
- Added translation of scripts for configuration on the current platform - k8s-c10f1, k8s-p10.
- Corrected syntax errors in documentation and code.

* Wed May 24 2023 Alexey Kostarev <kaf@altlinux.org> 1.0.0-alt1
- Fixed flannel operation, corrected work with images and launch of nginx-deployment, al/alt image with DNS check.
- Corrected typos.
- Finalized documentation on launching deploymants and pod's.
- Added copying all plugins to /opt/cni/bin.

* Tue May 23 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.39-alt1
- Corrected launch of flannel with cni-plugin.
- Added cancel mounting of /opt/cni/bin directory.
- Edited documentation.

* Mon May 22 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.38-alt1
- Added documentation for testing has been added.
- Added support for copying keys and policy.json to a new node.
- Transition to images with the prefix k8s-c10f1.
- Replaced the k8s-p10 prefix with k8s-c10f1.
- Created the podsec-dev package.
- Transition from k8s-p10 to k8s-c10f1.

* Mon May 22 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.37-alt1
- Edited of /var/lib/podsec directory ownership by packages.
- Added podsec-inotify-check-images.
- Completed documentation on podsec-inotify-check-images.
- Added podsec-inotify-check-images script with crontabs.
- Added write last event time to separate file to podsec-inotify-check-kubeapi.
- Deleted of testers' comments.
- Transfer mail sending from cron to podsec-inotify-check-policy script.
- Completed creation and description of monitoring scripts podsec-inotify-check-kubeapi, podsec-inotify-check-policy, podsec-inotify-check-vuln.

* Fri May 19 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.36-alt1
- Added man's for monitoring scripts podsec-inotify-check-kubeapi, podsec-inotify-check-policy, podsec-inotify-check-vuln.
- Adding trivy server.
- Tested policy-check service.

* Fri May 19 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.35-alt1
- Restored Rights to etcd directory.
- Added service file podsec-inotify-check-kubeapi.service.

* Thu May 18 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.34-alt1
- Created additional inotify programs (podsec-inotify-check-kubeapi).
- Changed the scheme for calling programs via cron - /var/spool/crontab/root.
- Added audit of API requests.
- Created a new audit policy, fixed bugs podsec-k8s-rbac-create-kubeconfig.
- Added main audit files and functions.
- Added YAML file /etc/kubernetes/audit.policy.
- Added cron.hourly for *checkpolicy.

* Wed May 17 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.33-alt1
- Fixed bugs, replaced extIP mask search algorithm.
- Fixed bugs.
- Added podsec-inotify-check-vuln.
- Documentation revision.
- Added /usr/bin/rootlessctl script.
- Done Code revision.
- Done optimization.
- Fixed bugs.
- Rewrited getExtIP(), getExtDev() to work correctly with network masks.

* Tue May 16 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.32-alt1
- Fixed errors noticed by testers.
- Sdded support for connecting control-plane nodes !!!!!!!!!!.
- Edited service dependencies.
- Configured podsec-inotify package, add documentation, optimize scripts.
- Prepared documentation for connecting control-plane nodes.
- Configured podsec-inotify package.
- Ensured Control Plane connection.
- Splitted ClusterConfigurationWithEtcd.yaml into InitClusterConfiguration.yaml and JoinClusterConfiguration.yaml.
- Edited for testing department comments.
- Fixed kuber version from 1.24.8 to 1.26.3.
- Added display certificateKey in join master.
- Added nagios, systemd directory owners.

* Mon May 15 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.30-alt1
- Display certificateKey in join master.
- Updated README.md.

* Sun May 14 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.28-alt1
- Move delegate.conf from /etc/systemd to /lib/systemd.
- Removed debug.
- Fixed bugs.

* Sun May 14 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.27-alt1
- Fixed notes.

* Sun May 14 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.26-alt1
- Fixed notes.

* Sun May 14 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.25-alt1
- Added nagios, systemd directory owners.

* Sun May 14 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.24-alt1
- Added kubeadm flags for setting network addresses.
- Added support for kubeadm join --certificate-key.
- Added support for --pod-network-cidr.
- Configure Join Control Plane.
- Found correct directory for etcd.
- Added support for apiserver-advertise-address, control-plane-endpoint, service-cidr flags.

* Sun May 14 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.23-alt1
- Configured Join Control Plane.
- Debugged kube-proxy, coredns startup after reboot.

* Fri May 12 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.22-alt1
- Take ca.crt from the usual place /etc/kubernetes/.
- Added redirection 443 to 6443 after rule in PREROUTE.
- Moved usernetes.conf to /lib/modules-load.d/.
- Added wait for socket from rootlesslit service to _kubeadm.sh.
- Added wait for socket from rootlesslit service to _kubeadm.sh.
- Replaced HOME, optimized.
- Removed unimplemented podsec-inotify scripts.
- Fixed BUGs in spec and Makefile:
+ Replace "mkdir -p" -> $(MKDIR_P).
+ define more variables and allow redefine over environment.
+ define _libexecdir in rpm spec.
+ define libexecdir as /usr/libexec.
+ libexecdir=/usr/libexec and nagios_plugdir=/usr/lib/nagios/plugins.

* Thu May 11 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.21-alt1
- Removes echo "PermitRootLogin yes" >> /etc/openssh/sshd_config, login with key does not require it....
- Cleaned scripts.
- Removed unimplemented podsec-inotify scripts.

* Thu May 11 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.20-alt1
- Added waiting for socket from rootlesslit service to _kubeadm.sh.
- Debugged missing crio.sock.

* Thu May 11 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.19-alt1
- Restored list of images in podsec-k8s-save-oci.

* Thu May 11 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.18-alt1
- Added network setup.
- Added redirect /dev/stderr machinectl to /dev/null.

* Wed May 10 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.17-alt1
- Removed fuse-overlays from podsec-create-imagemakeruser, podsec-create-podmanusers.

* Wed May 10 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.16-alt1
- Changed permissions and owner for ~u7s-admin.
- Assigned user, group for .bashrc.
- Switched to 1.26.3-alt2 with group access to /etc/kubernetes.
- Added support for other kubeadm flags.
- Added allocating IP address and port for init apiServer.
- Added .bashrc.
- Addwd a separate YAML file for ControlPlane.
- Added JoinControlPlane.LocalAPIEndpoint.
- Added DNS to the algorithm for generating a static IP address (3).
- Replaced the etcd database directory with /var/lib/Etcd.
- Moved the etcd database to the standard location.
- Optimized code.

* Sun May 07 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.15-alt1
- Optimized systemctl@u7s code.
- Added the use of templates in systemd.

* Sun May 07 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.14-alt1
- Implemented first working version after moving all files out of ~u7s-admin.
- Fixed bugs.

* Thu May 04 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.13-alt1
- Addied .sh suffix for internal scripts.
- Merge common, boot, bin into bin.
- Removed .sh prefix, optimized.
- Moved config files to /etc/podsec/u7s.
- Removed unnecessary code, move user systemd services to /usr/lib/systemd/user.
- Added forward ports 53 (may need to be changed according to iptables kuber).
- Added providing access from cni0 interface of network 10.244.0.1/24 to external and internal announced addresses.
- Added raising addresses of TAP interfaces on external interface.
- Added providing launch of u7s services after sshd.service.

* Thu May 04 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.12-alt1
- Changed documentation.
- Fixed issues.
- Moved podsec-inotify-check-containers.service from .gear to /podsec-inotify/services/.

* Wed May 03 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.11-alt1
- Replaced symlinks with real scripts, fix remaining small problems with chmod, chown, chgrp.
- Replaced symlinks with real scripts, fix remaining small problems with chmod, chown, chgrp.
- Added forward ports 2379, 2380, 6443, 10250, 10255, 10256 out.

* Tue May 02 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.10-alt1
- Implemented switch to configuration composite configuration files init.yaml, join.yaml via "clean" ClusterConfigurationWithEtcd.yaml InitConfiguration.yaml JoinConfiguration.yaml KubeletConfiguration.yaml KubeProxyConfiguration.yaml.
- Provided allocation of static cluster addresses for tap0 interfaces from the range 10.96.0.0 - 10.96.155.254.
- Fixed a bug in join ControlPlane.
- Added documentation on adding a worker node.
- Added a debug level parameter.

* Mon May 01 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.9-alt1
- Add support connecting workers, starting flanneld as a container.
- Add support starting flanneld as a service.
- Add support starting flanneld as an image/pod.
- Provided support for kubeadm join for worker'а.
- Moved iptables settings from kubeadm to rootlesskit.
- Transferring directory creation to rootlesskit.
- Removed flanneld service, we will launch it via image/pod.
- Add support setting up kubeadm init mode.
- Connect etcd parameters for flanneld only for controlPlane=master.
- Set up a list of pending files depending on the deployment environment (controlPlane).
- Moved changing parameters controlPlane, caCertHash, token to ENV file, remove them from parameter transfers.
- Analyzed kubeadm join flags and pass them to binary kubeadm.
- Uses system group kube from kubernetes package.
- Switch to single script podsec-u7s-kubeadm.

* Fri Apr 28 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.8-alt1
- Switch to single script podsec-u7s-kubeadm.
- Merged podsec-u7s-node-init, podsec-u7s-node-join into one script podsec-u7s-kubeadm.
- Moved the password setting function to a separate script podsec-u7s-admin-passwd.
- Renamed the script podsec-u7s-create-node -> podsec-u7s-node-init.
- Created the script podsec-u7s-node-join and accompanying scripts in boot/ and /bin.

* Thu Apr 27 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.7-alt1
- Added support full deployment of the master node.
- Set access rights to /run/flannel.
- Set up the launch of system and --USER services.
- Added the function podsec-inotify-check-containers (thnx Nikolay Burykin).
- Modified services, removed unnecessary ones.

* Wed Apr 26 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.6-alt1
- Set up interaction between kube-apiserver and etcd.
- Moved certificates to the standard location /etc/kubernetes/pki.
- Added support full configuration of the etcd service as a POD.
- Set up kubeadm-configs/init.yaml.
- Added templates for kubeadm configuration files.
- Added etcd and flanneld services.
- Disabled services except kubelet and rootlesskit in the no-services branch.
- Switch to Clusternet 10.96.0.0/12.
- Added setting the tap0 IP address.
- Edited the link to crio.sock.

* Mon Apr 24 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.5-alt1
- Added the kubernetes group and editing the rights and group of the /etc/kubernetes, /etc/kubernetes/manifests/.
- Added support starting services after installation and reboot.

* Fri Apr 21 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.4-alt1
- First working version. kubeadm reaches the end, raises a full-fledged server.
- Copyied configuration files /etc/kubernetes/*.conf from namespace u7s-admin to the main file system.
- Fine-tuned configuration files.
- Removed fuse* packages, settings for fusemount in crio.

* Fri Apr 21 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.3-alt1
- Moved scripts out of podsec.spec.
- Moved directory /var/lib/etcd to ~u7s-admin/usernetes.
- Moved creation of /run to services.
- Removed bash'isms.
- Modev usernetes/Config -> config.
- Moved initialization from podsec.spec to podsec-k8s/bin/podsec-u7s-create-node.

* Thu Apr 20 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.2-alt1
- Edited podsec.spec attributes.

* Thu Apr 20 2023 Alexey Kostarev <kaf@altlinux.org> 0.9.1-alt1
- Renamed files and directories of the podsec-nagios-plugins package to files and directories of the podsec-inotify package.

* Thu Apr 20 2023 Alexey Kostarev <kaf@altlinux.org> 0.8.1-alt1
- Implemented first working version of deployment via kubeadm init.
- Switched kube-scheduler.sh to reading the command and parameters from the manifest.
- Removed dependencies on rootlesskit from the service, debugging has been added.
- Returned to boot/ with control uid. If uid>0 - call bin via nsenter.sh.
- Added usernetes/bin/_kubeadm.sh usernetes/bin/_kubelet.sh.

* Tue Apr 18 2023 Alexey Kostarev <kaf@altlinux.org> 0.7.6-alt1
- Renamed services, replaced boot/*.sh calls with bin/_*sh.

* Tue Apr 18 2023 Alexey Kostarev <kaf@altlinux.org> 0.7.5-alt1
- Renamed scripts in bin/*.sh to bin/_*.sh; systemctl waits for kubeadm to generate all manifests when starting the target service.

* Tue Apr 18 2023 Alexey Kostarev <kaf@altlinux.org> 0.7.4-alt1
- Fixed call format.
- Added debugging.

* Mon Apr 17 2023 Alexey Kostarev <kaf@altlinux.org> 0.7.3-alt1
- Added displaing call format.
- Fixed errors.

* Mon Apr 17 2023 Alexey Kostarev <kaf@altlinux.org> 0.7.2-alt1
- Moved running commands under nsenter from /boot/ to /bin/.
- Moved ~/bin/ to ~/usernetes/bin/.
- Fixed errors.

* Mon Apr 17 2023 Alexey Kostarev <kaf@altlinux.org> 0.7.1-alt1
- Started of transition to kubeadm.
- Writed commands from usernetes/Bin/ directory to bin/.
- Added execution permissions.
- Imported etcd, kube-api-server, kube-controller-manager startup parameters from /etc/kubernetes/manifests/*.yml, adjust certificate files in flanneld.sh, kubelet.sh.
- Added boot/kubeadm.sh script calling kubeadm in nsenter environment.

* Fri Apr 14 2023 Alexey Kostarev <kaf@altlinux.org> 0.6.1-alt1
- Adjusted for new kernel 5.15.105-un-def-alt1.
- Changed mount etc/sysconfig/ on RW --copy-up.
- Commented out messages about existence of groups.
- Added settings to podsec.spec.
- Added mkdir -p /etc/systemd/system/user@.service.d/.
- Downgraded flannel to 1.1.2.
- Removed all images from oci archive except coredns, podsec.
- Added description of current usernetes installation.
- Added password setting for u7s-admin.
- Generated and corrected the document Notes.md, CompareRootFullLess.md.
- Added authorization-mode=Node,RBAC.
- Generated and corrected the document Notes.md, CompareRootFullLess.md.
- Generated the document Notes.md.
- Added a document on how to configure kubeadm to work with rootless kuber (alt_usernetes).
- Added replacing /lib/systemd/system/kubelet.service to rootless kubelet.service.
- Added .config/systemd/user/ services.

* Sun Apr 09 2023 Alexey Kostarev <kaf@altlinux.org> 0.5.1-alt1
- Added attrs to spec.
- Added setting execution rights for *.sh.
- Removed binaries for rpm spec.
- Creating the user u7s-admin.
- Copyied usernetes to ~u7s-admin.
- Created the podsec-u7s-functions function, in which the commands for creating configuration files were moved to the createU7Environments function.
- Added alt_usernet to common development.

* Thu Apr 06 2023 Alexey Kostarev <kaf@altlinux.org> 0.4.1-alt1
- Added scripts for alt usernetes (rootless kubernetes).

* Wed Apr 05 2023 Alexey Kostarev <kaf@altlinux.org> 0.3.1-alt1
- Added podsec-k7s-create-node rootless kubernetes (alt_usernetes) to the spec file and Makefile, forming dependencies of kuber 1.26 packages.
- Added selecting an image by prefix and discarding it to avoid duplication (loadOci).
- Switched to kubernetes 1.26 images.
- Switched to crio to the new version of pause, moving crio configuration from k8s/install/createK8S.sh to createPolicy.
- Switched to saveK8SOci.sh on image version 1.26.
- Implemented podsec-nagios-plugins/bin/podsec-nagios-plugins-check-images.
- Added switching from sudo to running the podsec-nagios-plugins-check-policy plugin as root, supplementing the documentation on configuring the plugin call on the nagios server side.
- Eliminated sudo dependency.
- Added support for LANG=C.

* Tue Mar 28 2023 Alexey Kostarev <kaf@altlinux.org> 0.2.4-alt1
- Added support the registry path in loadAndSignOci.sh - itt should have the form registrar/path.
- Specifyied the path is mandatory.
- Added templates for new plugins.
- Corrected of the algorithm for generating the name of the temporary file.
- Added plugin templates for analyzing kubernetes.
- Added the podsec-nagios-plugins-create-nagiosuser script for creating a nagios user on the client.
- Added obtaining root rights via sudo.
- Changed the plugin placement path.
- Completed documentation for the podsec-nagios-plugins-check-policy plugin.
- Completed the initial version of podsec-nagios-plugins-check-policy.
- Completed mainly the first versions of the podsec podsec-k8s podsec-k8s-rbac packages.
- Fixed errors in loadAndSignOci.sh.
- Developed the main metrics of podsec-nagios-plugins-check-policy.
- Fixed the error of group formation when changing access rights to the .kube directory.
- Downgraded dependency versions to p10.
- Added functions to podsec-nagios-plugins/bin/podsec-nagios-plugins-functions and test script podsec-nagios-plugins/bin/podsec-nagios-plugins-functions-test.
- Added script podsec-nagios-plugins-create-nagiosuser to create nagios user on client.
- Added getting root rights via sudo.
- Changed plugin placement path.
- Completed documentation for podsec-nagios-plugins-check-policy.
- Completed initial version of podsec-nagios-plugins-check-policy.
- Added script templates for functions and checks in podsec-nagios-plugins, documentation for them, ....
- Configured Makefile podsec.spec to support functions in podsec-nagios-plugins/bin/podsec-nagios-plugins-functions.
- Added schemes of plugin interaction with nagios.
- Initial documentation for nagios plugins completed.
- Sudo dependency added for nagios-plugins package.

* Fri Mar 24 2023 Alexey Kostarev <kaf@altlinux.org> 0.2.3-alt1
- First versions of podsec podsec-k8s podsec-k8s-rbac packages mostly completed.
- Fixed BUGs in loadAndSignOci.sh.
- Developed core metrics podsec-nagios-plugins-check-policy.
- Fixed group formation error when changing access rights to .kube directory.

* Fri Mar 24 2023 Alexey Kostarev <kaf@altlinux.org> 0.2.2-alt1
- Decreased dependency versions to p10.
- Added features to podsec-nagios-plugins/bin/podsec-nagios-plugins-functions and test script podsec-nagios-plugins/bin/podsec-nagios-plugins-functions-test.
- Added script templates for functions and checks in podsec-nagios-plugins, documentation on them, ....
- Configured Makefile podsec.spec to support functions in podsec-nagios-plugins/bin/podsec-nagios-plugins-functions.
- Formatted initial version of documentation on nagios-plugins.
- Added sudo dependency for nagios-plugins package.
- Removed unformatted scripts.
- Added description of plugin call format, functionality, exit codes.
- Added podsec-nagios-plugins package to Makefile podsec.spec.
- Added function for working with nagios plugins: metricaInInterval() - Returns code 0 if metric falls within specified interval..
- Renamed script ImageSignatureVerification/checkImagesSignature.sh.
- Added author to documentation.
- Added dependencies wget and coreutils.
- Added new scripts to podsec/bin.

* Sun Mar 19 2023 Alexey Kostarev <kaf@altlinux.org> 0.2.1-alt1
- Finalized documentation the kubernetes API service audit setting.
- Modified Makefile, podsec.spec, removed references to unused scripts.
- Added documentation for the podsec-k8s-create-master script.
- Added documentation (in man. md format) for podsec-k8s-rbac-bindrole, podsec-k8s-rbac-create-remoteplace, podsec-k8s-rbac-get-userroles, podsec-k8s-rbac-unbindrole, modified documentation for podsec-k8s-rbac-create-kubeconfig, podsec-k8s-rbac-create-user.
- Added scripts podsec-k8s-rbac-bindrole, podsec-k8s-rbac-get-userroles, podsec-k8s-rbac-unbindrole, functions file podsec-k8s-rbac-functions, modified podsec-k8s-rbac-create-kubeconfig, podsec-k8s-rbac-create-user.
- Edited syntax of man files.
- Added commands, md- and man-files of the podsec-k8s-rbac package.

* Fri Mar 17 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.6-alt1
- Added man for podsec-k8s-create-master.
- Added manifest kube-flannel.yml.
- Added scripts podsec-k8s-save-oci, podsec-save-oci, man pages formatted, scripts modified - added checks that they are launched in the right order and on the right nodes.

* Thu Mar 16 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.5-alt1
- Changed the format of the list of imagemaker users - user@regPath.
- Added the ability to create multiple imagemaker class users.

* Thu Mar 16 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.4-alt1
- Removed /etc/kubernetes from Required, debug createImageMakerUser.sh.

* Thu Mar 16 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.3-alt1
- Addwd man pages.
- Created podsec-create-policy.md.

* Thu Mar 16 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.2-alt1
- Changed directory structure: podmanbin -> podsec/bin, k8sbin -> podsec-k8s/bin.

* Wed Mar 15 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.1-alt1
- Added Required to podsec, podsec-k8s.
- Added username parameters to createImageMakerUser.sh, remove apt-get install and checking list installes packages from createPolicy.sh.
- Tuned Makefile, podsec.spec.
- Added changelog.
- Added gear files.
- Splitted bin to podmanbin, k8sbin.
- Added bin/podsec-* links.
- Removed package installation, added check for installed....
- Moved archiveImages to k8s.
- Added skopeo and sigstore: to imagemaker.
- Added loadAndSignOci.sh.
- Added install skopeo.
- Added createK8S.sh and kube-flannel.yml.
- Created README.md.
- Moved RBAC to k8s.
- Moved RBAC repository.
- Added use of pause image for podman 4.4.2.
- Added shadow-submap package.
- Added podman package.
- Added adding groups to createPolicy.sh.
- Added entry into fuse group.
- Moved package installation to createPolicy.sh, chattr -i made recursive on all files in the directory.
- Disabled http2 service.
- Separated service createServices.sh from createPodmanUsers.
- Added commands for correct configuration of rootless mode.
- Changes to 'trivy/tests/k8s/namespace'.
- Added trivy examples.
- Added createPolicy.sh.
- Universalized saveOci.sh script.
- Implemented new version of loadOci.sh.
- Written the basis of the monitorPoliciesAndImages.sh script.
- Added scripts for archiving and unarchiving (kubetnetes) images.
- Added support for loading YAML files into /etc/containers/registries.d/.
- Checking config files in local user directories.
- Added noDefaultSigStore field support.
- Added support signed and notSigned images.
- Tuned checkImagesSignature.sh - JSON output.
- Added checkImagesSignature.sh.
- Created registry/Dockerfile.
