%define _unpackaged_files_terminate_build 1

%global realname proper

Name: erlang-%realname
Version: 1.4.0.19.3bbd
Release: alt1
Summary: A QuickCheck-inspired property-based testing tool for Erlang
Group: Development/Erlang
License: GPLv3+
Url: https://proper-testing.github.io/
VCS: https://github.com/proper-testing/proper

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar

%description
PropEr (PROPerty-based testing tool for ERlang) is a QuickCheck-inspired
open-source property-based testing tool for Erlang.

%prep
%setup

%build
%make

%install
mkdir -p %buildroot/%_erllibdir/%realname-%version/ebin
mkdir -p %buildroot/%_erllibdir/%realname-%version/include
install -m 644 -p ebin/*.beam %buildroot/%_erllibdir/%realname-%version/ebin
install -m 644 -p ebin/%realname.app %buildroot/%_erllibdir/%realname-%version/ebin
install -m 644 -p include/*.hrl %buildroot/%_erllibdir/%realname-%version/include

%check
export ERL_LIBS=%buildroot%_erllibdir
%make test

%files
%doc COPYING
%doc doc README.md
%_erllibdir/%realname-%version

%changelog
* Tue Oct 25 2022 Egor Ignatov <egori@altlinux.org> 1.4.0.19.3bbd-alt1
- Merge with upstream/master to fix build with OTP-25.1.1

* Tue Oct 12 2021 Egor Ignatov <egori@altlinux.org> 1.4-alt1
- 1.4

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt2
- Fixed build with rebar2.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt1
- Updated to upstream version 1.3.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1
- Initial build for ALT.
