Name: webui-vue
Version: 1.0
Release: alt1.gitce7db82.1

Summary: webui-vue is a web-based user interface for the OpenBMC firmware stack built on Vue.js
License: Apache-2.0
Group: Networking/Other
BuildArch: noarch
Url: https://github.com/openbmc/webui-vue 
Vcs: https://github.com/openbmc/webui-vue.git 

Source0: %name-%version.tar
Source1: vendor.tar

Patch: Add_useful_makefile.patch
Patch1: Fix_build_by_new_nodejs_v22.patch
Patch2: Use_the_require_syntax_within_a_bound_attribute.patch

BuildRequires: npm
BuildRequires: node

%description
%summary.

%prep
%setup -a1
%autopatch -p1

%build
%make_build build

%install
%makeinstall_std

%files
%_datadir/bmcweb

%changelog
* Wed Mar 14 2026 Anatoly Mukosey <mukav@altlinux.org> 1.0-alt1.gitce7db82.1
- Initial build for Sisyphus.
