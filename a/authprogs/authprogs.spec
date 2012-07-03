# Spec file for authporgs utility

Name: authprogs
Version: 0.5
Release: alt1

Summary: SSH command authenticator

License: %gpl2plus
Group: Security/Networking
URL: http://www.hackinglinuxexposed.com/tools/authprogs/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar
Source1: default.conf
Source2: README.alt

BuildRequires(pre): rpm-build-licenses

%description
authprogs is a SSH command authenticator. It is intended to be
called from an authorized_keys file,  i.e. triggered by use of
specific SSH identities.

It will check the original command (saved in SSH_ORIGINAL_COMMAND
environment variable by sshd) and see if it is on the 'approved'
list.

For details see README.alt.

%prep
%setup
mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

cp --  %SOURCE2 .

%install
install -d %buildroot%_bindir
install -m 0755 %name %buildroot%_bindir/%name
install -m 0751 -d -- %buildroot%_sysconfdir/%name
install -m 0644 %SOURCE1 %buildroot%_sysconfdir/%name/default.conf

%files
%doc README TODO BUGS README.alt
%doc --no-dereference COPYING
%_bindir/%name
%attr(0751,root,root) %dir %_sysconfdir/%name
%_sysconfdir/%name/default.conf

%changelog
* Thu Apr 12 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.5-alt1
- Initial build for ALT Linux Sisyphus


