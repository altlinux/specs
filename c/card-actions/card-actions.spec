Name: card-actions
Version: 1.10
Release: alt7

Summary: Smart card action handler scripts
License: GPLv3+
Group: Monitoring

Source0: card-inserted-default
Source1: card-removed-default
Source2: card-actions-default.alternatives

Source3: card-inserted-terminate
Source4: card-removed-terminate
Source5: card-actions-terminate.alternatives

Source100: card-actions.control

BuildArch: noarch

Requires: pam_pkcs11 >= 0.6.9-alt23

%description
%summary

%install
install -pDm755 %SOURCE0 %buildroot%_bindir/card-inserted-default
install -pDm755 %SOURCE1 %buildroot%_bindir/card-removed-default
install -pDm644 %SOURCE2 %buildroot%_altdir/card-actions-default

install -pDm755 %SOURCE3 %buildroot%_bindir/card-inserted-terminate
install -pDm755 %SOURCE4 %buildroot%_bindir/card-removed-terminate
install -pDm644 %SOURCE5 %buildroot%_altdir/card-actions-terminate

install -pDm755 %SOURCE100 %buildroot%_controldir/card-actions

sed -i -e 's,/usr/bin,%_bindir,g' \
    %buildroot%_bindir/card-inserted-terminate \
    %buildroot%_bindir/card-removed-terminate \
    %buildroot%_controldir/card-actions

%files
%_bindir/*
%_altdir/*
%_controldir/*

%changelog
* Fri Nov 03 2017 Paul Wolneykien <manowar@altlinux.org> 1.10-alt7
- Fixed "terminate" profile.
- Skip card identification on insert in the "terminate" mode.

* Thu Nov 02 2017 Paul Wolneykien <manowar@altlinux.org> 1.10-alt6
- Add the alternative remove handler that terminates a user
  session.
- Add the "card-actions" control to select it.

* Tue Oct 31 2017 Paul Wolneykien <manowar@altlinux.org> 1.10-alt5
- Fix: Need to query the card in order to have a chance to swith
  to the existing session.

* Tue Oct 31 2017 Paul Wolneykien <manowar@altlinux.org> 1.10-alt4
- If a default user name is configured then use it instead of
  querying the card when the latter is inserted.
- Use "pam_pkcs11_query_config" to get the default user name when
  the card is removed.

* Mon Oct 30 2017 Paul Wolneykien <manowar@altlinux.org> 1.10-alt3
- Fixed state query: catch the error output.

* Thu Oct 26 2017 Paul Wolneykien <manowar@altlinux.org> 1.10-alt2
- To be improved: explicitly pass 'nobody' to the DM.

* Tue Oct 24 2017 Paul Wolneykien <manowar@altlinux.org> 1.10-alt1
- Allow to pass username on the command line (card-inserted-default).

* Fri Oct 20 2017 Paul Wolneykien <manowar@altlinux.org> 1.9-alt1
- Reset the greeter when a token is removed.

* Tue Aug 08 2017 Paul Wolneykien <manowar@altlinux.org> 1.8-alt4
- Rebuild with separated "dm-tool" package.

* Wed Jul 12 2017 Paul Wolneykien <manowar@altlinux.org> 1.8-alt3
- Try to switch even if the username is unknown yet.

* Fri Jun 09 2017 Paul Wolneykien <manowar@altlinux.org> 1.8-alt2
- Moved the event manager service to the pam_pkcs11 package.
- Start a new session if the user isn\'t known to loginctl.

* Tue Jun 06 2017 Paul Wolneykien <manowar@altlinux.org> 1.8-alt1
- Use pklogin_finder to get the username of the currently inserted token.
- Use loginctl to activete an existing session.
- Systemd-only event-manager service.
- Make /usr/bin/card-inserted and /usr/bin/card-removed an alternative
  (for use with pkcs11-events control).

* Fri Feb 10 2017 Andrey Cherepanov <cas@altlinux.org> 1.7-alt1
- Initial build in Sisyphus

* Mon Nov 14 2016 Andrey Cherepanov <cas@altlinux.org> 1.7-alt0.M70C.1
- rewrite to use loginctl and dm-tool

* Fri Oct 05 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6-alt1
- add homedir removing on different user login

* Wed Oct 03 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5-alt1
- remove /var/lib/smartcard/user on shutdown and startup

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 1.4-alt1
- card_*: minor tweaks/fixups

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- card_*: slightly better logging

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 1.2-alt1
- essentially rewrote scripts
  + card_insert:
    - get rid of extra gnome-panel dependency
    - a few hundred microsecond sleeps were clearly a thinko here
- added initscript instead of rc.local hack (no migration though)
- spec cleanup

* Tue Jan 31 2012 Michail Yakushin <silicium@altlinux.ru> 1.1-alt1
- fix card_insert script. kill all user process after session termination

* Thu Nov 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1
- initial
