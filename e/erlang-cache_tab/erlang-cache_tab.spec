%global realname cache_tab

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.13
Release: alt1%ubt
Summary: In-memory cache Erlang / Elixir library
Group: Development/Erlang
License: ASL 2.0
Url: https://github.com/processone/cache_tab

# https://github.com/processone/cache_tab.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-p1_utils

%description
In-memory cache Erlang / Elixir library.

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
* Fri Apr 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.13-alt1%ubt
- Initial build for ALT.
