Name: pam_fabo
Version: 0.1.1
Release: alt1

Summary: PAM false bottom module
License: GPL-2.0-or-later
Group: System/Base
URL: git.altlinux.org/people/ved/public/pam_fabo.git

Source: %name-%version.tar

BuildRequires(pre): libpam-devel

%description
FAlse BOttom is a pam module for mapping passwords to actions.

%prep
%setup

%build
%make_build

%install
%make_install install \
                  DESTDIR=%buildroot \
                  SBINDIR=%_sbindir \
                  SLIBDIR=%_libdir \

%files
%_libdir/security/pam_fabo.so
%_sbindir/fabo_syntax_checker
%doc README

%changelog
* Mon Jul 28 2025 Egor Shestakov <ved@altlinux.org> 0.1.1-alt1
- Initial build. 
