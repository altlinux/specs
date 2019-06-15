%global realname luerl

Name: erlang-%realname
Version: 0.3
Release: alt2
Summary: Lua in Erlang
Group: Development/Erlang
License: ASL 2.0
BuildArch: noarch
Url: https://github.com/rvirding/luerl

# https://github.com/rvirding/luerl.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar

%description
An experimental implementation of Lua 5.2 written solely in pure Erlang.

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
* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2
- NMU: remove %ubt from release

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt1%ubt
- Initial build for ALT.
