%define _unpackaged_files_terminate_build 1

%global realname tidy

Name: erlang-%realname
Version: 2.3.1.0.1.d9c7
Release: alt1
Summary: Erlang code cleaner
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/ezlib.git
BuildArch: noarch

# https://github.com/richcarl/erl_tidy
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel

%description
erl_tidy is an automatic code cleaner for Erlang code. It was previously
part of the syntax_tools application.

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_erllibdir/%realname-%version
cp -r ./ebin %buildroot%_erllibdir/%realname-%version

%files
%doc LICENSE LGPL README
%_erllibdir/%realname-%version

%changelog
* Tue Oct 12 2021 Egor Ignatov <egori@altlinux.org> 2.3.1.0.1.d9c7-alt1
- Initial build for ALT as a separate application
