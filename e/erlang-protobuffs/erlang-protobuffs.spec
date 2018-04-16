%global realname protobuffs

Name: erlang-%realname
Version: 0.9.0
Release: alt1%ubt
Summary: A set of Protocol Buffers tools and modules for Erlang applications
Group: Development/Erlang
License: Apache 2.0
BuildArch: noarch
Url: https://github.com/basho/erlang_protobuffs

# https://github.com/basho/erlang_protobuffs.git
Source: %name-%version.tar
Source1: erlang-protobuffs-fedora-protoc-erl

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-common_test-devel
BuildRequires: erlang-meck

%description
An implementation of Google's Protocol Buffers for Erlang.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

# Install Erlang protobuf compiler script
install -D -p -m 0755 %SOURCE1 %buildroot%_bindir/protoc-erl

%check
%rebar_eunit

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version
%_bindir/*

%changelog
* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1%ubt
- Initial build for ALT.
