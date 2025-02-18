%define gemname github-linguist

Name: gem-github-linguist
Version: 9.0.0
Release: alt1
Summary: GitHub Language detection
License: MIT
Group: Development/Ruby
Url: https://github.com/github/linguist
Vcs: https://github.com/github/linguist.git

Source: %name-%version.tar
Source1: samples.json

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(charlock_holmes)
BuildRequires: gem(mini_mime)
BuildRequires: gem(rugged)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

Provides: gem(github-linguist) = 9.0.0

%description
We use this library at GitHub to detect blob languages, highlight code, ignore
binary files, suppress generated files in diffs, and generate language breakdown
graphs.

%package -n github-linguist
Summary: GitHub Language detection
Group: Other

Requires: gem(github-linguist) = 9.0.0

%description  -n github-linguist
We use this library at GitHub to detect blob languages, highlight code, ignore
binary files, suppress generated files in diffs, and generate language breakdown
graphs.

%package devel
Summary: Headers for gem-github-linguist
Group: Development/Ruby

Requires: gem(github-linguist) = 9.0.0

%description devel
This package contains development files for gem-github-linguist.

%package doc
Summary: Docs for gem-github-linguist
Group: Development/Documentation

Requires: gem(github-linguist) = 9.0.0

%description doc
This package contains docs for gem-github-linguist.

%prep
%setup
%patch -p1

%build
%ruby_build

%install
%ruby_install
install -Dm 644 %SOURCE1 %buildroot%ruby_gemlibdir/lib/linguist/

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files doc
%ruby_gemdocdir

%files devel
%ruby_includedir/*

%files -n github-linguist
%_bindir/git-linguist
%_bindir/github-linguist

%changelog
* Fri Feb 14 2025 Andrey Kovalev <ded@altlinux.org> 9.0.0-alt1
- Initial build for Sisyphus.
