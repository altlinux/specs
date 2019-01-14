%define _unpackaged_files_terminate_build 1

%global realname fast_yaml

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.17
Release: alt1
Summary: Fast YAML native library for Erlang / Elixir
Group: Development/Erlang
License: ASL 2.0
Url: https://github.com/processone/fast_yaml

# https://github.com/processone/fast_yaml.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-p1_utils
BuildRequires: libyaml-devel

%description
Fast YAML is an Erlang wrapper for libyaml "C" library.

It is designed to be fast and efficient.

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
* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.17-alt1
- Updated to upstream version 1.0.17.

* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.13-alt1
- Initial build for ALT.
