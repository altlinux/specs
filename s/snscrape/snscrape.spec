# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: snscrape
Version: 0.4.3.20220106
Release: alt1
Summary: A social networking service scraper in Python
License: GPL-3.0-or-later
Group: Networking/File transfer
Url: https://github.com/JustAnotherArchivist/snscrape

Requires: glibc-gconv-modules
Requires: python3-module-beautifulsoup4
Requires: python3-module-lxml
Requires: python3-module-pytz
Requires: tzdata

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%description
snscrape is a scraper for social networking services (SNS). It scrapes things
like user profiles, hashtags, or searches and returns the discovered items,
e.g. the relevant posts.

The following services are currently supported:

- Facebook: user profiles, groups, and communities (aka visitor posts)
- Instagram: user profiles, hashtags, and locations
- Mastodon: user profiles and toots (single or thread)
- Reddit: users, subreddits, and searches (via Pushshift)
- Telegram: channels
- Twitter: users, user profiles, hashtags, searches, tweets (single or
  surrounding thread), list posts, and trends
- VKontakte: user profiles
- Weibo (Sina Weibo): user profiles

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%files
%doc LICENSE README.md
%_bindir/snscrape
%python3_sitelibdir/%{name}*

%changelog
* Mon Oct 31 2022 Vitaly Chikunov <vt@altlinux.org> 0.4.3.20220106-alt1
- First import v0.4.3.20220106 (2022-01-06).
