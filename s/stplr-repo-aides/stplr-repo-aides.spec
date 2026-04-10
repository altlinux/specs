%define rname aides

Name: stplr-repo-%rname
Version: 0.2.0
Release: alt1

Summary: Aides repository for stplr
License: ALT-Public-Domain
Group: System/Configuration/Other
Url: https://aides.space/

Source0: aides.toml

Requires: stplr >= 0.1.0

BuildArch: noarch

%description
%summary.

%install
install -D -m 0644 %SOURCE0 %buildroot%_target_libdir_noarch/stplr/repos.d/%rname.toml

%files
%_target_libdir_noarch/stplr/repos.d/%rname.toml

%changelog
* Mon Apr 06 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.2.0-alt1
- Migrate to new repo schema.

* Wed Feb 18 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.1.0-alt2
- Sync repo config with upstream.
- Add Requires(post,postun): stplr to guarantee stplr is installed before %%post and 
  removed after %%postun scripts run (closes #57933).

* Tue Feb 03 2026 Semen Fomchenkov <armatik@altlinux.org> 0.1.0-alt1
- Initial build.
