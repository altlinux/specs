%define _unpackaged_files_terminate_build 1
%define pypi_name anyio

%def_with check

Name: python3-module-anyio
Version: 4.2.0
Release: alt1

Summary: High level compatibility layer for multiple asynchronous event loop implementations
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/anyio
Vcs: https://github.com/agronholm/anyio

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-trio-tests
%pyproject_builddeps_metadata_extra test
%endif

# either asyncio or trio
%filter_from_requires /python3(trio.*)/d
# clean pytest from requirements
%add_python3_req_skip pytest

%description
AnyIO is an asynchronous networking and concurrency library
that works on top of either asyncio or trio.
It implements trio-like structured concurrency (SC) on top of asyncio,
and works in harmony with the native SC of trio itself.

Applications and libraries written against AnyIO's API will run
unmodified on either asyncio or trio.
AnyIO can also be adopted into a library or application incrementally -
bit by bit, no full refactoring necessary.
It will blend in with native libraries of your chosen backend.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# Next "bad tests" don't work within hasher, where network and name resolution
# aren't configured.
## Wrong localhost address
badtests+=" or (TestTCPStream and (test_happy_eyeballs and (ipv6 or dualstack)"
badtests+=" or (test_connection_refused and multi)))"
badtests+=" or (TestTCPListener and test_bind_link_local)"

## Bind and resolution failure
badtests+=" or (TestTCPStream and ipv6 and (test_send_after_close"
badtests+="     or test_unretrieved_future_exception_server_crash"
badtests+="     or test_send_after_peer_closed or test_iterate"
badtests+="     or test_connect_tcp_with_tls_cert_check_fail"
badtests+="     or test_connect_tcp_with_tls or test_send_eof"
badtests+="     or test_receive_after_close or test_send_large_buffer"
badtests+="     or test_close_during_receive or test_send_receive"
badtests+="     or test_concurrent_receive or test_extra_attributes"
badtests+="     or test_socket_options or test_receive_timeout"
badtests+="     or test_concurrent_send))"
badtests+=" or (test_reuse_port and (TestConnectedUDPSocket or TestUDPSocket"
badtests+="     or TestTCPListener))"
badtests+=" or ((TestConnectedUDPSocket or TestUDPSocket)"
badtests+="     and (test_receive_after_close or test_send_after_close"
badtests+="         or test_close_during_receive or test_send_receive"
badtests+="         or test_iterate or test_close_during_receive"
badtests+="         or test_concurrent_receive))"
badtests+=" or (TestConnectedUDPSocket and test_extra_attributes and ipv6)"
badtests+=" or (TestUDPSocket and test_extra_attributes)"
badtests+=" or (TestTCPListener and (test_send_after_eof"
badtests+="     or test_close_from_other_task or test_socket_options"
badtests+="     or test_accept_after_close or (test_accept and (ipv4 or ipv6))"
badtests+="     or test_extra_attributes))"
%pyproject_run_pytest -Wignore -m "not network" -k "not (${badtests:4})"

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Feb 08 2024 Alexandr Shashkin <dutyrok@altlinux.org> 4.2.0-alt1
- 3.6.2 -> 4.2.0

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 3.6.2-alt1
- new version 3.6.2 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 3.6.1-alt1
- new version 3.6.1 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.5.0-alt1
- new version 3.5.0 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- initial build for ALT Sisyphus
