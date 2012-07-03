Name:       kup
Version:    0.3.2
Release:    alt1
Summary:    Kernel.org Uploader

Group:      Development/Tools
License:    GPLv2
URL:        https://git.kernel.org/?p=utils/kup/kup.git;a=summary
Source0:    https://www.kernel.org/pub/software/network/kup/kup-%{version}.tar.xz
Source1:    kup-server-tmpfiles.conf
BuildArch:  noarch

BuildRequires: gnupg perl-BSD-Resource perl-Config-Simple perl-Encode perl-Git

%description
Kup is a secure upload tool used by kernel developers to upload
cryptographically verified packages to kernel.org.

This package includes the client-side kup utility.


%package server
Summary:    Kernel.org Uploader - server utilities
Group:      Development/Tools
Requires:   gnupg, xz

%description server
Kup is a secure upload tool used by kernel developers to upload
cryptographically verified packages to kernel.org.

This package includes the server-side kup-server utility.


%package server-utils
Summary:    Kernel.org Uploader - administration tools
Group:      Development/Tools
Requires:   kup-server = %version-%release

%description server-utils
Kup is a secure upload tool used by kernel developers to upload
cryptographically verified packages to kernel.org.

This package includes additional tools to help in kup-server administration.


%prep
%setup -q

%install
mkdir -p -- \
	%buildroot/%_bindir \
	%buildroot/%_man1dir \
	%buildroot/%_sysconfdir/kup \
	%buildroot/%_localstatedir/run/kup

install -pm 0755 kup gpg-sign-all genrings kup-server %buildroot/%_bindir
install -pm 0644 kup.1 %buildroot/%_man1dir/
install -pm 0644 kup-server.cfg %buildroot/%_sysconfdir/kup/kup-server.cfg

# Runtime directories and files
mkdir -pm 0755 \
	%buildroot/%_localstatedir/kup/{pub,tmp,pgp} \
	%buildroot/%_sysconfdir/tmpfiles.d

install -pm 0644 %SOURCE1 %buildroot/%_sysconfdir/tmpfiles.d/kup-server.conf
touch %buildroot/%_localstatedir/run/kup/lock

%files
%doc COPYING
%_bindir/kup
%_man1dir/kup.*

%files server
%doc README test
%config(noreplace) %_sysconfdir/tmpfiles.d/kup-server.conf
%config %dir %_sysconfdir/kup
%config(noreplace) %_sysconfdir/kup/kup-server.cfg
%_bindir/kup-server
%dir %attr(1777,root,root) %_localstatedir/kup/tmp
%dir %_localstatedir/kup
%dir %_localstatedir/kup/pgp
%dir %_localstatedir/kup/pub
%dir %_localstatedir/run/kup
%_localstatedir/run/kup/lock

%files server-utils
%_bindir/gpg-sign-all
%_bindir/genrings

%changelog
* Thu Jan 12 2012 Alexey Gladkov <legion@altlinux.ru> 0.3.2-alt1
- Upstream 0.3.2

* Thu Nov 24 2011 Konstantin Ryabitsev <mricon@kernel.org> - 0.3.1-1
- Upstream 0.3.1
- Upstream now releases tarballs, so remove the gen-tarball script.

* Fri Nov 18 2011 Konstantin Ryabitsev <mricon@kernel.org> - 0.3-2
- Require gnupg and xz for kup-server (gzip and bzip2 are in base)

* Wed Nov 16 2011 Konstantin Ryabitsev <mricon@kernel.org> - 0.3-1
- Use the git-checkout notation as per Fedora guidelines.
- Move "test" dir to be with the -server package.
- Make kup-client to just be the "kup" package.
- Provide the kup-generate-tarball.sh script to automate tarball generation.
- Create a -server-utils subpackage for gpg-sign-all and genrings tools.
- Create a tmpfiles entry for systemd (needed for F15 and above).

* Mon Nov 14 2011 Konstantin Ryabitsev <mricon@kernel.org>
- Match Fedora's spec format.
- Generate runtime directories.

* Mon Oct 17 2011 John 'Warthog9' Hawley <warthog9@kernel.org>
- created spec file
