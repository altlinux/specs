%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global realname p1_acme

Name: erlang-%realname
Version: 1.0.16
Release: alt1
Summary: ACME client library for Erlang
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/p1_acme

BuildArch: noarch

# https://github.com/processone/p1_acme.git
Source: %name-%version.tar

%add_erlang_req_modules_skiplist str

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-jiffy
BuildRequires: erlang-yconf
BuildRequires: erlang-idna
BuildRequires: erlang-jose
BuildRequires: erlang-base64url

%description
Erlang ACME client (RFC8555).

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE.txt
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Mon Jan 17 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.16-alt1
- Updated to upstream version 1.0.16.

* Mon Jul 26 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.13-alt1
- Updated to upstream version 1.0.13.

* Fri Jun 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.12-alt1
- Updated to upstream version 1.0.12.

* Wed Feb 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.11-alt1
- Updated to upstream version 1.0.11.

* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.10-alt1
- Updated to upstream version 1.0.10.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.8-alt1
- Updated to upstream version 1.0.8.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Initial build for ALT.

