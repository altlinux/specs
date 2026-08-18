%define _unpackaged_files_terminate_build 1

Name: rpmconf
Version: 1.1.12
Release: alt1
Summary: Tool to handle rpmnew and rpmsave files
Group: File tools
License: GPL-3.0-only
URL: https://github.com/xsuchy/rpmconf
VCS: https://github.com/xsuchy/rpmconf

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(rpm)
BuildRequires: python3(sphinx)
BuildRequires: docbook-utils
BuildRequires: docbook-dtds
BuildRequires: python3-devel

%description
This tool search for .rpmnew, .rpmsave and .rpmorig files
and ask you what to do with them:
Keep current version, place back old version, watch the diff or merge.

%package -n python3-module-%name
Summary: Python3 interface for %name
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%name
%summary.

%package -n python3-module-%name-doc
Summary: Documentation for python3-module-%name
Group: Documentation
BuildArch: noarch

%description -n python3-module-%name-doc
%summary.

%prep
%setup
%autopatch -p1

%build
sed -i 's/__version__ = .*/__version__ = "%version"/' rpmconf/rpmconf.py
sed -i 's/version = .*,/version = "%version",/' setup.py
%pyproject_build
docbook2man rpmconf.sgml
%make_build -C docs html man

%install
%pyproject_install
install -d %buildroot%_datadir/%name
install -D -m644 rpmconf.8 %buildroot%_man8dir/rpmconf.8
install -D -m644 docs/build/man/rpmconf.3 %buildroot%_man3dir/rpmconf.3

%files
%doc README.md LICENSES/GPL-3.0-only.txt
%dir %_datadir/%name
%_bindir/%name
%_man8dir/*.8.*

%files -n python3-module-%name
%doc LICENSES/GPL-3.0-only.txt
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name-%version.dist-info
%_man3dir/*.3.*

%files -n python3-module-%name-doc
%doc docs/build/html/*

%changelog
* Tue Aug 18 2026 Valery Zabrovsky <brow@altlinux.org> 1.1.12-alt1
- Initial build for ALT Sisyphus.
