%global realname p1_oauth2

Name: erlang-%realname
Version: 0.6.2
Release: alt1.git5806c87%ubt

Summary: An Oauth2 implementation for Erlang
Group: Development/Erlang
License: MIT
BuildArch: noarch
Url: https://github.com/processone/p1_oauth2

# https://github.com/processone/p1_oauth2.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-proper
BuildRequires: erlang-meck

%description
This library is designed to simplify the implementation of the server side of
OAuth2. It is a fork of erlang-oauth2 by processone, and is needed by ejabberd.

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
* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.2-alt1.git5806c87%ubt
- Initial build for ALT.
