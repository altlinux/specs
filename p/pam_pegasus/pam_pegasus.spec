Name: pam_pegasus
Version: 0.2
Release: alt1

Summary: Pluggable private /tmp space support for interactive sessions
License: GPLv2+
Group: System/Base

Source: %name-%version.tar

BuildRequires: libpam-devel

%description
pam_pegasus is a PAM module which may be used with a PAM-aware login
service to provide per-user privately mounted /tmp directory
as a part of PAM session management.

The directory is being mounted with the following mount options:
-t tmpfs -o mode=0700,uid=UID,gid=GID,size=64g

This PAM module was implemented for use in pegasus systems, hence the name.

%prep
%setup

%build
cc %optflags %optflags_shared -Werror --shared \
	-Wl,--version-script,%name.map \
	%name.c -lpam -o %name.so
%set_verify_elf_method strict

%install
install -pDm644 %name.so %buildroot/%_lib/security/%name.so

%files
/%_lib/security/%name.so

%changelog
* Mon May 29 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2-alt1
- Changed tmpfs size from 25% to 64g.

* Fri Apr 15 2016 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
