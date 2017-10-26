%global realname lager
%global upstream basho
%global debug_package %nil
%global _erllibdir /usr/lib/erlang/lib

Name: erlang-lager
Version: 3.1.0
Release: alt1.1

Summary: A logging framework for Erlang/OTP
Group: Development/Erlang
License: ASL 2.0
Url: http://github.com/%upstream/%realname
Packager: Denis Medvedev <nbr@altlinux.org>
BuildArch: noarch

Source: erlang-%realname-%version.tar.gz

BuildRequires: erlang-goldrush >= 0.1.8
BuildRequires: rebar
BuildPreReq: erlang-otp-devel erlang-devel

%description
Lager (as in the beer) is a logging framework for Erlang. Its purpose is to
provide a more traditional way to perform logging in an erlang application that
plays nicely with traditional UNIX logging tools like logrotate and syslog.

%prep
%setup -n erlang-%realname-%version

%build
rebar compile

%install
install -p -m 0644 -D ebin/%realname.app %buildroot%_erllibdir/%realname-%version/ebin/%realname.app
install -p -m 0644 ebin/%{realname}*.beam %buildroot%_erllibdir/%realname-%version/ebin
install -p -m 0644 ebin/error_logger_lager_h.beam %buildroot%_erllibdir/%realname-%version/ebin
install -p -m 0644 -D include/%realname.hrl %buildroot%_erllibdir/%realname-%version/include/%realname.hrl

%files
%doc LICENSE
%doc README.md
%dir %_erllibdir/%realname-%version
%dir %_erllibdir/%realname-%version/ebin
%dir %_erllibdir/%realname-%version/include
%_erllibdir/%realname-%version/ebin/%realname.app
%_erllibdir/%realname-%version/ebin/error_logger_lager_h.beam
%_erllibdir/%realname-%version/ebin/%{realname}*.beam
%_erllibdir/%realname-%version/include/%realname.hrl

%changelog
* Mon Oct 23 2017 Denis Medvedev <nbr@altlinux.org> 3.1.0-alt1.1
- Rebuild with fixed rpm-build-erlang.

* Fri Apr 08 2016 Denis Medvedev <nbr@altlinux.org> 3.1.0-alt1
- Initial Sisyphus release
