%define _altdata_dir %_datadir/alterator

Name: alterator-etcgit
Version: 1.1
Release: alt17

BuildArch: noarch

Source:%name-%version.tar

Summary: Alterator module to control versions of configuration files in /etc using git
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.22-alt2
Requires: alterator-fbi >= 5.27-alt1
Requires: git-server
Conflicts: alterator >= 5.0
Conflicts: alterator-fbi >= 6.0

BuildPreReq: alterator rpm-macros-fillup rpm-macros-alterator

%description
Alterator module to control versions of configuration files in /etc
using git.

%package -n etcgit
Summary: A tool to control versions of configuration files in /etc using git
License: GPL
Group: System/Configuration/Other

%description -n etcgit
A tool to control versions of configuration files in /etc using git.
Currently is used by the "etcgit" Alterator module.

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/etcgit
%_alterator_backend3dir/etcgit
%_alterator_datadir/design

%files -n etcgit
%_bindir/*
%_sbindir/*
%_sysconfdir/etckeeper/*/*

%changelog
* Thu Oct 25 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt17
- Use the X-Alterator-VCS category.

* Sun Sep 16 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt16
- Fix: do not try to fetch profile if no URL is given.
- Interpret #f as the null URL.
- Fix: do not output local only branches in red.
- Fix: do not require the current repo URL to be valid on the
  page load.

* Thu Sep 13 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt15
- Add update, add and publish scripts for etckeeper.
- Improve the remote repo handling.

* Fri Sep 07 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt14
- Always list the local branches and thier publication status.
- Do not try to calculate inter-service dependencies (buggy).
- Restart the service when its runlevel settings changes.
- Fix more: pass on the list-modified parameters.
- Fix: try to filter out all non-service /etc/init.d files.
- Fix forced branch publication.
- Fix: commit changes using base and new branch parameter pair.
- Fix error handling in the filter checkout/setup procs.
- Fix: use `git ls-tree` instead of `git ls-files`.

* Thu Sep 06 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt13
- Check/ignore some errors during file checkouts.

* Thu Sep 06 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt12
- Add the 'checkout-meta' command for initial extract of the
  auxiliary and metadata files.

* Thu Sep 06 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt11
- Clean untracked not ignored files after the checkout.

* Wed Sep 05 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt10
- Fetch the remote branch before head comparison.

* Wed Sep 05 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt9
- Update/improve the independent service list.
- Never select the 'alteratord' for restart by file.
- Fix the async branch reload.

* Tue Sep 04 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt8
- Fix the head/branch parameter passing (affects 'etcgit fetch').

* Mon Sep 03 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt7
- Extract the `etcgit` tool to the subpackage.

* Fri Aug 31 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt6
- Use X-Alterator-Monitoring-Control category.

* Wed Aug 29 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt5
- Do not walk-up the paths to .gitignore and the other auxiliary
  files. Thus, do not restart extra services by accident.

* Tue Aug 28 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt4
- Implement asynchronous 'switch' command.

* Fri Aug 24 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt3
- Output the last (HEAD) commit message on plain `etcgit` call.
- Fix undefined "in_head" parameter (functions).

* Thu Aug 23 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt2
- Fix/update readonly operations of the etcgit tool.

* Wed Aug 22 2012 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Refactor the module for working with the local repo copy.

* Fri Jul 20 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial draft release.
