%global import_path github.com/gitlab-org/gitlab-runner
%define config_dir gitlab-runner.d

Name:    gitlab-runner
Version: 19.1.0
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

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup
%autopatch -p1

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
install -pDm644 ./config.toml.example %buildroot%_sysconfdir/%name/config.toml
install -dm775 %buildroot%_localstatedir/%name

%pre
if [ $1 -eq 1 ]; then
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
%attr(0770,root,gitlab-runner) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.toml
%attr(0770,root,gitlab-runner) %dir %_localstatedir/gitlab-runner

%changelog
* Thu Jun 18 2026 Andrew A. Vasilyev <andy@altlinux.org> 19.1.0-alt1
- New version 19.1.0

* Wed Jun 03 2026 Andrew A. Vasilyev <andy@altlinux.org> 19.0.1-alt1
- New version 19.0.1

* Tue May 26 2026 Andrew A. Vasilyev <andy@altlinux.org> 19.0.0-alt1
- New version 19.0.0

* Tue May 12 2026 Andrew A. Vasilyev <andy@altlinux.org> 18.11.3-alt1
- New version 18.11.3

* Tue May 05 2026 Andrew A. Vasilyev <andy@altlinux.org> 18.11.2-alt1
- New version 18.11.2

* Tue Apr 21 2026 Andrew A. Vasilyev <andy@altlinux.org> 18.11.1-alt1
- New version 18.11.1

* Tue Apr 07 2026 Andrew A. Vasilyev <andy@altlinux.org> 18.10.1-alt1
- New version 18.10.1
- Mentioned vulnerabilities (fixes: CVE-2025-22868, CVE-2025-46334,
  CVE-2025-46334, CVE-2025-47907, CVE-2025-48384, CVE-2025-48384,
  CVE-2025-48385, CVE-2025-48385)

* Fri Mar 20 2026 Andrew A. Vasilyev <andy@altlinux.org> 18.10.0-alt1
- New version 18.10.0

* Tue Feb 24 2026 Andrew A. Vasilyev <andy@altlinux.org> 18.9.0-alt1
- New version 18.9.0

* Tue Jan 20 2026 Andrew A. Vasilyev <andy@altlinux.org> 18.8.0-alt1
- New version 18.8.0

* Tue Jan 13 2026 Andrew A. Vasilyev <andy@altlinux.org> 18.7.2-alt1
- New version 18.7.2

* Thu Dec 25 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.7.1-alt1
- New version 18.7.1

* Mon Dec 22 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.7.0-alt1
- New version 18.7.0

* Wed Dec 17 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.6.6-alt1
- New version 18.6.6

* Wed Nov 26 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.6.2-alt1
- New version 18.6.2

* Mon Oct 20 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.5.0-alt1
- New version 18.5.0

* Tue Sep 09 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.3.1-alt1
- New version 18.3.1

* Wed Aug 27 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.3.0-alt1
- New version 18.3.0

* Mon Jul 28 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.2.1-alt1
- New version 18.2.1

* Tue Jul 01 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.1.1-alt1
- New version 18.1.1

* Fri Jun 20 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.1.0-alt1
- New version 18.1.0

* Wed Jun 18 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.0.3-alt1
- New version 18.0.3

* Mon May 26 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.0.2-alt1
- New version 18.0.2

* Tue May 20 2025 Andrew A. Vasilyev <andy@altlinux.org> 18.0.1-alt1
- New version 18.0.1

* Tue May 06 2025 Andrew A. Vasilyev <andy@altlinux.org> 17.11.1-alt1
- New version 17.11.1

* Fri Apr 18 2025 Andrew A. Vasilyev <andy@altlinux.org> 17.11.0-alt1
- New version 17.11.0

* Thu Apr 03 2025 Andrew A. Vasilyev <andy@altlinux.org> 17.10.1-alt1
- New version 17.10.1

* Tue Mar 25 2025 Andrew A. Vasilyev <andy@altlinux.org> 17.10.0-alt1
- New version 17.10.0

* Wed Mar 12 2025 Andrew A. Vasilyev <andy@altlinux.org> 17.9.1-alt1
- New version 17.9.1

* Tue Mar 04 2025 Andrew A. Vasilyev <andy@altlinux.org> 17.9.0-alt1
- New version 17.9.0

* Mon Feb 03 2025 Andrew A. Vasilyev <andy@altlinux.org> 17.8.3-alt1
- New version 17.8.3

* Thu Jan 30 2025 Andrew A. Vasilyev <andy@altlinux.org> 17.8.0-alt1
- New version 17.8.0

* Wed Jan 29 2025 Andrew A. Vasilyev <andy@altlinux.org> 16.11.3-alt2
- Fix:
  + condition in %%pre to create new user/group on install
  + change config directory

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
