%define _unpackaged_files_terminate_build 1

%global realname stun

Name: erlang-%realname
Version: 1.0.26
Release: alt1
Summary: STUN and TURN library for Erlang / Elixir
Group: Development/Erlang
License: ASL 2.0
BuildArch: noarch
Url: https://github.com/processone/stun

# https://github.com/processone/stun.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-p1_utils
BuildRequires: erlang-fast_tls

%description
STUN and TURN library for Erlang / Elixir. Both STUN (Session Traversal
Utilities for NAT) and TURN standards are used as techniques to establish media
connection between peers for VoIP (for example using SIP or Jingle) and WebRTC.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit

%files
%doc LICENSE.txt
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.26-alt1
- Updated to upstream version 1.0.26.

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.21-alt1
- Initial build for ALT.
