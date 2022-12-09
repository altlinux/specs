%def_with check

%define oname priority

Name: python3-module-%oname
Version: 2.0.0
Release: alt1

Summary: A pure-Python implementation of the HTTP/2 priority tree

Url: http://python-hyper.org/priority/
License: MIT
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# https://github.com/python-hyper/priority
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-hypothesis
%endif

%description
Priority is a pure-Python implementation of the priority logic for HTTP/2, set
out in `RFC 7540 Section 5.3 (Stream Priority)`_. This logic allows for clients
to express a preference for how the server allocates its (limited) resources to
the many outstanding HTTP requests that may be running over a single HTTP/2
connection.

Specifically, this Python implementation uses a variant of the implementation
used in the excellent `H2O`_ project. This original implementation is also the
inspiration for `nghttp2's`_ priority implementation, and generally produces a
very clean and even priority stream. The only notable changes from H2O's
implementation are small modifications to allow the priority implementation to
work cleanly as a separate implementation, rather than being embedded in a
HTTP/2 stack directly.

While priority information in HTTP/2 is only a suggestion, rather than an
enforceable constraint, where possible servers should respect the priority
requests of their clients.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%tox_check

%files
%python3_sitelibdir/*

%changelog
* Thu Dec 08 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Build new version.
- Build with check.

* Thu Aug 05 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt2
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1.qa1
- NMU: applied repocop patch

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Sisyphus

