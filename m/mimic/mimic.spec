Name: mimic
Version: 0.0.1
Release: alt1

Summary: [ab]using Unicode to create tragedy
License: %mit
Group: Text tools
BuildArch: noarch

URL: https://github.com/reinderien/mimic
# https://github.com/reinderien/mimic.git
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

Requires: python3-module-docutils

%define _unpackaged_files_terminate_build 1

%description
mimic provokes:

* fun
* frustration
* curiosity
* murderous rage

It's inspired by this terrible idea floating around:
  MT: Replace a semicolon with a greek question mark in your
  friend's C# code and watch them pull their hair out over the syntax
  error
    - Peter Ritchie (@peterritchie) November 16, 2014

There are many more characters in the Unicode character set that look,
to some extent or another, like others - homoglyphs. Mimic substitutes
common ASCII characters for obscure homoglyphs.

Fun games to play with mimic:

* Pipe some source code through and see if you can find all of
  the problems
* Pipe someone else's source code through without telling them
* Be fired, and then killed

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install

%files
%doc README.md LICENSE.md
%_bindir/%name
%python3_sitelibdir_noarch/%{name}*

%changelog
* Fri Jun 10 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1
- Fix version.
- Set license.
- Updated from upstream git.

* Mon Oct 26 2015 Mikhail Efremov <sem@altlinux.org> 0-alt1
- Initial build

