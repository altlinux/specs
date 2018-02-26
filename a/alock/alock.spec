Name: alock
Version: 0.0.1
Release: alt0.svn94.0
URL: http://code.google.com/p/alock/

Summary: Locks the local X display until the correct password is entered
License: free
Group: System/X11
Packager: Andriy Stepanov <stanv@altlinux.ru>
Patch1: alt_change_pam_scheme.diff

Source: %name.tar
Source1: %name.pam

BuildRequires: imlib2-devel libXcursor-devel libXpm-devel libXrender-devel libXxf86misc-devel libfreetype-devel libpam-devel xorg-bitmaps

%description
'alock' locks the X server until the user enters the correct password at the
keyboard. If the authentification was successful, the X server is
unlocked and the user can continue to work.

'alock' does not provide fancy animations like 'xlock' and 'xscreensaver'
and never will. It's just for locking the current X session.

When 'alock' is started it just waits for the first keypress. This first
keypress is to indicate that the user now wants to type in the password.
A colored frame is drawn around the screen and the user can now type in
his password. If it was typed in incorrectly, the colored frame turns red and
the user has to wait a certain timeout.

%prep
%setup -n %name
%patch1 -p2

%build
%configure \
        --with-xrender \
        --with-xcursor \
        --with-imlib2 \
        --with-xpm \
        --with-pam \
        --with-hash

%make_build

%install
install -pm0644 -D %{S:1} %buildroot%_sysconfdir/pam.d/%name
%makeinstall

%files
%_bindir/*
%_datadir/%name/bitmaps/*.xbm
%_datadir/%name/xcursors/*
%_man1dir/*
%_sysconfdir/pam.d/%name
%doc LICENSE.txt README.txt CHANGELOG.txt

%changelog
* Fri Apr 13 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt0.svn94.0
- Import to ALT Linux Sisyphus

