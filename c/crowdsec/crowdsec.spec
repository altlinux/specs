%global _unpackaged_files_terminate_build 1
%global import_path github.com/crowdsecurity/crowdsec
# git rev-parse --short v%version
%global commit_hash 027974f
%global _libexecdir %_prefix/libexec
%global cmd_path .gopath/src/%import_path/cmd

Name: crowdsec
Version: 1.7.7
Release: alt2
Summary: Security solution offering crowdsourced protection against malicious IPs
License: MIT
Group: System/Servers
Url: https://www.crowdsec.net
VCS: https://github.com/crowdsecurity/crowdsec

Source: %name-%version.tar
Source1: vendor.tar
Patch: alt-fix-build-vendor-cre2.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: gcc-c++
BuildRequires: libre2-devel

%description
CrowdSec - the open-source and participative security solution
offering crowdsourced protection against malicious IPs and
access to the most advanced real-world CTI.

%prep
# go mod vendor
# git add vendor -f && git commit -m "Updated go vendor modules."
%setup -a 1
%patch -p1

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
export BUILD_VERSION=v%version
export BUILD_TAG=%commit_hash
export DEBUG=1
%golang_prepare
cd .gopath/src/%import_path
%make_build
./cmd/%name-cli/cscli completion bash > cmd/cscli.bash
./cmd/%name-cli/cscli completion zsh > cmd/cscli.fish
./cmd/%name-cli/cscli completion fish > cmd/_cscli
cd -
sed -i 's/Environment=/Environment=GIN_MODE=release /' debian/%name.service

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_unitdir \
         %buildroot%_logdir/%name \
         %buildroot%_libexecdir/%name/plugins \
         %buildroot%_localstatedir/%name \
         %buildroot%_sysconfdir/%name/hub \
         %buildroot%_sysconfdir/%name/patterns \
         %buildroot%_sysconfdir/%name/notifications \
         %buildroot%_sysconfdir/cron.daily \
         %buildroot%_datadir/bash-completion/completions \
         %buildroot%_datadir/zsh/site-functions \
         %buildroot%_datadir/fish/vendor_completions.d
install -m 0755 %cmd_path/%name/%name %buildroot%_bindir
install -m 0755 %cmd_path/%name-cli/cscli %buildroot%_bindir
install -m 0644 %cmd_path/cscli.bash %buildroot%_datadir/bash-completion/completions
install -m 0644 %cmd_path/cscli.fish %buildroot%_datadir/fish/vendor_completions.d
install -m 0644 %cmd_path/_cscli %buildroot%_datadir/zsh/site-functions
install -m 0644 debian/%name.service %buildroot%_unitdir
install -m 0644 debian/%name-hubupdate.service %buildroot%_unitdir
install -m 0644 debian/%name-hubupdate.timer %buildroot%_unitdir
install -m 0755 debian/hubupdate.sh %buildroot%_libexecdir/%name
install -m 0644 config/acquis.yaml %buildroot%_sysconfdir/%name
install -m 0644 config/config.yaml %buildroot%_sysconfdir/%name
install -m 0644 config/console.yaml %buildroot%_sysconfdir/%name
install -m 0644 config/context.yaml %buildroot%_sysconfdir/%name
install -m 0644 config/detect.yaml %buildroot%_sysconfdir/%name
install -m 0644 config/local_api_credentials.yaml %buildroot%_sysconfdir/%name
install -m 0644 config/online_api_credentials.yaml %buildroot%_sysconfdir/%name
install -m 0644 config/profiles.yaml %buildroot%_sysconfdir/%name
install -m 0644 config/simulation.yaml %buildroot%_sysconfdir/%name
install -m 0644 config/patterns/* %buildroot%_sysconfdir/%name/patterns
find %cmd_path/notification-* \
    -type f \
    -executable \
    -exec install -m 0755 {} %buildroot%_libexecdir/%name/plugins \;
find %cmd_path/notification-* \
    -type f \
    -name "*.yaml" \
    -exec install -m 0644 {} %buildroot%_sysconfdir/%name/notifications \;
sed -i -e "s|/usr/local/lib|%_libexecdir|g" \
       -e "/log_dir/s|/var/log/$|%_logdir/%name|" %buildroot%_sysconfdir/%name/config.yaml
echo "{}" > %buildroot%_sysconfdir/%name/hub/.index.json

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/cscli
%_bindir/%name
%_logdir/%name
%_localstatedir/%name
%_unitdir/%name.service
%_unitdir/%name-hubupdate.timer
%_unitdir/%name-hubupdate.service
%_sysconfdir/%name/patterns
%_libexecdir/%name/hubupdate.sh
%_libexecdir/%name/plugins/notification-dummy
%_libexecdir/%name/plugins/notification-email
%_libexecdir/%name/plugins/notification-file
%_libexecdir/%name/plugins/notification-http
%_libexecdir/%name/plugins/notification-sentinel
%_libexecdir/%name/plugins/notification-slack
%_libexecdir/%name/plugins/notification-splunk
%config(noreplace) %_sysconfdir/%name/acquis.yaml
%config(noreplace) %_sysconfdir/%name/config.yaml
%config(noreplace) %_sysconfdir/%name/console.yaml
%config(noreplace) %_sysconfdir/%name/context.yaml
%config(noreplace) %_sysconfdir/%name/detect.yaml
%config(noreplace) %_sysconfdir/%name/local_api_credentials.yaml
%config(noreplace) %_sysconfdir/%name/online_api_credentials.yaml
%config(noreplace) %_sysconfdir/%name/profiles.yaml
%config(noreplace) %_sysconfdir/%name/simulation.yaml
%config(noreplace) %_sysconfdir/%name/hub/.index.json
%config(noreplace) %_sysconfdir/%name/notifications/dummy.yaml
%config(noreplace) %_sysconfdir/%name/notifications/email.yaml
%config(noreplace) %_sysconfdir/%name/notifications/file.yaml
%config(noreplace) %_sysconfdir/%name/notifications/http.yaml
%config(noreplace) %_sysconfdir/%name/notifications/sentinel.yaml
%config(noreplace) %_sysconfdir/%name/notifications/slack.yaml
%config(noreplace) %_sysconfdir/%name/notifications/splunk.yaml
%_datadir/bash-completion/completions/cscli.bash
%_datadir/zsh/site-functions/_cscli
%_datadir/fish/vendor_completions.d/cscli.fish
%dir %_libexecdir/%name
%dir %_libexecdir/%name/plugins
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/hub
%dir %_sysconfdir/%name/notifications
%doc LICENSE

%changelog
* Sat Jun 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.7.7-alt2
- FTBFS fixed.

* Wed Apr 15 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 1.7.7-alt1
- Updated to version 1.7.7.

* Sun Mar 29 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.7.6-alt1
- Updated to version 1.7.6.

* Fri Dec 05 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.7.4-alt1
- Updated to version 1.7.4.

* Sun Nov 02 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.7.3-alt1
- Updated to version 1.7.3.

* Sun Sep 28 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.7.0-alt1
- Updated to version 1.7.0.

* Fri Apr 25 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.6.8-alt1
- Updated to version 1.6.8.

* Thu Dec 05 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.6.4-alt1
- Initial build for ALT.
