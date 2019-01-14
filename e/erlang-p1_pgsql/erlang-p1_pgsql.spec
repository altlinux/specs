%define _unpackaged_files_terminate_build 1

%global realname p1_pgsql

Name: erlang-%realname
Version: 1.1.6
Release: alt1
Summary: Pure Erlang PostgreSQL driver
Group: Development/Erlang
License: ERPL
BuildArch: noarch
Url: https://github.com/processone/p1_pgsql

# https://github.com/processone/p1_pgsql.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
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
* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.6-alt1
- Updated to upstream version 1.1.6.

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.5-alt1
- Initial build for ALT.
