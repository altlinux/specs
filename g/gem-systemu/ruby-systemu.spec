%define        pkgname systemu

Name:          gem-%pkgname
Version:       2.6.6
Release:       alt0.1
Summary:       Univeral capture of stdout and stderr and handling of child process pid for windows, *nix, etc.
License:       BSD-2-Clause or Ruby
Group:         Development/Ruby
Url:           https://github.com/ahoward/systemu
Vcs:           https://github.com/ahoward/systemu.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Universal capture of stdout and stderr and handling of child process pid
for windows, *nix, etc.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Apr 13 2020 Pavel Skrylev <majioa@altlinux.org> 2.6.6-alt0.1
- > Ruby Policy 2.0
- ^ 2.6.5 -> 2.6.6pre (closes #38350)
- * re-licencing
- ! spec tags and syntax

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1.2
- Rebuild with new Ruby autorequirements.

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version from https://rubygems.org/gems/systemu/versions/2.6.5

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- Initial build for ALT Linux
