%global realname lager

Name: erlang-%realname
Version: 3.4.2
Release: alt1%ubt
Summary: A logging framework for Erlang/OTP
Group: Development/Erlang
License: ASL 2.0
BuildArch: noarch
Url: https://github.com/erlang-lager/lager

# https://github.com/erlang-lager/lager.git
Source: %name-%version.tar

%add_erlang_req_modules_skiplist lager_default_tracer

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: erlang-goldrush
BuildRequires: rebar

%description
Lager (as in the beer) is a logging framework for Erlang. Its purpose is to
provide a more traditional way to perform logging in an erlang application that
plays nicely with traditional UNIX logging tools like logrotate and syslog.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Fri Apr 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.2-alt1%ubt
- Updated to upstream version 3.4.2.

* Mon Oct 23 2017 Denis Medvedev <nbr@altlinux.org> 3.1.0-alt1.1
- Rebuild with fixed rpm-build-erlang.

* Fri Apr 08 2016 Denis Medvedev <nbr@altlinux.org> 3.1.0-alt1
- Initial Sisyphus release
