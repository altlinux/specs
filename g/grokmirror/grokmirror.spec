# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: grokmirror
Version: 2.0.11
Release: alt1
Summary: Smartly mirror git.kernel.org repositories
License: GPL-3.0-or-later
Group: Networking/File transfer
Url: https://www.kernel.org/mirroring-kernelorg-repositories.html
Vcs: https://git.kernel.org/pub/scm/utils/grokmirror/grokmirror.git

Requires: python3(urllib3)
%add_python3_req_skip requests.packages.urllib3.util.retry

Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
Grokmirror was written to make mirroring large git repository collections
more efficient. Grokmirror uses the manifest file published by the
master mirror in order to figure out which repositories to clone, and
to track which repositories require updating. The process is extremely
lightweight and efficient both for the master and for the mirrors.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
install -Dpm0644 man/*.1 -t %buildroot%_man1dir

%files
%define _customdocdir %_docdir/%name
%doc CHANGELOG.rst LICENSE.txt README.rst grokmirror.conf
%doc contrib/*.service contrib/*.timer contrib/logrotate
%_bindir/grok-*
%python3_sitelibdir/%{name}*
%_man1dir/grok-*.1*

%changelog
* Thu Mar 27 2024 Vitaly Chikunov <vt@altlinux.org> 2.0.11-alt1
- First import v2.0.11 (2021-08-06).
