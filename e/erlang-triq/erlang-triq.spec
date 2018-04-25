%global realname triq

%add_erlang_req_modules_skiplist triq_rnd

Name: erlang-%realname
Version: 1.2.0
Release: alt1%ubt
Summary: A property-based testing library for Erlang
Group: Development/Erlang
License: Apache 2.0
BuildArch: noarch
Url: https://github.com/triqng/triq

# https://github.com/triqng/triq.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar

%description
A property-based testing library for Erlang.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
export ERL_LIBS=%buildroot%_erllibdir
%rebar_eunit -C rebar.config.script

%files
%doc LICENSE
%doc README.org
%_erllibdir/%realname-%version

%changelog
* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt1%ubt
- Initial build for ALT.
