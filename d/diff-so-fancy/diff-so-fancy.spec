%define _unpackaged_files_terminate_build 1
%def_with check

Name: diff-so-fancy
Version: 1.4.14
Release: alt1

Summary: Human-readable git diffs with improved highlighting
License: MIT
Group: Development/Tools
Url: https://github.com/so-fancy/diff-so-fancy
Vcs: https://github.com/so-fancy/diff-so-fancy.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: rpm-build-perl
BuildRequires: perl(Encode.pm)
BuildRequires: perl(JSON/PP.pm)
BuildRequires: bats
BuildRequires: bats-support
BuildRequires: bats-assert
BuildRequires: git-core
BuildRequires: /proc

%filter_from_requires /^perl(DiffHighlight.pm)/d

%description
diff-so-fancy strives to make diffs human readable instead of machine
readable. It improves on git's diff-highlight, strips unnecessary
markers and makes file headers easier to spot.

%prep
%setup
# Use system perl instead of the first one found in PATH
sed -i '1s|^#!/usr/bin/env perl|#!/usr/bin/perl|' diff-so-fancy

%install
install -Dpm755 diff-so-fancy %buildroot%_datadir/%name/diff-so-fancy
install -Dpm644 lib/DiffHighlight.pm %buildroot%_datadir/%name/lib/DiffHighlight.pm
mkdir -p %buildroot%_bindir
ln -rs %buildroot%_datadir/%name/diff-so-fancy %buildroot%_bindir/%name
install -Dpm644 docs/diff-so-fancy.1 %buildroot%_man1dir/diff-so-fancy.1

%check
rmdir test/test_helper/bats-support test/test_helper/bats-assert
ln -s %_datadir/bats-support test/test_helper/bats-support
ln -s %_datadir/bats-assert test/test_helper/bats-assert
# bugs.bats relies on a UTF-8 locale from the environment
export LESSCHARSET=utf-8
bats test

%files
%doc LICENSE README.md docs/pro-tips.md
%_bindir/%name
%dir %_datadir/%name
%dir %_datadir/%name/lib
%_datadir/%name/diff-so-fancy
%_datadir/%name/lib/DiffHighlight.pm
%_man1dir/diff-so-fancy.1*

%changelog
* Tue Nov 17 2026 Mikhail Nogin <joycap@altlinux.org> 1.4.14-alt1
- Initial build for ALT Sisyphus.
