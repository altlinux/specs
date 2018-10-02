%define _unpackaged_files_terminate_build 1
%def_with check

Name: custodia
Version: 0.6.0
Release: alt1

Summary: A tool for managing secrets
License: %gpl3plus
Group: System/Configuration/Other

Url: https://github.com/latchset/custodia
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-configparser
BuildRequires: python-module-coverage
BuildRequires: python-module-cryptography
BuildRequires: python-module-jwcrypto
BuildRequires: python-module-mock
BuildRequires: python-module-requests-gssapi
BuildRequires: python-module-tox
BuildRequires: python3-module-coverage
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-ipaclient
BuildRequires: python3-module-jwcrypto
BuildRequires: python3-module-requests-gssapi
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-tox
%endif

Requires: python3-module-%name = %EVR

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
%add_python_req_skip ipalib
%py_provides %name

%description -n python-module-%name
%overview

%package -n python3-module-%name
Summary: Subpackage with python3 custodia modules
Group: Development/Python
# module 'requests' doesn't contain 'urllib3', but imports within
%add_python3_req_skip requests.packages.urllib3.connection
%add_python3_req_skip requests.packages.urllib3.connectionpool
%py3_requires requests.packages
%py3_requires urllib3.connection
%py3_requires urllib3.connectionpool
%py3_provides %name

%description -n python3-module-%name
%overview

%prep
%setup
%patch -p1

# set the shebang to Python3
sed -i \
's@ExecStart=/usr/sbin/custodia\($\|[[:space:]]\+\)@ExecStart=/usr/sbin/custodia.py3 @' \
contrib/config/systemd/system/custodia@.service
rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_man7dir
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
install -m 644 -t "%buildroot%_man7dir" man/custodia.7
install -m 644 -t "%buildroot%_defaultdocdir/custodia" README API.md
install -m 644 -t "%buildroot%_defaultdocdir/custodia/examples" custodia.conf
install -m 600 %_builddir/%name-%version/contrib/config/custodia/custodia.conf %buildroot%_sysconfdir/custodia
install -m 644 %_builddir/%name-%version/contrib/config/systemd/system/custodia@.service  %buildroot%_unitdir
install -m 644 %_builddir/%name-%version/contrib/config/systemd/system/custodia@.socket  %buildroot%_unitdir
install -m 644 %_builddir/%name-%version/contrib/config/tmpfiles.d/custodia.conf  %buildroot%_tmpfilesdir/custodia.conf

%check
export PIP_INDEX_URL=http://host.invalid./
tox --sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
tox.py3 --sitepackages -e py%{python_version_nodots python3} -v -- -v
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
* Wed Sep 26 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.0 -> 0.6.0.
- Set Python3 as default within systemd service.

* Mon Jul 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt4
- Remove runtime requirements to setuptools (closes: #35114)

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt3
- NMU: rebuilt with python-3.6.

* Mon Jan 29 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt2
- Fix tests for Python3

* Wed Oct 25 2017 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
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

