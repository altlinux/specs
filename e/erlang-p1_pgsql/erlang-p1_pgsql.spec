%global realname p1_pgsql

Name: erlang-%realname
Version: 1.1.5
Release: alt1%ubt
Summary: Pure Erlang PostgreSQL driver
Group: Development/Erlang
License: ERPL
BuildArch: noarch
Url: https://github.com/processone/p1_pgsql

# https://github.com/processone/p1_pgsql.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar

%description
This is an Erlang PostgreSQL driver.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit

%files
%doc EPLICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.5-alt1%ubt
- Initial build for ALT.
