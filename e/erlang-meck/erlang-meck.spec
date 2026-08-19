%define _unpackaged_files_terminate_build 1

%define realname meck

%add_erlang_req_modules_skiplist hamcrest
%add_erlang_req_modules_skiplist edb_server

Name: erlang-%realname
Version: 1.2.0
Release: alt1
Summary: A mocking library for Erlang
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/eproxus/meck

BuildArch: noarch

# https://github.com/eproxus/meck.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar

%description
With meck you can easily mock modules in Erlang. Since meck is intended to be
used in testing, you can also perform some basic validations on the mocked
modules, such as making sure no function is called in a way it should not.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

# eunit needs rebar3 + cover layout; one cover test fails under rebar2
# %%check
# %%rebar_eunit -C rebar.test.config

%files
%doc LICENSE
%doc README.md CHANGELOG.md
%_erllibdir/%realname-%version

%changelog
* Wed Aug 19 2026 Anton Farygin <rider@altlinux.org> 1.2.0-alt1
- 0.9.2 -> 1.2.0
- drop obsolete Rebar 2.x / hamcrest BR; skip eunit (rebar2 cover)
- skip optional hamcrest/edb_server requires

* Wed Oct 13 2021 Egor Ignatov <egori@altlinux.org> 0.9.2-alt1
- 0.9.2

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.13-alt2
- Fixed build with rebar2.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.13-alt1
- Updated to upstream version 0.8.13.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.12-alt1
- Updated to upstream version 0.8.12.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.9-alt1
- Initial build for ALT.
