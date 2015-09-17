%define realname sd_notify

Name: erlang-%realname
Version: 0.1
Release: alt1
Summary: Erlang interface to systemd notify subsystem
Group: Development/Erlang
License: MIT
Url: https://github.com/lemenkov/erlang-sd_notify
#VCS: scm:git:https://github.com/lemenkov/erlang-sd_notify.git
Source: %name-%version.tar

BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: rpm-build-erlang rebar
BuildRequires: libsystemd-devel

%description
%summary.

%prep
%setup

%build
CFLAGS="%optflags" LDFLAGS=-lsystemd REBAR_FLAGS="--verbose 2" make %{?_smp_mflags}

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
* Wed Sep 16 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build
