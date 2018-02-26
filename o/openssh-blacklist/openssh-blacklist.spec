Name: openssh-blacklist
Version: 0.3
Release: alt1

Summary: Blacklist file for openssh
License: GPLv3+
Group: Networking/Remote access
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ftp.debian.org/debian/pool/main/o/%name/%{name}_%{version}.tar.gz
Source: %name-%version.tar
Source1: utils-%version.tar

Requires: /etc/openssh

%description
This package contains blacklist file with default blacklisted OpenSSH
RSA and DSA keys.

%package utils
Summary: Blacklist file utils for openssh
License: ISC-style
Group: Networking/Remote access
Requires: %name = %version-%release

%description utils
This package contains blacklist file utils used to create and verify
blacklist files for openssh.

%prep
%setup -q -a1

%build
%__cc %optflags utils-%version/blacklist-check.c -o %name-check
%__cc %optflags utils-%version/blacklist-encode.c -o %name-encode
cat [DR]SA-{1024,2048}.[bl]e{32,64} |./%name-encode 6 >blacklist

%install
mkdir -p %buildroot{%_bindir,/etc/openssh}
install -pm644 blacklist %buildroot/etc/openssh/
install -pm755 %name-{check,encode} %buildroot%_bindir/

%files
%config /etc/openssh/*

%files utils
%_bindir/*

%changelog
* Mon May 26 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Initial revision.
