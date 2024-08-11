%global import_path github.com/gitlab-org/gitlab-runner
%define config_dir gitlab-runner.d

Name:    gitlab-runner
Version: 16.11.3 
Release: alt1

Summary: GitLab Runner is the open source project that is used to run your CI/CD jobs and send the results back to GitLab
License: MIT
Group:   Development/Tools
Url:     https://gitlab.com/gitlab-org/gitlab-runner

Source: %name-%version.tar
Source1: %name.service
Source2: %name.init
Source3: %name.tmpfiles
Source4: %name.sysconfig
Patch0: %name-16.9.1-alt-fix-for-su-command.patch
Patch1: vendored-cilium-ebpf-alt-loongarch64-support.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
install -pDm644 %SOURCE1 %buildroot%_unitdir/%name.service
install -pDm755 %SOURCE2 %buildroot%_initdir/%name
install -pDm644 %SOURCE3 %buildroot%_tmpfilesdir/%name.conf
install -pDm640 %SOURCE4 %buildroot%_sysconfdir/sysconfig/%name
install -pDm644 ./config.toml.example %buildroot%_sysconfdir/%config_dir/config.toml
install -dm775 %buildroot%_localstatedir/%name

%pre
if [ $1 == 1 ]; then
#Add the "gitlab-runner" user
	%_sbindir/groupadd -r -f gitlab-runner 2>/dev/null ||:
	%_sbindir/useradd  -r -g gitlab-runner -c 'Gitlab-runner daemon' \
		-s /dev/null -M -d %_localstatedir/gitlab-runner gitlab-runner 2>/dev/null ||:
fi

%files
%doc *.md
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%_sysconfdir/sysconfig/%name
%_tmpfilesdir/%name.conf
%attr(0770,root,gitlab-runner) %dir %_sysconfdir/%config_dir
%config(noreplace) %_sysconfdir/%config_dir/config.toml
%attr(0770,root,gitlab-runner) %dir %_localstatedir/gitlab-runner

%changelog
* Sun Aug 11 2024 Nikolay Burykin <bne@altlinux.org> 16.11.3-alt1
- New version 16.11.3

* Sun Mar 24 2024 Ivan A. Melnikov <iv@altlinux.org> 16.9.1-alt1.1
- NMU: fix FTBFS on loongarch64

* Wed Mar 20 2024 Nikolay Burykin <bne@altlinux.org> 16.9.1-alt1
- New version 16.9.1
- Fix:
  + "/root/.bash_profile: Permission denied" when use shell as an executor (ALT #47620)
  + failure prepare environment step, when use Docker as an executor (ALT #47621)

* Mon Aug 28 2023 Nikolay Burykin <bne@altlinux.org> 16.1.1-alt2
- Changed group from Other to Development/Tools

* Fri Aug 11 2023 Nikolay Burykin <bne@altlinux.org> 16.1.1-alt1
- Initial build for Sisyphus
