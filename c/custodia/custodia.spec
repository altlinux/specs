%define _unpackaged_files_terminate_build 1

# FreeIPA up to 4.4.4 are not compatible with custodia because the custodia
# script now runs under Python 3. FreeIPA 4.4.5 and 4.4.4-2 on F26 are fixed.
%define ipa_conflict 4.4.5

Name: custodia
Version: 0.5.0
Release: alt1%ubt
Summary: A tool for managing secrets

Group: System/Configuration/Other
License: %gpl3plus
Url: https://github.com/latchset/custodia
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python-module-jwcrypto >= 0.4.2
BuildRequires: python-module-requests
BuildRequires: python-module-coverage
BuildRequires: python-module-tox >= 2.3.1
BuildRequires: python-module-systemd
BuildRequires: python-module-virtualenv
BuildRequires: python-module-configparser
BuildRequires: python-module-coverage
BuildRequires: python-module-cryptography
BuildRequires: python-module-etcd
BuildRequires: python-modules-sqlite3
BuildRequires: python-module-pytest
BuildRequires: python-module-pytest-runner
BuildRequires: python-module-pytest-cov
BuildRequires: pytest
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-jwcrypto >= 0.4.2
BuildRequires: python3-module-requests
BuildRequires: python3-module-coverage
BuildRequires: python3-module-tox >= 2.3.1
BuildRequires: python3-module-systemd
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-configparser
BuildRequires: python3-module-coverage
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-etcd
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-pytest-cov
BuildRequires: pytest3

Requires: python3-module-custodia = %version-%release

Conflicts: freeipa-server-common < %ipa_conflict

%define overview                                                              \
Custodia is a Secrets Service Provider, it stores or proxies access to keys,  \
password, and secret material in general. Custodia is built to use the HTTP   \
protocol and a RESTful API as an IPC mechanism over a local Unix Socket. It   \
can also be exposed to a network via a Reverse Proxy service assuming proper  \
authentication and header validation is implemented in the Proxy.             \
                                                                              \
Custodia is modular, the configuration file controls how authentication,      \
authorization, storage and API plugins are combined and exposed.

%description
%overview

%package -n python-module-%name
Summary: Subpackage with python custodia modules
Group: Development/Python
Requires: python-module-setuptools
Requires: python-module-jwcrypto >= 0.4.2
Requires: python-module-requests
Requires: python-module-systemd
Requires: python-module-configparser
Requires: python-module-urllib3
Conflicts: python-module-freeipa < %ipa_conflict
%py_provides %name

%description -n python-module-%name
%overview

%package -n python3-module-%name
Summary: Subpackage with python3 custodia modules
Group: Development/Python
Requires: python3-module-setuptools
Requires: python3-module-jwcrypto >= 0.4.2
Requires: python3-module-requests
Requires: python3-module-systemd
Requires: python3-module-configparser
Requires: python3-module-urllib3
%py3_provides %name

%description -n python3-module-%name
%overview

%prep
%setup
%patch -p1
rm -rf ../python3
cp -a . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_mandir/man7
mkdir -p %buildroot%_defaultdocdir/custodia
mkdir -p %buildroot%_defaultdocdir/custodia/examples
mkdir -p %buildroot%_sysconfdir/custodia
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_tmpfilesdir
mkdir -p %buildroot%_sharedstatedir/custodia
mkdir -p %buildroot%_logdir/custodia
mkdir -p %buildroot%_runtimedir/custodia

pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
        mv -v $i $i.py3
done
popd

%python_install
mv -v %buildroot%_bindir/custodia %buildroot%_sbindir/custodia
mv -v %buildroot%_bindir/custodia.py3 %buildroot%_sbindir/custodia.py3
install -m 644 -t "%buildroot%_mandir/man7" man/custodia.7
install -m 644 -t "%buildroot%_defaultdocdir/custodia" README API.md
install -m 644 -t "%buildroot%_defaultdocdir/custodia/examples" custodia.conf
install -m 600 %_builddir/%name-%version/contrib/config/custodia/custodia.conf %buildroot%_sysconfdir/custodia
install -m 644 %_builddir/%name-%version/contrib/config/systemd/system/custodia@.service  %buildroot%_unitdir
install -m 644 %_builddir/%name-%version/contrib/config/systemd/system/custodia@.socket  %buildroot%_unitdir
install -m 644 %_builddir/%name-%version/contrib/config/tmpfiles.d/custodia.conf  %buildroot%_tmpfilesdir/custodia.conf
#workaround fix to python2.7 import error of custodia's module
touch %buildroot%python_sitelibdir/%name/__init__.py

%check
# don't download packages
export PIP_INDEX_URL=http://host.invalid./

export PYTHONPATH=%buildroot%python_sitelibdir_noarch:%python_sitelibdir_noarch:%_libdir/python2.7/site-packages
TOX_TESTENV_PASSENV='PYTHONPATH' tox -e py27 -v

pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch:%python3_sitelibdir_noarch:%_libdir/python3/site-packages
TOX_TESTENV_PASSENV='PYTHONPATH' tox -e py35 -v
popd

%pre
getent group custodia >/dev/null || groupadd -r custodia
getent passwd custodia >/dev/null || \
    useradd -r -g custodia -d / -s /sbin/nologin \
    -c "User for custodia" custodia
exit 0

%post
%systemd_post custodia@\*.socket
%systemd_post custodia@\*.service

%preun
%systemd_preun custodia@\*.socket
%systemd_preun custodia@\*.service

%postun
%systemd_postun custodia@\*.socket
%systemd_postun custodia@\*.service

%files
%doc %_defaultdocdir/custodia
%doc %_defaultdocdir/custodia/examples/custodia.conf
%_man7dir/custodia*
%dir %attr(0700,custodia,custodia) %_sysconfdir/custodia
%config(noreplace) %attr(600,custodia,custodia) %_sysconfdir/custodia/custodia.conf
%attr(644,root,root)  %_unitdir/custodia@.socket
%attr(644,root,root)  %_unitdir/custodia@.service
%dir %attr(0700,custodia,custodia) %_sharedstatedir/custodia
%dir %attr(0700,custodia,custodia) %_logdir/custodia
%dir %attr(0755,custodia,custodia) %_runtimedir/custodia
%_tmpfilesdir/custodia.conf

%files -n python-module-%name
%python_sitelibdir/%name
%python_sitelibdir/%name-%version-py%_python_version.egg-info
%python_sitelibdir/%name-%version-py%_python_version-nspkg.pth
%_sbindir/custodia
%_bindir/custodia-cli

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version-py%_python3_version.egg-info
%python3_sitelibdir/%name-%version-py%_python3_version-nspkg.pth
%_sbindir/custodia.py3
%_bindir/custodia-cli.py3

%changelog
* Wed Oct 25 2017 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1%ubt
- Put v0.5.0 sources from https://github.com/latchset/custodia

* Tue Sep 26 2017 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt4
- Really fix SimpleCreds authenticator.

* Fri Aug 04 2017 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt3
- Fix SimpleCreds authenticator.

* Thu Oct 06 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt2
- Mive binary to %%_sbindir.

* Wed May 11 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Allow tox to use locally installed packages (patch from upstream).
- Initial build.

