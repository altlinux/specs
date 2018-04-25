%global realname goldrush

Name: erlang-%realname
Version: 0.1.9
Release: alt1%ubt
Summary: Small, fast event processing and monitoring for Erlang/OTP applications
License: MIT
Group: Development/Erlang
BuildArch: noarch
Url: https://github.com/DeadZen/goldrush

# https://github.com/DeadZen/goldrush.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: rebar

%description
A small Erlang app that provides fast event stream processing.

%prep
%setup

%build
%rebar_compile
%rebar_doc

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE
%doc doc README.org
%_erllibdir/%realname-%version

%changelog
* Fri Apr 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.9-alt1%ubt
- Updated to upstream version 0.1.9.

* Fri Apr 08 2016 Denis Medvedev <nbr@altlinux.org> 0.1.8-alt1
- Initial Sisyphus release.
