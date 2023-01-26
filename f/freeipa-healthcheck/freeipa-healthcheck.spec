%define _libexecdir %_usr/libexec
%define _unpackaged_files_terminate_build 1
%def_with check
# don't remove: it's used on local build
%def_without pylint

Name: freeipa-healthcheck
Version: 0.12
Release: alt1

Summary: Check the health of a FreeIPA installation
License: GPLv3
Group: System/Base
Url: https://github.com/freeipa/freeipa-healthcheck

Source0: %name-%version.tar.gz
Patch: %name-%version-alt.patch

# Dogtag PKI 11.2.1 requires Java 17 that is not built for armh
ExcludeArch: %ix86 armh

Requires: python3-module-%name = %EVR
Requires: dogtag-pki-healthcheck

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3-module-ipaserver
BuildRequires: python3(pytest)
BuildRequires: /proc

%if_with pylint
BuildRequires: python3(pylint)
%endif

%endif

%description
%name is a framework which is needed to assist with the identification,
diagnosis and potentially repair of problems.

%package -n python3-module-%name
Summary: Python modules for %name
License: GPLv3
Group: Development/Python3
Requires: python3-module-lib389 >= 1.4.1.11

%description -n python3-module-%name
Python modules for %name.

%package -n python3-module-%name-core
Summary: Core plugin system for %name
License: GPLv3
Group: Development/Python3
# core plugin was a part of python3-freeipa-healthcheck
Conflicts: python3-module-freeipa-healthcheck <= 0.9-alt2

%description -n python3-module-%name-core
Core plugin system for %name.

%prep
%setup

%patch -p1

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_sysconfdir/ipahealthcheck
echo "[default]" > %buildroot%_sysconfdir/ipahealthcheck/ipahealthcheck.conf

mkdir -p %buildroot%_unitdir

mkdir -p %buildroot%_libexecdir/ipa
install -p -m755 systemd/ipa-healthcheck.sh %buildroot%_libexecdir/ipa/

mkdir -p %buildroot%_logrotatedir/ipahealthcheck
install -p -m644 logrotate/ipahealthcheck %buildroot%_logrotatedir/ipahealthcheck/

mkdir -p %buildroot%_logdir/ipa/healthcheck
mkdir -p %buildroot%_man5dir
mkdir -p %buildroot%_man8dir
install -p -m644 man/man5/ipahealthcheck.conf.5 %buildroot%_man5dir/
install -p -m644 man/man8/ipa-healthcheck.8 %buildroot%_man8dir/
install -p -m644 systemd/ipa-healthcheck.service %buildroot%_unitdir/
install -p -m644 systemd/ipa-healthcheck.timer %buildroot%_unitdir/

# since we package python modules as arch dependent
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%post
%post_service ipa-healthcheck

%preun
%preun_service ipa-healthcheck

%check
%pyproject_run_pytest -vra

%if_with pylint
# it's needed for pylint's plugin
export PYTHONPATH="$(pwd)"
%pyproject_run -- python -m pylint \
    --rcfile=pylintrc --load-plugins=pylint_plugins src tests
%endif

%files
%doc README.md COPYING
%_bindir/ipa-healthcheck
%_bindir/ipa-clustercheck
%_sysconfdir/ipahealthcheck/
%_unitdir/ipa-healthcheck.service
%_unitdir/ipa-healthcheck.timer
%_libexecdir/ipa
%_logdir/ipa/healthcheck
%_logrotatedir/ipahealthcheck
%_man5dir/ipahealthcheck.conf.5.xz
%_man8dir/ipa-healthcheck.8.xz

%files -n python3-module-%name
%python3_sitelibdir/ipahealthcheck/
%python3_sitelibdir/ipahealthcheck-%version-py%__python3_version-nspkg.pth
%python3_sitelibdir/ipahealthcheck-%version.dist-info/
%python3_sitelibdir/ipaclustercheck/
%exclude %python3_sitelibdir/ipahealthcheck/core/

%files -n python3-module-%name-core
%python3_sitelibdir/ipahealthcheck/core/

%changelog
* Mon Jan 23 2023 Stanislav Levin <slev@altlinux.org> 0.12-alt1
- 0.11 -> 0.12.

* Tue Aug 23 2022 Stanislav Levin <slev@altlinux.org> 0.11-alt2
- Skipped build on armh (Java 17).

* Mon Jun 27 2022 Stanislav Levin <slev@altlinux.org> 0.11-alt1
- 0.10 -> 0.11.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 0.10-alt1
- 0.9 -> 0.10.

* Thu Dec 02 2021 Stanislav Levin <slev@altlinux.org> 0.9-alt3
- Applied upstream fixes.

* Thu Sep 09 2021 Stanislav Levin <slev@altlinux.org> 0.9-alt2
- Applied upstream fix (GH#213).

* Fri Jun 18 2021 Stanislav Levin <slev@altlinux.org> 0.9-alt1
- 0.8 -> 0.9.

* Tue Mar 30 2021 Stanislav Levin <slev@altlinux.org> 0.8-alt1
- 0.7 -> 0.8.

* Fri Nov 06 2020 Stanislav Levin <slev@altlinux.org> 0.7-alt1
- 0.6 -> 0.7.

* Thu Aug 06 2020 Stanislav Levin <slev@altlinux.org> 0.6-alt2
- Applied upstream fixes.

* Wed Jul 22 2020 Stanislav Levin <slev@altlinux.org> 0.6-alt1
- Initial build (by Ivan Alekseev <qwetwe@altlinux.org>).
