Name: python3-module-aiocoap
Version: 0.4.17
Release: alt1

Summary: The Python CoAP library
License: MIT
Group: Development/Python
URL: https://pypi.org/project/aiocoap
VCS: https://github.com/chrysn/aiocoap

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: /usr/bin/openssl
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_tox tox.ini testenv

%build
%pyproject_build

%install
%pyproject_install

%check
# The build chroot has no hostname resolving to ::1 (/etc/hosts maps ::1 to
# localhost6 only; editing host hasher config is out of scope), and its only
# interfaces are loopback, so OS-level connectivity error reporting differs.
# Deselect the tests that depend on a ::1-resolving hostname or on routable
# interfaces; everything else still runs.
%pyproject_run_pytest tests \
	--deselect tests/test_client.py::TestClientWithSetHost::test_uri_parser \
	--deselect tests/test_client.py::TestClientWithHostlessMessages::test_uri_parser \
	--deselect tests/test_reverseproxy.py::TestReverseProxy::test_options \
	--deselect tests/test_reverseproxy.py::TestReverseProxy::test_routing \
	--deselect tests/test_tls.py::TestTLS::test_tls \
	--deselect tests/test_uri_path_abbrev.py::TestClientWithSetHost::test_uri_path_abbrev_conflict \
	--deselect tests/test_commandline.py::TestCommandlineClient::test_blame_broadcast \
	--deselect tests/test_commandline.py::TestCommandlineClient::test_blame_connectivity_ipv4 \
	--deselect tests/test_commandline.py::TestCommandlineClient::test_blame_multicast_con

%files
%_bindir/aiocoap-*
%python3_sitelibdir/aiocoap
%python3_sitelibdir/aiocoap-%version.dist-info

%changelog
* Fri Oct 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.17-alt1
- 0.4.17 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.11-alt1
- 0.4.11 released

* Thu May 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.7-alt1
- 0.4.7 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.4-alt1
- 0.4.4 released
