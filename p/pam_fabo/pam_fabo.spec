%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: pam_fabo
Version: 0.1.3
Release: alt1

Summary: PAM false bottom module
License: GPL-2.0-or-later
Group: System/Base
URL: http://git.altlinux.org/people/ved/public/pam_fabo.git
VCS: git://git.altlinux.org/people/ved/public/pam_fabo.git

Source: %name-%version.tar

BuildRequires(pre): libpam-devel

%description
FAlse BOttom is a pam module for mapping passwords to actions.

%set_pam_name pam_fabo

%package -n %pam_name
Summary: %summary
Group: System/Base
Provides: pam_fabo = %EVR
# Before and include 0.1.2-alt1 doesn't comply to the PAM packaging policy
Obsoletes: pam_fabo <= 0.1.2-alt1

%description -n %pam_name
FAlse BOttom is a pam module for mapping passwords to actions.

%prep
%setup

%build
%make_build

%install
%makeinstall_std SBINDIR=%_sbindir SLIBDIR=%_libdir

%files -n %pam_name
%_pam_modules_dir/pam_fabo.so
%_sbindir/fabo_syntax_checker
%doc README
%doc examples/

%changelog
* Tue Nov 11 2025 Egor Shestakov <ved@altlinux.org> 0.1.3-alt1
- Multiple fabo files support.
- Packaging:
  + Package examples directory as documentation.
  + Correspond to Linux-PAM packaging policy.
- Add protocols part to URL and VCS tags in the spec.

* Wed Oct 22 2025 Egor Shestakov <ved@altlinux.org> 0.1.2-alt1
- Hardening permissions to the fabo executables.
- Move spec to altlinux directory.
- Add VCS tag to spec.
- Minor spec cleanup.

* Mon Jul 28 2025 Egor Shestakov <ved@altlinux.org> 0.1.1-alt1
- Initial build.
