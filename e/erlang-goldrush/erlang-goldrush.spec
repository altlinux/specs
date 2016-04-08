%global realname goldrush
%global upstream DeadZen
# Technically, we're noarch; but erlang whose directories we install into is not.
%global debug_package %nil
%global _erllibdir /usr/lib/erlang/lib/

Name: erlang-goldrush
Version: 0.1.8
Release: alt1
Summary: Small, fast event processing and monitoring for Erlang/OTP applications
License: MIT
Group: Development/Erlang 
Url: https://github.com/%upstream/%realname
Packager: Denis Medvedev <nbr@altlinux.org>

Source: erlang-%realname-%version.tar.gz
BuildRequires: rebar
BuildPreReq: erlang-devel erlang-otp-devel
BuildArch: noarch

%description
A small Erlang app that provides fast event stream processing.

%prep
%setup -n erlang-%realname-%version

%build
rebar compile
rebar doc

%install
mkdir -p %buildroot%_erllibdir/%realname-%version/ebin
install -p -m 644 ebin/%realname.app ebin/*.beam %buildroot%_erllibdir/%realname-%version/ebin

%check
rebar eunit -C rebar.test.config

%files
%doc LICENSE
%doc doc README.org
%_erllibdir/%realname-%version

%changelog
* Fri Apr 08 2016 Denis Medvedev <nbr@altlinux.org> 0.1.8-alt1
- Initial Sisyphus release.
