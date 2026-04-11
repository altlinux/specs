%define _unpackaged_files_terminate_build 1

%define realname eimp

%def_with check

Name: erlang-%realname
Version: 1.0.27
Release: alt1
Summary: Erlang Image Manipulation Process
Group: Development/Erlang
License: Apache-2.0
Url: https://github.com/processone/eimp
Vcs: https://github.com/processone/eimp.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-p1_utils
BuildRequires: libgd3-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libwebp-devel

%description
eimp is an Erlang/Elixir application for manipulating graphic images
using external C libraries. It supports WebP, JPEG, PNG and GIF.

%prep
%setup

%build
%autoreconf
%configure
%rebar_compile

%install
%rebar_install %realname

%check
mkdir -p .eunit/priv/bin
cp priv/bin/eimp .eunit/priv/bin/
%rebar_eunit

%files
%doc LICENSE.txt
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Sat Apr 11 2026 Anton Farygin <rider@altlinux.org> 1.0.27-alt1
- 1.0.26 -> 1.0.27

* Mon Nov 17 2025 Ilya Sorochan <k0tran@altlinux.org> 1.0.26-alt1
- Updated to upstream version 1.0.26.
- Enabled tests.
- Added Vcs tag.
- Removed %%set_verify_elf_method relaxed.

* Mon Jul 26 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.21-alt1
- Updated to upstream version 1.0.21.

* Fri Jun 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.20-alt1
- Updated to upstream version 1.0.20.

* Wed Feb 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.19-alt1
- Updated to upstream version 1.0.19.

* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.18-alt1
- Updated to upstream version 1.0.18.

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.17-alt1
- Updated to upstream version 1.0.17.

* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.14-alt1
- Updated to upstream version 1.0.14.

* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.11-alt1
- Updated to upstream version 1.0.11.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.10-alt1
- Updated to upstream version 1.0.10.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.9-alt1
- Updated to upstream version 1.0.9.

* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.4-alt1
- Initial build for ALT.
