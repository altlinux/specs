%define realname sd_notify

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0
Release: alt1%ubt
Summary: Erlang interface to systemd notify subsystem
Group: Development/Erlang
License: MIT
Url: https://github.com/systemd/erlang-sd_notify

#VCS: scm:git:https://github.com/systemd/erlang-sd_notify.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: rebar
BuildRequires: libsystemd-devel

%description
%summary.

%prep
%setup

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
* Sat Apr 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1%ubt
- Rebuilt to fix linking.

* Fri Nov 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Wed Sep 16 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build
