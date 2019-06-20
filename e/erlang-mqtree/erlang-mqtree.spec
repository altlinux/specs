%define _unpackaged_files_terminate_build 1

%global realname mqtree

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.3
Release: alt1
Summary: Index tree for MQTT topic filters
Group: Development/Erlang
License: ASL 2.0
Url: https://github.com/processone/mqtree

# https://github.com/processone/mqtree.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-p1_utils

%description
mqtree is an Erlang NIF implementation of N-ary tree to keep MQTT
topic filters for efficient matching.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.3-alt1
- Updated to upstream version 1.0.3.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Initial build for ALT.
