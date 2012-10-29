%define _altdata_dir %_datadir/alterator

Name: alterator-mastercontrol
Version: 1.0
Release: alt11

BuildArch: noarch

Source:%name-%version.tar

Summary: Alterator module to control configuration profiles on the remote hosts
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.22-alt2
Requires: alterator-fbi >= 5.27-alt1
Conflicts: alterator >= 5.0
Conflicts: alterator-fbi >= 6.0

BuildPreReq: alterator rpm-macros-fillup rpm-macros-alterator

%description
Alterator module to control configuration profiles on the remote hosts.

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/mastercontrol
%_alterator_backend3dir/mastercontrol
%_alterator_datadir/design
%_bindir/*

%changelog
* Thu Oct 25 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt11
- Use the X-Alterator-VCS category.

* Thu Sep 20 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt10
- Filter for the 'A - B' IP ranges.

* Thu Sep 13 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt9
- Fix the unknown (unsuccess) counter value calculation.
- Fix: do not dispatch if the passphrase input was cancelled.
- Clear the password field on dialog dismiss.
- Fix the hardcoded text in Russian.
- Set the 'UNKNOWN' status for etcgit values not matching the pattern.

* Thu Sep 06 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt8
- Do not output an Alterator error message for each failed SQL
  command.

* Wed Sep 05 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt7
- Update the next ID for hostmacro on macro update/insert.

* Fri Aug 31 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt6
- Use X-Alterator-Monitoring-Control category.

* Thu Aug 30 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt5
- Output the link to the control panel (ahttpd) for each host.

* Thu Aug 30 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Install the custom CSS.

* Wed Aug 29 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Localize host status on the /viewparams page.
- Fix MySQL default connection charset (UTF-8).
- Fix inserting/updating the profile head macro: start IDs from 1.
- Fix etcgit item name in the changelog.

* Tue Aug 28 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Update the etcgit host macro on profile switch.
- Output the expected hash code in the status field.
- Send `etcgit switch` command. Write the log.
- SSH key management.
- Add the dispatcher.
- Shrink strings for 16 chars in the min/avg/max output.
- Expand escaped characters in the min/avg/max output.
- Add space before "Advanced search" area.
- Functions: read values with `read -r`.
- Remove the "Manage repositories..." link.
- Use one (plain) etcgit item for both commit data (hash, message)
  and the profile name.
- Select and output the last etcgit commit info for each host.
- Use ETCGIT_HEAD as profile macro name, system.run[sudo etcgit] as
  current profile item key.

* Fri Jul 20 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial draft release.
