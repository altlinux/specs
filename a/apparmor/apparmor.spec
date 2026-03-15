%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define optflags_lto %nil
%define sover 1
%def_with check

# Knobs
%def_with pam
%def_with python

Name: apparmor
Version: 4.1.7
Release: alt1

Summary: Name-based Mandatory Access Control

License: GPL-2.0-or-later and LGPL-2.1-or-later
Group: System/Base
Url: https://apparmor.net
Vcs: https://gitlab.com/apparmor/apparmor.git

BuildRequires(pre): rpm-macros-pam0
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: /usr/bin/podchecker
BuildRequires: /usr/bin/swig
BuildRequires: /usr/bin/pod2html
BuildRequires: autoconf-archive
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-devel-static

%if_with check
BuildRequires: dejagnu
BuildRequires: perl-Locale-gettext
BuildRequires: python3(notify2)
BuildRequires: python3(psutil)
BuildRequires: python3(tkinter)
BuildRequires: python3(gi)
%endif

Source: %name-%version.tar

%description
AppArmor is a Mandatory Access Control (MAC) mechanism which uses the
Linux Security Module (LSM) framework. The confinement's restrictions
are mandatory and are not bound to identity, group membership, or object
ownership. The protections provided are in addition to the kernel's
regular access control mechanisms (including DAC) and can be used to
restrict the superuser.

%package -n libapparmor%sover
Summary: Apparmor library
Group: System/Libraries

%description -n libapparmor%sover
AppArmor is a Mandatory Access Control (MAC) mechanism which uses the
Linux Security Module (LSM) framework. The confinement's restrictions
are mandatory and are not bound to identity, group membership, or object
ownership. The protections provided are in addition to the kernel's
regular access control mechanisms (including DAC) and can be used to
restrict the superuser.

%package -n libapparmor-devel
Summary: Development files for libapparmor
Group: System/Libraries

%description -n libapparmor-devel
%summary.

%package -n libapparmor-devel-doc
Summary: Documantaion for AppArmor API
Group: System/Libraries

%description -n libapparmor-devel-doc
%summary.

%if_with python
%package -n python3-module-apparmor
Summary: Python module for AppArmor
Group: Development/Python3
BuildArch: noarch
# IDK why this happens, filter needless dependency to make the package really noarch
%filter_from_requires /^\/usr\/lib\/python3\/site-packages/d

%description -n python3-module-apparmor
%summary.

%package -n python3-module-libapparmor
Summary: Python module for libapparmor
Group: Development/Python3

%description -n python3-module-libapparmor
%summary.
%endif

%if_with pam
%package -n pam0_apparmor
Summary: PAM AppArmor module.
Group: System/Libraries
BuildRequires(pre): rpm-macros-pam0
BuildRequires: libpam-devel

%description -n pam0_apparmor
%summary.
%endif

%prep
%setup

%build
pushd libraries/libapparmor
%autoreconf
%configure \
	%{subst_with python} \
	#
%make_build
popd

make -C utils

make -C binutils

make -C parser

make -C profiles

%{?_with_pam: make -C changehat/pam_apparmor}

%install
%makeinstall_std -C libraries/libapparmor
%makeinstall_std -C utils
%makeinstall_std -C binutils
%makeinstall_std -C profiles
%{?_with_pam: %makeinstall_std -C changehat/pam_apparmor SECDIR=%buildroot%_pam_modules_dir}
%makeinstall_std SBIN="%buildroot/sbin" APPARMOR_BIN_PREFIX="%buildroot/lib/apparmor" install-systemd -C parser

rm %buildroot%_libdir/libapparmor.a

# relocate library to /%%_lib
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/libapparmor.so; do
	t=$(readlink "$f")
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/libapparmor.so.* %buildroot/%_lib

%find_lang apparmor --all-name

#mkdir -p %buildroot%_unitdir/
#mv -fv %buildroot/lib/systemd/system/apparmor.service %buildroot%_unitdir/
#
#mv -fv %buildroot/lib/apparmor %buildroot/usr/lib/

%check
export LD_LIBRARY_PATH="%buildroot%_lib:%buildroot%_libdir"
# thanks, Arch
echo "INFO: Running check: libraries/libapparmor"
make -C libraries/libapparmor check
echo "INFO: Running check binutils"
make -C binutils check
# echo "INFO: Running check parser"
# make -C parser check
# NOTE: the profiles checks are notoriously broken, so run each separately
echo "INFO: Running check-abstractions.d profiles"
make -C profiles check-abstractions.d
#  # many hardcoded paths are not accounted for:
#  # https://gitlab.com/apparmor/apparmor/-/issues/137
#  echo "INFO: Running check-logprof profiles"
#  make -C profiles check-logprof
echo "INFO: Running check-parser profiles"
make -C profiles check-parser
# echo "INFO: Running check utils"
# we do not care about linting when running tests
# https://gitlab.com/apparmor/apparmor/-/issues/121
# make PYFLAKES='/usr/bin/true' -C utils check


%files -f apparmor.lang
%doc LICENSE README.md
%config(noreplace) %_sysconfdir/apparmor
%dir %_sysconfdir/apparmor.d
%_sysconfdir/apparmor.d/*

%_bindir/aa-easyprof
%_bindir/aa-enabled
%_bindir/aa-exec
%_bindir/aa-features-abi

/lib/apparmor/apparmor.systemd
/lib/apparmor/profile-load
/lib/apparmor/rc.apparmor.functions

/usr/sbin/aa-audit
/usr/sbin/aa-autodep
/usr/sbin/aa-cleanprof
/usr/sbin/aa-complain
/usr/sbin/aa-decode
/usr/sbin/aa-disable
/usr/sbin/aa-enforce
/usr/sbin/aa-genprof
/usr/sbin/aa-load
/usr/sbin/aa-logprof
/usr/sbin/aa-mergeprof
/usr/sbin/aa-notify
/usr/sbin/aa-remove-unknown
/usr/sbin/aa-status
/usr/sbin/aa-teardown
/usr/sbin/aa-unconfined
/usr/sbin/apparmor_status

%dir %_datadir/apparmor
%_datadir/apparmor/*
%_datadir/polkit-1/actions/net.apparmor.pkexec.aa-notify.policy

%_man1dir/aa-enabled.1*
%_man1dir/aa-exec.1*
%_man1dir/aa-features-abi.1*
%_man5dir/apparmor.d.5*
%_man5dir/apparmor.vim.5*
%_man5dir/logprof.conf.5*
%_man7dir/apparmor.7*
%_man7dir/apparmor_xattrs.7*
%_man8dir/aa-audit.8*
%_man8dir/aa-autodep.8*
%_man8dir/aa-cleanprof.8*
%_man8dir/aa-complain.8*
%_man8dir/aa-decode.8*
%_man8dir/aa-disable.8*
%_man8dir/aa-easyprof.8*
%_man8dir/aa-enforce.8*
%_man8dir/aa-genprof.8*
%_man8dir/aa-load.8*
%_man8dir/aa-logprof.8*
%_man8dir/aa-mergeprof.8*
%_man8dir/aa-notify.8*
%_man8dir/aa-remove-unknown.8*
%_man8dir/aa-status.8*
%_man8dir/aa-teardown.8*
%_man8dir/aa-unconfined.8*
%_man8dir/apparmor_parser.8*
%_man8dir/apparmor_status.8*

/sbin/apparmor_parser

%_unitdir/apparmor.service

%files -n libapparmor%sover
/%_lib/libapparmor.so.%sover
/%_lib/libapparmor.so.%sover.*

%files -n libapparmor-devel
%dir %_includedir/aalogparse
%dir %_includedir/sys

%_includedir/aalogparse/aalogparse.h
%_includedir/sys/apparmor.h
%_includedir/sys/apparmor_private.h
%_pkgconfigdir/libapparmor.pc
%_libdir/libapparmor.so

%files -n libapparmor-devel-doc
%_man2dir/aa_change_hat.2*
%_man2dir/aa_change_profile.2*
%_man2dir/aa_find_mountpoint.2*
%_man2dir/aa_getcon.2*
%_man2dir/aa_query_label.2*
%_man2dir/aa_stack_profile.2*
%_man3dir/aa_features.3*
%_man3dir/aa_kernel_interface.3*
%_man3dir/aa_policy_cache.3*
%_man3dir/aa_splitcon.3*

%if_with python
%files -n python3-module-apparmor
%python3_sitelibdir_noarch/apparmor
%python3_sitelibdir_noarch/apparmor-%version-py3*.egg-info

%files -n python3-module-libapparmor
%python3_sitelibdir/LibAppArmor.py
%python3_sitelibdir/_LibAppArmor.cpython-3*.so
%python3_sitelibdir/__pycache__/LibAppArmor.cpython-3*.pyc
%python3_sitelibdir/LibAppArmor-%version-py3*.egg-info
%endif

%if_with pam
%files -n pam0_apparmor
%doc changehat/pam_apparmor/README
%_pam_modules_dir/pam_apparmor.so
%endif

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 4.1.7-alt1
- New version 4.1.7.

* Sat Feb 28 2026 Nikolay Strelkov <snk@altlinux.org> 4.1.6-alt1
- NMU: new version 4.1.6.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 4.1.4-alt1
- NMU: new version 4.1.4.

* Thu Jan 08 2026 Nikolay Strelkov <snk@altlinux.org> 4.1.3-alt1
- NMU: new version 4.1.3.

* Fri Oct 31 2025 Nikolay Strelkov <snk@altlinux.org> 4.1.2-alt1
- NMU: major version upgrade (4.1.2) with rpmgs script (closes #56684)

* Thu Oct 30 2025 Nikolay Strelkov <snk@altlinux.org> 3.0.9-alt3
- NMU: removed dependency on /sbin/telinit (closes #56684)

* Tue Jul 15 2025 Nikolay Strelkov <snk@altlinux.org> 3.0.9-alt2
- NMU: added missed build-dependies - rpm-macros-systemd and pod2html.
- NMU: moved the systemd unitfile to the correct location.
- NMU: built with localization.
- NMU: moved /lib/apparmor to /usr/lib/apparmor.
- NMU: filtered out strange /usr/etc/rc.d/init.d/apparmor from Requires

* Thu Mar 09 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.9-alt1
- Updated to v3.0.9.

* Sun Oct 30 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.7-alt4
- Built pam0_apparmor subpackage.
- Partially enabled tests.

* Sun Oct 16 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.7-alt3
- Packed man pages for 5 section.

* Sun Oct 16 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.7-alt2
- SysVInit: Added condrestart.
- Added post-install and pre-uninstall scripts.
- Fixed configs.
- Fixed license.

* Sat Oct 15 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.7-alt1
- Initial build with a basic support for ALT Sisyphus.
