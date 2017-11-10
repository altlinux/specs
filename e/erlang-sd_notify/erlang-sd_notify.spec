%define realname sd_notify

Name: erlang-%realname
Version: 1.0
Release: alt1
Summary: Erlang interface to systemd notify subsystem
Group: Development/Erlang
License: MIT
Url: https://github.com/systemd/erlang-sd_notify
#VCS: scm:git:https://github.com/systemd/erlang-sd_notify.git
Source: %name-%version.tar

BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: rpm-build-erlang rebar
BuildRequires: libsystemd-devel

%description
%summary.

%prep
%setup

%build
rebar compile

%install
mkdir -p %buildroot%_otplibdir/%realname-%version/{ebin,priv}
install -m 644 -p ebin/%realname.app %buildroot%_otplibdir/%realname-%version/ebin
install -m 644 -p ebin/%realname.beam %buildroot%_otplibdir/%realname-%version/ebin
install -m 755 -p priv/%{realname}_drv.so %buildroot%_otplibdir/%realname-%version/priv

%check
# Empty for now
#rebar eunit -v

%files
%doc LICENSE
%_otplibdir/*

%changelog
* Fri Nov 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Wed Sep 16 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build
