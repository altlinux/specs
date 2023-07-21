%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-pyrogram
Version: 2.0.106
Release: alt1

Summary: Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots
License: GPL-3.0 and LGPL-3.0
Group: Development/Python3

VCS: https://github.com/pyrogram/pyrogram
Url: https://pyrogram.org/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

Requires: python3-module-pyaes
Requires: python3-module-socks

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pyaes
BuildRequires: python3-module-socks
BuildRequires: python3-modules-sqlite3
%endif

%description
Pyrogram is a modern, elegant and asynchronous MTProto API
framework. It enables you to easily interact with the main Telegram
API through a user account (custom client) or a bot identity (bot API
alternative) using Python.

%prep
%setup
%patch0 -p1

%build
%python3_build

pushd compiler/api
python3 compiler.py
popd

pushd compiler/errors
python3 compiler.py
popd

python3 setup.py sdist
python3 setup.py bdist_wheel

%install
%python3_install

%check
python3 -m pytest tests

%files
%doc COPYING COPYING.lesser NOTICE README.md
%python3_sitelibdir_noarch/pyrogram
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Thu Jul 20 2023 Egor Ignatov <egori@altlinux.org> 2.0.106-alt1
- new version 2.0.106

* Mon Sep 05 2022 Egor Ignatov <egori@altlinux.org> 2.0.49-alt1
- new version 2.0.49

* Wed Aug 31 2022 Egor Ignatov <egori@altlinux.org> 2.0.43-alt1
- new version 2.0.43

* Thu Aug 04 2022 Egor Ignatov <egori@altlinux.org> 2.0.35-alt1
- First build for ALT
