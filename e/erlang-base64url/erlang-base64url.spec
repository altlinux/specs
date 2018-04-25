%global realname base64url

Name: erlang-%realname
Version: 1.0
Release: alt1%ubt
Summary: URL safe base64-compatible codec
Group: Development/Erlang
License: MIT
BuildArch: noarch
Url: https://github.com/dvv/base64url

# https://github.com/dvv/base64url.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar

%description
Standalone URL safe base64-compatible codec.

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
* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1%ubt
- Initial build for ALT.
