Name: x11-ssh-askpass
Version: 1.2.4.1
Release: alt4
Serial: 1

Summary: An X11-based passphrase dialog for use with OpenSSH
License: BSD-like
Group: Networking/Remote access
Url: http://www.jmknoble.net/software/%name
Packager: Dmitry V. Levin <ldv@altlinux.org>

# %url/%name-%version.tar.gz
Source: %name-%version.tar

%define openssh_askpass_dir %_libexecdir/openssh

PreReq: alternatives >= 0:0.4, %openssh_askpass_dir
Provides: %openssh_askpass_dir/ssh-askpass
Requires: openssh-askpass-common
Provides: openssh-askpass-x11 = %serial:%version-%release
Obsoletes: openssh-askpass-x11

# Automatically added by buildreq on Fri Dec 26 2008
BuildRequires: gccmakedep imake libXt-devel xorg-cf-files

%description
This is an X11-based passphrase dialog for use with OpenSSH.
These dialogs are intended to be called from the ssh-add program and
not invoked directly.

The features of x11-ssh-askpass are as follows:
+ Configurable via the standard X resource mechanism
  (/usr/lib/X11/app-defaults, ~/.Xdefaults, xrdb, etc.).
+ Requires only stock X11 libraries (libXt, libX11, libSM, libICE).
+ Can be configured to grab the keyboard and/or pointer (grabs the
  keyboard by default, not the pointer).

The user interface is somewhat different than most password/passphrase
dialogs and more similar to the X11-based passphrase dialog that
accompanies the regular SSH distribution.  Instead of a text field that
fills with asterisks or some other character as the user enters the
passphrase, a series of LED-like areas light up one-by-one with each
passphrase character entered, beginning from the lefthand edge of the
dialog.  When they reach the righthand edge, they go dark one-by-one
again, and so on.  This gives the user feedback that passphrase
characters have been entered, but does not provide onlookers with a
clue as to the length of the passphrase.

%prep
%setup -q

%build
%configure \
	--libexecdir=%openssh_askpass_dir \
	--mandir=%_mandir \
	--with-app-defaults-dir=%_sysconfdir/X11/app-defaults \
	#
xmkmf -a
%make_build CDEBUGFLAGS="%optflags"

%install
%make_install install install.man DESTDIR="%buildroot"
rm %buildroot{%openssh_askpass_dir/ssh-askpass,%_man1dir/ssh-askpass.*}

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name<<EOF
%openssh_askpass_dir/ssh-askpass	%openssh_askpass_dir/%name	20
EOF

%files
%config(noreplace) %_sysconfdir/X11/app-defaults/SshAskpass
%_altdir/%name
%openssh_askpass_dir/%name
%_man1dir/%name.*
%doc README TODO ChangeLog SshAskpass*.ad

%changelog
* Fri Dec 26 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.4.1-alt4
- Switched to alternatives-0.4.
- Updated build dependencies.

* Fri Dec 02 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.4.1-alt3
- Fixed bug in alternatives entries introduced in previous release.

* Wed Nov 30 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.4.1-alt2
- Relocated helper directory (#8565).
- Converted alternatives config file to new format (0.2.0).

* Mon May 05 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.2.4.1-alt1.1
- moved to new alternatives scheme

* Sat Feb 22 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.4.1-alt1
- Initial revision as separate package.
