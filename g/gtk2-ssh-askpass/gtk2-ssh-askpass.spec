Name: gtk2-ssh-askpass
Version: 5.4p1
Release: alt1

Summary: A GTK2-based passphrase dialog for use with OpenSSH
License: BSD-style
Group: Networking/Remote access
Url: http://www.openssh.com/

Source0: %name.c
Source1: %name.1
Patch: %name-fc-progress.patch

%define openssh_askpass_dir %_libexecdir/openssh

PreReq: alternatives >= 0:0.4, %openssh_askpass_dir
Requires: openssh-askpass-common
Provides: %openssh_askpass_dir/ssh-askpass
Provides: openssh-askpass-gtk2 = %version-%release
Provides: openssh-askpass-gnome = %version-%release
Obsoletes: openssh-askpass-gnome

BuildPreReq: libgtk+2-devel

%description
This is a Gtk2-based passphrase dialog for use with OpenSSH.
These dialogs are intended to be called from the ssh-add program and
not invoked directly.

There is only two run-time options: if you set the environment variable
"GNOME_SSH_ASKPASS_GRAB_SERVER=true" then %name will grab
the X server.  If you set "GNOME_SSH_ASKPASS_GRAB_POINTER=true", then the 
pointer will be grabbed too.  These may have some benefit to security if 
you don't trust your X server.  We grab the keyboard always.

%prep
%setup -qcT
install -pm644 %_sourcedir/%name.c .
%patch

%build
%__cc %optflags %name.c -o %name \
	`pkg-config --cflags gtk+-2.0` \
	`pkg-config --libs gtk+-2.0 x11`

%install
install -pD -m755 %name %buildroot%openssh_askpass_dir/%name
install -pD -m644 %_sourcedir/%name.1 %buildroot%_man1dir/%name.1

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name<<EOF
%openssh_askpass_dir/ssh-askpass	%openssh_askpass_dir/%name	10
EOF

%files
%_altdir/%name
%openssh_askpass_dir/%name
%_man1dir/%name.*

%changelog
* Tue May 22 2012 Dmitry V. Levin <ldv@altlinux.org> 5.4p1-alt1
- Updated to 5.4p1.
- Fixed build with ld --no-copy-dt-needed-entries.

* Fri Dec 26 2008 Dmitry V. Levin <ldv@altlinux.org> 5.1p1-alt2
- Imported manual page from Debian openssh package.
- Switched to alternatives-0.4.

* Fri Sep 12 2008 Dmitry V. Levin <ldv@altlinux.org> 5.1p1-alt1
- Updated to 5.1p1.
- Imported "progress" patch from FC package.

* Fri Dec 02 2005 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p1-alt3
- Fixed bug in alternatives entries introduced in previous release.

* Wed Nov 30 2005 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p1-alt2
- Relocated helper directory (#8565).
- Converted alternatives config file to new format (0.2.0).

* Mon May 05 2003 Stanislav Ievlev <inger@altlinux.ru> 3.6.1p1-alt1.1
- Moved to new alternatives scheme.

* Sat Apr 12 2003 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p1-alt1
- Updated to 3.6.1p1.

* Sat Feb 22 2003 Dmitry V. Levin <ldv@altlinux.org> 3.5p1-alt1
- Initial revision as separate package.
