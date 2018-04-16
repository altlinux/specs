%global realname sqlite3

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.1.6
Release: alt1%ubt
Summary: Sqlite gen_server port for Erlang. Creates, reads and writes to sqlite database.
Group: Development/Erlang
License: Erlang Public License Version 1.1
Url: https://github.com/processone/erlang-sqlite3

# https://github.com/processone/erlang-sqlite3.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: libsqlite3-devel

%description
This library allows you to work with SQLite3 databases from Erlang.

%prep
%setup
rm -rf sqlite3_amalgamation

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
* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.6-alt1%ubt
- Initial build for ALT.
