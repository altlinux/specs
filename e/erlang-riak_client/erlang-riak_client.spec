%global realname riakc

Name: erlang-riak_client
Version: 2.5.3
Release: alt3
Summary: Erlang client for Riak
Group: Development/Erlang
License: ASL 2.0
BuildArch: noarch
Url: https://github.com/processone/riak-erlang-client

# https://github.com/processone/riak-erlang-client.git
Source: %name-%version.tar

Patch1: erlang-riak_client-alt-nowarn.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-riak_pb

%description
Erlang client for Riak.

%prep
%setup
%patch1 -p1

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt2
- NMU: remove %ubt from release

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.3-alt1%ubt
- Initial build for ALT.
