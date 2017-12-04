%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%define _basename lightdm-gtk-greeter

Name: lightdm-gtk-greeter-pd
Epoch: 1
Version: 2.0.1.5
Release: alt1
Summary: LightDM GTK+ Greeter (prompt-driven)
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/lightdm-gtk-greeter
#To get source code use the command "bzr branch lp:lightdm-gtk-greeter"
Source: %_basename-%version.tar
Patch1: %_basename-2.0.1-alt-fixes.patch
Patch2: %_basename-%version-advanced.patch

Requires: lightdm >= 1.16.7-alt11
Requires: gnome-icon-theme gnome-icon-theme-symbolic gnome-themes-standard
Requires: /usr/share/design/current

Provides: lightdm-greeter lightdm-gtk-greeter
Conflicts: lightdm-gtk-greeter

BuildRequires: gcc-c++ intltool gnome-common gobject-introspection-devel
BuildRequires: glib2-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gmodule-export-2.0)
BuildRequires: pkgconfig(liblightdm-gobject-1) >= 1.3.5
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libxklavier)
BuildRequires: lightdm-devel >= 1.16.7-alt11 lightdm-gir-devel >= 1.16.7-alt11
BuildRequires: /usr/bin/exo-csource

%description
This package provides a GTK+-based LightDM greeter engine. In contrast
to the conventional "lightdm-gtk-greeter" package this version is
directly controlled by PAM prompts and messages.

%prep
%setup -n %_basename-%version
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure \
	%{subst_enable introspection} \
	--disable-static \
	--disable-libindicator \
	--disable-indicator-services-command \
	--enable-at-spi-command="/usr/libexec/at-spi-bus-launcher --launch-immediately" \
	--with-libxklavier \
	--enable-maintainer-mode \
	--libexecdir=%_libexecdir

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %_basename

cd %buildroot
# Add alternatives for xgreeters
mkdir -p ./%_altdir
printf '%_datadir/xgreeters/lightdm-default-greeter.desktop\t%_datadir/xgreeters/lightdm-gtk-greeter.desktop\t100\n' >./%_altdir/lightdm-gtk-greeter

%files -f %_basename.lang
%_altdir/lightdm-gtk-greeter
%_sbindir/lightdm-gtk-greeter
%_datadir/xgreeters/lightdm-gtk-greeter.desktop
%_datadir/doc/lightdm-gtk-greeter/sample-lightdm-gtk-greeter.css
%_datadir/icons/hicolor/scalable/places/*.svg
%config(noreplace) %_sysconfdir/lightdm/lightdm-gtk-greeter.conf

%changelog
* Fri Nov 17 2017 Paul Wolneykien <manowar@altlinux.org> 1:2.0.1.5-alt1
- A better layout for error messages.

* Wed Nov 15 2017 Paul Wolneykien <manowar@altlinux.org> 1:2.0.1.4-alt1
- Load CSS from file ("css-path" config. option).

* Tue Nov 14 2017 Paul Wolneykien <manowar@altlinux.org> 1:2.0.1.3-alt1
- Added to the bottom margin of the buttons.
- Support Pnago markup for error messages.

* Fri Nov 10 2017 Paul Wolneykien <manowar@altlinux.org> 1:2.0.1.2-alt1
- Reset change password enable flag when all errors are cleared.
- Fix: Show change password buttton when prompted regardless of
  message patterns.
- Compare password change patterns to messages as prefix patterns.
- Fix: Enable the change password button when prompted.

* Thu Nov 09 2017 Paul Wolneykien <manowar@altlinux.org> 1:2.0.1.1-alt1
- Start the password change session with password reset hint when
  is activated by the double click or the keyboard shortcut.

* Thu Nov 09 2017 Paul Wolneykien <manowar@altlinux.org> 1:2.0.1.0-alt1
- Switch the epoch: 1 and four part version numbering.
- Fix: Always allow to activate the password change by the button.
- Fix: Enable the visible password change button by default.
- Automatically start new authentication session when the password
  is successfully changed.
- Fix/improve: Don\'t hide the last error message (it is shown
  again on auth start anyway).
- Fix: Don\'t show the change password button if there is no
  authentication in progress.
- Fix/Improve: Leave the password change mode on cancel only,
  don\'t leave on error.

* Wed Nov 01 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt5
- Make the login and cancel button labels configurable.
- Use CSS to style the prompt and error messages.
- Activate the change password function by the double click on
  certain configurable error messages.
- Activate the change password function by a configurable accelerator
  key.

* Mon Oct 30 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt4
- Calculate the 'advanced' diff locally.
- Read the patches/advanced tree into the master branch.

* Wed Oct 25 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt3
- Fixed missing GtkBox object IDs.

* Tue Oct 24 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt2
- Clear PAM errors on reset() or when a new username is selected
  from the list.
- Show change pass button unconditionally when no trigger messages
  are configured. Add the option to hide it when there is no prompt
  shown.
- Conditional change pass (PIN) button.

* Mon Oct 23 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt1
- A prompt-driven greeter.
- New dialog the layout!
- Require lightdm >= 1.16.7-alt11.
- Hide the last error until prompted or the session is finished.
- Don\'t duplicate error messages. Leave only the last error message
  if there were no prompts in the session.
- Add options to hide login and cancel buttons when there are
  no prompts.
- Introduce 'restart-on-cancel' param: automatically restart the
  auth. session after cancel when it is true.
- Reset to the default info message on session start.
- Use configurable default info text.
- Clear error when the auth. session is started by the button.
- Control the output of implicit error messages with the config param.
- Clear errors and prompts when an auth. session completes due to its
  cancellation.
- Append the error messages until user responds.
- Hide cancel button when authentication completes.
- Hide the error message initially.
- Hide the error message on respond.

* Fri Sep 08 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt9
- Fixed switch-to-user with newly created greeter.

* Wed Jul 12 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt8
- Fix/improve: Start the session with the named user when switching.

* Thu Jun 22 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt7
- Fix: Don\'t claim the greeter as resettable leaving the "reset"
  callback registered.

* Tue Jun 20 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt6
- Make the greeter resettable. On reset, select the provided username
  and start authentication.
- Trying to workaround the weird bug in GTK+3 #710888 related to
  the info_bar.
- Workaround possible race with message label cleanup.
- Hide the message label when it is NULL or empty.

* Mon Feb 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt5
- fixed showing messages after empty message showing

* Mon Feb 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt4
- fixed showing message about failed login(closes: #33148)

* Fri Feb 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt3
- memory leak fixed

* Fri Feb 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt2
- Show multiple PAM messages to user (closes: #33116)

* Thu Mar 03 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed May 13 2015 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Fri Sep 19 2014 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri Mar 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Wed Apr 10 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Wed Jan 30 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- enable show-language-selector
- define logo, background, icon-theme-name

* Mon Oct 15 2012 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Wed Mar 07 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1
- 1.1.4
- initial package
