%global realname p1_utils

Name: erlang-%realname
Version: 1.0.11
Release: alt1%ubt
Summary: Erlang Utility Modules from ProcessOne
Group: Development/Erlang
License: ASL 2.0
BuildArch: noarch
Url: https://github.com/processone/p1_utils

# https://github.com/processone/p1_utils.git
Source: %name-%version.tar

%add_erlang_req_modules_skiplist str

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar

%description
Erlang Utility Modules from ProcessOne.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE.txt
%doc doc README.md
%_erllibdir/%realname-%version

%changelog
* Fri Apr 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.11-alt1%ubt
- Initial build for ALT.
