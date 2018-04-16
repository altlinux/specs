%global realname riak_pb

Name: erlang-%realname
Version: 2.3.2
Release: alt1%ubt
Summary: Riak Protocol Buffers Messages
Group: Development/Erlang
License: ASL 2.0
BuildArch: noarch
Url: https://github.com/basho/riak_pb

# https://github.com/basho/riak_pb.git
Source: %name-%version.tar

# https://github.com/basho/riak_pb/pull/227
Patch1: erlang-riak_pv-upstream-nowarn.patch
Patch2: erlang-riak_pb-alt-deps.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-hamcrest
BuildRequires: erlang-protobuffs

%description
The message definitions for the Protocol Buffers-based interface to Riak and
various Erlang-specific utility modules for the message types.

%prep
%setup
%patch1 -p1
%patch2 -p1

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
* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.2-alt1%ubt
- Initial build for ALT.
