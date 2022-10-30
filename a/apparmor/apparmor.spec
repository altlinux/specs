%define optflags_lto %nil
%define sover 1
%def_with check

# Knobs
%def_with pam
%def_with python

Name: apparmor
Version: 3.0.7
Release: alt4

Summary: Name-based Mandatory Access Control

License: GPL-2.0-or-later and LGPL-2.1-or-later
Group: System/Base
Url: https://apparmor.net

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: flex gcc-c++ perl-Pod-Checker python3-module-setuptools swig
BuildRequires: libstdc++-devel
%{?_with_check:BuildRequires: dejagnu perl-Locale-gettext}

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
%patch -p1

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
%makeinstall_std SBIN="%buildroot/sbin" APPARMOR_BIN_PREFIX="%buildroot/lib/apparmor" -C parser

mkdir -p %buildroot/lib/systemd/system
mv %buildroot/usr/lib/systemd/system/apparmor.service %buildroot/lib/systemd/system

rm %buildroot%_libdir/libapparmor.a

# relocate library to /%%_lib
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/libapparmor.so; do
	t=$(readlink "$f")
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/libapparmor.so.* %buildroot/%_lib

%find_lang apparmor

%check
export LD_LIBRARY_PATH="%buildroot%_lib:%buildroot%_libdir"
make check -C libraries/libapparmor
#make check -C parser
make check -C binutils

#make -C profiles check-parser

#make check -o check_lint -C utils PYFLAKES=pyflakes-py3

%post
if [ $1 -ge 2 ]; then
	/sbin/service apparmor condrestart ||:
else
	/sbin/chkconfig --add apparmor ||:
fi

%preun
if [ $1 = 0 ]; then
	/sbin/chkconfig --del apparmor ||:
fi

%files -f apparmor.lang
%config(noreplace) %_sysconfdir/apparmor
%dir %_sysconfdir/apparmor.d
%dir %_sysconfdir/apparmor.d/disable
%dir %_sysconfdir/apparmor.d/local
%_sysconfdir/apparmor.d/abi
%_sysconfdir/apparmor.d/abstractions
%_sysconfdir/apparmor.d/tunables

/lib/apparmor

/sbin/apparmor_parser
/sbin/rcapparmor
/usr/sbin/aa-audit
/usr/sbin/aa-autodep
/usr/sbin/aa-cleanprof
/usr/sbin/aa-complain
/usr/sbin/aa-decode
/usr/sbin/aa-disable
/usr/sbin/aa-enforce
/usr/sbin/aa-genprof
/usr/sbin/aa-logprof
/usr/sbin/aa-mergeprof
/usr/sbin/aa-notify
/usr/sbin/aa-remove-unknown
/usr/sbin/aa-status
/usr/sbin/aa-teardown
/usr/sbin/aa-unconfined
/usr/sbin/apparmor_status
%_bindir/aa-easyprof
%_bindir/aa-enabled
%_bindir/aa-exec
%_bindir/aa-features-abi

%_datadir/apparmor
%_man1dir/aa-enabled.1.xz
%_man1dir/aa-exec.1.xz
%_man1dir/aa-features-abi.1.xz
%_man5dir/apparmor.d.5.xz
%_man5dir/apparmor.vim.5.xz
%_man5dir/logprof.conf.5.xz
%_man7dir/apparmor.7.xz
%_man7dir/apparmor_xattrs.7.xz
%_man8dir/aa-audit.8.xz
%_man8dir/aa-autodep.8.xz
%_man8dir/aa-cleanprof.8.xz
%_man8dir/aa-complain.8.xz
%_man8dir/aa-decode.8.xz
%_man8dir/aa-disable.8.xz
%_man8dir/aa-easyprof.8.xz
%_man8dir/aa-enforce.8.xz
%_man8dir/aa-genprof.8.xz
%_man8dir/aa-logprof.8.xz
%_man8dir/aa-mergeprof.8.xz
%_man8dir/aa-notify.8.xz
%_man8dir/aa-remove-unknown.8.xz
%_man8dir/aa-status.8.xz
%_man8dir/aa-teardown.8.xz
%_man8dir/aa-unconfined.8.xz
%_man8dir/apparmor_parser.8.xz
%_man8dir/apparmor_status.8.xz

%_initdir/apparmor
%_unitdir/apparmor.service

%files -n libapparmor%sover
/%_lib/libapparmor.so.%sover
/%_lib/libapparmor.so.%sover.*

%files -n libapparmor-devel
%_includedir/aalogparse/aalogparse.h
%_includedir/sys/apparmor.h
%_includedir/sys/apparmor_private.h
%_pkgconfigdir/libapparmor.pc
%_libdir/libapparmor.so

%files -n libapparmor-devel-doc
%_man2dir/aa_change_hat.2.xz
%_man2dir/aa_change_profile.2.xz
%_man2dir/aa_find_mountpoint.2.xz
%_man2dir/aa_getcon.2.xz
%_man2dir/aa_query_label.2.xz
%_man2dir/aa_stack_profile.2.xz
%_man3dir/aa_features.3.xz
%_man3dir/aa_kernel_interface.3.xz
%_man3dir/aa_policy_cache.3.xz
%_man3dir/aa_splitcon.3.xz

%if_with python
%files -n python3-module-apparmor
%python3_sitelibdir_noarch/apparmor
%python3_sitelibdir_noarch/apparmor-%version-py3*.egg-info

%files -n python3-module-libapparmor
%python3_sitelibdir/LibAppArmor
%python3_sitelibdir/LibAppArmor-%version-py3*.egg-info
%endif

%if_with pam
%files -n pam0_apparmor
%doc changehat/pam_apparmor/README
%_pam_modules_dir/pam_apparmor.so
%endif

%changelog
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
