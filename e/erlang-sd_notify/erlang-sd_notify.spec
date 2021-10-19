%define _unpackaged_files_terminate_build 1

%define realname sd_notify

Name: erlang-%realname
Version: 1.1
Release: alt1
Summary: Erlang interface to systemd notify subsystem
Group: Development/Erlang
License: MIT
Url: https://github.com/systemd/erlang-sd_notify
BuildArch: noarch

#VCS: scm:git:https://github.com/systemd/erlang-sd_notify.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: rebar
BuildRequires: libsystemd-devel

%description
%summary.

%prep
%setup

%build
rebar3 compile

%install
mkdir -p %buildroot/%_erllibdir/%realname-%version/ebin
install -m 644 -p _build/default/lib/sd_notify/ebin/%realname.app %buildroot/%_erllibdir/%realname-%version/ebin
install -m 644 -p _build/default/lib/sd_notify/ebin/%realname.beam %buildroot/%_erllibdir/%realname-%version/ebin

%check
rebar3 eunit

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Tue Oct 12 2021 Egor Ignatov <egori@altlinux.org> 1.1-alt1
- 1.1

* Tue Mar 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt5
- Fixed build with rebar2.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3
- NMU: remove %%ubt from release

* Tue May 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt2
- Disabled tests.

* Sat Apr 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Rebuilt to fix linking.

* Fri Nov 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Wed Sep 16 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build
