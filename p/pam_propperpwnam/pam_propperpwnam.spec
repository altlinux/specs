Name: pam_propperpwnam
Version: 0.0.1
Release: alt2

Summary: PAM module that uses login name configured through NSS
License: BSD-3-Clause
Group: System/Base
Url: https://github.com/datenwolf/pam_propperpwnam

Source: %name-%version.tar

# due to PAM policy.
BuildRequires(pre): libpam-devel
# due to change in format of PAM modules requirements.
BuildRequires: rpm-build >= 0:4.0.4-alt55

%set_pam_name %name

%package -n %pam_name
Summary: PAM module that uses login name configured through NSS
Group: System/Base
Provides: %name = %version-%release
Obsoletes: %name

%description
A PAM module that uses the entered login name as key to
query the password database configured through nsswitch.conf
and replaces the login name with what has been returned.
pam_mktemp is a PAM module which may be used with a PAM-aware login
service to provide per-user private directories under /tmp as a part
of PAM session or account management.

%description -n %pam_name
A PAM module that uses the entered login name as key to
query the password database configured through nsswitch.conf
and replaces the login name with what has been returned.
pam_mktemp is a PAM module which may be used with a PAM-aware login
service to provide per-user private directories under /tmp as a part
of PAM session or account management.

%prep
%setup
sed -i 's/$(CC)/$(CC) $(CFLAGS)/' Makefile

%build
%make_build CC=gcc CFLAGS="%optflags %optflags_shared -Werror"

%install
install -D -m 644 pam_propperpwnam.so %buildroot/%_lib/security/pam_propperpwnam.so
install -D -m 755 pam_propperpwnam.control %buildroot/%_sysconfdir/control.d/facilities/pam_propperpwnam

%files -n %pam_name
/%_lib/security/*
%_sysconfdir/control.d/facilities/pam_propperpwnam
%doc LICENSE README

%changelog
* Wed Dec 13 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.0.1-alt2
- Add control pam_propperpwnam for support module in system authentication (ALT#47713).

* Tue Jul 04 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus.

